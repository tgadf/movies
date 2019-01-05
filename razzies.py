import re
from time import sleep
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findPatternExt, findExt
from strUtils import convertCurrency
from webUtils import getWebData, getHTML
from movieDB import movieDB
from os import getcwd
import operator


##############################################################################################################################
# Box Office 
##############################################################################################################################
class razzies(movieDB):
    def __init__(self, basedir=None):
        self.name = "razzies"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadRazziesCategoryData(self, category, outdir, debug=False):

        url  = "https://en.wikipedia.org/wiki/Golden_Raspberry_Award_for_{0}".format(category)

        savename = setFile(outdir, category+".p")
        if isFile(savename): return
        if debug:
            print("Downloading {0}".format(url))
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(1)


    def getRazziesCategoryData(self, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)

        categories = ["Worst_Picture", "Worst_Actor", "Worst_Actress", "Worst_Director"]
        for category in categories:
            self.downloadRazziesCategoryData(category, outdir, debug)
                

                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################  
    
    
    def parseRazziesActingData(self, table, category, debug=False):
        data = {}
        
        ths = table.findAll("th")
        ths = [x.text for x in ths if x is not None]
        ths = [x.replace("\n", "") for x in ths]

        trs = table.findAll("tr")
        for i,tr in enumerate(trs[1:]):
            tds = tr.findAll("td")

            if len(tds) == 1:
                try:
                    year = int(tds[0].find("b").text)
                except:
                    raise ValueError("Expected integer year, but found {0}".format(tds[0]))

            if len(tds) == 3:
                tds = [x.text for x in tds]
                tds = [x.replace("\n", "") for x in tds]
                tds = [x.strip() for x in tds]
                tds.insert(0, year)

                try:
                    row = dict(zip(ths, tds))
                except:
                    raise ValueError("Could not zip: [{0}], [{1}]".format(ths, tds))

                if data.get(year) is None:
                    data[year] = {}
                if data[year].get(category) is None:
                    data[year][category] = []

                try:
                    movie = row["Film"]
                except:
                    raise ValueError("Cannot find movie in {0}".format(row))

                data[year][category].append(movie)


                if debug:
                    print("{0: <10}{1: <20}{2}".format(year,category,movie))
                    
        return data
    
    
    def parseRazziesFilmData(self, table, category, debug=False):
        filmdata = {}
        
        try:
            caption = table.find('caption')
            year = int(caption.find("big").text)
        except:
            raise ValueError("Cannot extract year from {0}".format(table.find('caption')))
        
        ths = table.findAll("th")
        ths = [x.text for x in ths if x is not None]
        ths = [x.replace("\n", "") for x in ths]
        
        trs = table.findAll("tr")
        for i,tr in enumerate(trs[1:]):
            tds = tr.findAll("td")
            tds = [x.text for x in tds]
            tds = [x.replace("\n", "") for x in tds]
            tds = [x.strip() for x in tds]

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

            filmdata[year][category].append(movie)


            if debug:
                print("{0: <10}{1: <20}{2}".format(year,category,movie))
                    
        return filmdata



    def parseRazziesCategoryData(self, ifile, category, debug = False):
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
            
        data   = {}
        done   = False
        tables = bsdata.findAll("table", {"class": "wikitable"})
        if debug:
            print("  Found {0} tables".format(len(tables)))
        for table in tables:
            caption = table.find("caption")
            
            if caption is None:
                yeardata = self.parseRazziesActingData(table, category, debug=False)
                data = {**data, **yeardata}
            else:
                yeardata = self.parseRazziesFilmData(table, category, debug=False)
                data = {**data, **yeardata}
        
        for year,yearData in data.items():
            for category in yearData.keys():
                data[year][category] = list(set(data[year][category]))
        
        return data



    def processRazziesCategoryData(self, debug=False):
        outdir = self.getDataDir()
        files = findExt(outdir, ext=".p")

        from collections import OrderedDict
        movies = OrderedDict()
        for ifile in files:
            
            if debug:
                print("Processing {0}".format(ifile))
            category = getBaseFilename(ifile)
            results  = self.parseRazziesCategoryData(ifile, category, debug=debug)
            
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
        print("Saving {0} Years of Razzies Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)
        #yamldata.saveYaml(savename, movies)   