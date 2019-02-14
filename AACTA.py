import re
from time import sleep
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findPatternExt, findExt
from strUtils import convertCurrency
from webUtils import getWebData, getHTML, removeTag
from movieDB import movieDB
from os import getcwd
import operator


##############################################################################################################################
# Box Office 
##############################################################################################################################
class AACTA(movieDB):
    def __init__(self, basedir=None):
        self.name = "AACTA"
        movieDB.__init__(self, dbdir=self.name)
    
    
    ###########################################################################################################################
    # Get AACTA Files
    ###########################################################################################################################
    def downloadAACTACategoryData(self, category, outdir, debug=False):

        url = "https://en.wikipedia.org/wiki/AACTA_Award_for_{0}".format(category)
        savename = setFile(outdir, category+".p")
        if isFile(savename): return
        if debug:
            print("Downloading {0}".format(url))
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(1)


    def getAACTACategoryData(self, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)

        categories = ["Best_Film",
                      "Best_Direction",
                      "Best_Actor_in_a_Leading_Role",
                      "Best_Actress_in_a_Leading_Role",
                      "Best_Actor_in_a_Supporting_Role",
                      "Best_Actress_in_a_Supporting_Role"]
        for category in categories:
            self.downloadAACTACategoryData(category, outdir, debug)
                

                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################  
    def parseAACTAFilmData(self, table, category, debug=False):
        filmdata = {}
        
        ths = table.findAll("th")
        ths = [x.text for x in ths if x is not None]
        ths = [x.replace("\n", "") for x in ths]
        
        trs  = table.findAll("tr")
        
        year = None
        for i,tr in enumerate(trs[1:]):
            tds = tr.findAll("td")
            if len(tds) == 1:
                continue
            #print(i,'\t',len(tds),'\t',tds)
            #continue
            if len(tds) == 3:
                try:
                    year = tds[0].find('b').text
                    year = year.replace("\n", "").strip()
                    if year == "1974/5":
                        year = "1974"
                    year = int(year)
                    tds = tds[1:]
                except:
                    raise ValueError("Could not find year in {0}".format(tds[0]))
                    
                    
            if len(tds) == 2:
                tds = [x.text for x in tds]
                tds = [x.replace("\n", "") for x in tds]
                tds = [x.strip() for x in tds]
                tds.insert(0, year)
            else:
                raise ValueError("Not sure what to do with this row: {0}".format(tds))
            
                
            try:
                row = dict(zip(ths, tds))
            except:
                raise ValueError("Could not zip: [{0}], [{1}]".format(ths, tds))

            if filmdata.get(year) is None:
                filmdata[year] = {}
            if filmdata[year].get(category) is None:
                filmdata[year][category] = []

            try:
                movie = row["Film"]
            except:
                raise ValueError("Cannot find movie in {0}".format(row))
                
            if movie.endswith(" ‡"):
                movie = movie[:-2]
            elif movie.endswith(" †"):
                movie = movie[:-2]


            filmdata[year][category].append(movie)
            

            if debug:
                print("{0: <10}{1: <75}{2}".format(year,category,movie))
                    
        return filmdata
    
    
    def parseAACTAActorData(self, table, category, debug=False):
        filmdata = {}
        
        ths = table.findAll("th")
        ths = [x.text for x in ths if x is not None]
        ths = [x.replace("\n", "") for x in ths]
        
        trs  = table.findAll("tr")
        
        
        year = None
        for i,tr in enumerate(trs[1:]):
            nbs = len(tr.findAll("b"))
            tds = tr.findAll("td")
            if len(tds) == 1:
                continue
            #print(i,'\t',len(tds),'\t',tds[0])
            if len(tds) == 4:
                try:
                    year = tds[0].find('b').text
                    year = year.replace("\n", "").strip()
                    if year == "1974–75":
                        year = '1974'
                    year = int(year)
                    tds  = tds[1:]
                except:
                    raise ValueError("Could not find year in {0}".format(tds[0]))

            if year is None:
                break
                    
            if len(tds) >= 2:
                tds = [x.text for x in tds]
                tds = [x.replace("\n", "") for x in tds]
                tds = [x.strip() for x in tds]
                tds.insert(0, year)
                
            if len(tds) == 3:
                tds.insert(2, tds[2])
            if len(tds) != 4:
                raise ValueError("Not sure what to do with this row: {0}".format(tds))
            
                
            try:
                row = dict(zip(ths, tds))
            except:
                raise ValueError("Could not zip: [{0}], [{1}]".format(ths, tds))

            if filmdata.get(year) is None:
                filmdata[year] = {}
            if filmdata[year].get(category) is None:
                filmdata[year][category] = []

            try:
                movie = row["Film"]
            except:
                raise ValueError("Cannot find movie in {0}".format(row))
                
            if movie.endswith(" ‡"):
                movie = movie[:-2]
            elif movie.endswith(" †"):
                movie = movie[:-2]

            if movie.find("Mitzi Del Bra") != -1:
                continue
            if movie.find("N/A") != -1:
                continue

                
            filmdata[year][category].append(movie)
            

            if debug:
                print("{0: <10}{1: <75}{2}".format(year,category,movie))
                    
        return filmdata



    def parseAACTACategoryData(self, ifile, category, debug = False):
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
            
        data   = {}
        done   = False
        tables = bsdata.findAll("table", {"class": "wikitable"})
        if debug:
            print("  Found {0} tables".format(len(tables)))
        for table in tables:
            if category.find("_Role") != -1:
                yeardata = self.parseAACTAActorData(table, category, debug=debug)
            else:
                yeardata = self.parseAACTAFilmData(table, category, debug=debug)
            #yeardata = self.parseAACTAActorData(table, category, debug=debug)                

            data = {**data, **yeardata}
        
        for year,yearData in data.items():
            for category in yearData.keys():
                data[year][category] = list(set(data[year][category]))
        
        return data



    def processAACTACategoryData(self, debug=False):
        outdir = self.getDataDir()
        files = findExt(outdir, ext="*.p")

        from collections import OrderedDict
        movies = OrderedDict()
        print(files)
        for ifile in files:
            
            if debug:
                print("Processing {0}".format(ifile))
            category = getBaseFilename(ifile)
            results  = self.parseAACTACategoryData(ifile, category, debug=debug)
            
            if len(results) == 0:
                raise ValueError("No results for {0}".format(ifile))
                

            for year,yearData in results.items():
                for category,categoryData in yearData.items():
                    if movies.get(year) is None:
                        movies[year] = []
                    for movie in categoryData:
                        movies[year].append(movie)

        for year in movies.keys():
            movies[year] = list(set(movies[year]))
            yearlyMovies = movies[year]
            movies[year] = []
            for movie in yearlyMovies:
                movies[year].append([movie,10])

        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of AACTA Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)
        #yamldata.saveYaml(savename, movies)   