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
class wikifilm(movieDB):
    def __init__(self, basedir=None):
        self.name = "wikifilm"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadWikiFilmYearlyData(self, year, outdir, debug=False):
        url = "https://en.wikipedia.org/wiki/{0}_in_film".format(year)
        savename = setFile(outdir, str(year)+".p")
        if isFile(savename): return
        if debug:
            print("Downloading {0}".format(url))
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(1)


    def getWikiFilmYearlyData(self, startYear = 1921, endYear = 2017, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)
        if startYear < 1921:
            raise ValueError("Must start at or after 1921")
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            self.downloadWikiFilmYearlyData(year, outdir, debug)
                

                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################  
    def parseWikiFilmOscarDataSpecial(self, ifile, debug = True):
        print("HI: {0}".format(ifile))
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
            
        data   = {}
        done   = False
        tables = bsdata.findAll("table", {"class": "wikitable"})
        if debug:
            print("  Found {0} tables".format(len(tables)))
        for table in tables:
            if done:
                if debug:
                    print("  Breaking...")
                break
                
                
            ## Get <th> data
            ths = table.findAll("th")
            thData = [x.find('a') for x in ths]
            titles = [x.string for x in thData if x is not None]
            if len(titles) == 0:
                continue
            
            
            ## Get <tr> data
            trData = []
            trs = table.findAll("tr")
            for tr in trs:
                tds = tr.findAll("td")
                for td in tds:
                    ul = td.find("ul")
                    if ul is not None:
                        trData.append(ul)
                        
            print(len(titles))
            print(len(trData))
            if len(titles) != len(trData):
                print("Can not process this data!")
                print("Titles: {0}: {1}".format(len(titles), titles))
                print("Data:   {0}".format(len(trData)))

                return None
            
            ## Merge titles and data
            for title,titleData in zip(titles,trData):
                results = []

                lis = titleData.findAll("li")
                if debug:
                    print("    Found {0} entries".format(len(lis)))

                for k,li in enumerate(lis):
                    text = []
                    if k == 0: 
                        for lival in li.findAll("b"):
                            for ref in lival.findAll("a"): 
                                text.append(ref.string)
                    else:
                        for ref in li.findAll("a"):
                            text.append(ref.string)
                    if len(text) == 0: continue
                    if len(text) > 2: text = [text[0], ", ".join(text[1:])]
                    text = self.reorderwikifilmOscarData(text, title)
                    results.append(text)

                for k,result in enumerate(results):
                    if isinstance(result, list):
                        if len(result) == 1: results[k] = result[0]

                data[title] = {}
                data[title]["Winner"]   = results[0]
                data[title]["Nominees"] = results[1:]
                if debug:
                    print("      Winner  :",data[title]["Winner"])
                    print("      Nominees:",data[title]["Nominees"])
                    print("")
                
        return data


    def parseWikiFilmYearlyData(self, ifile, debug = False):
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
            
        data   = {}
        done   = False
        tables = bsdata.findAll("table", {"class": "wikitable"})
        if debug:
            print("  Found {0} tables".format(len(tables)))
        for table in tables:
            if len(data) > 0:
                break
            trs = table.findAll("tr")
            headerRow = trs[0]
            ths = headerRow.findAll("th")
            if len(ths) == 0:
                raise ValueError("There are no headers in the first row!")

            ths = [x.text for x in ths]
            ths = [x.replace("\n", "") for x in ths]
            try:
                maxCol = max([ths.index("Rank"), ths.index("Title")])
            except:
                raise ValueError("No Rank/Title in header: {0}".format(ths))
            
            pRank = None
            for itr,tr in enumerate(trs[1:]):
                tds = tr.findAll("td")
                th  = tr.find("th")
                if th is not None:
                    rank = th.text
                    rank = rank.replace(".", "")
                    rank = rank.replace("\n", "").strip()
                    if len(rank) == 0:
                        rank = pRank
                    try:
                        int(rank)
                    except:
                        raise ValueError("Cannot create integer rank from {0}".format(rank))
                    rank = int(rank)
                    tds = [x.text for x in tds]
                    tds = [x.replace("\n", "") for x in tds]
                    tds.insert(0, rank)
                else:
                    tds = [x.text for x in tds]
                    tds = [x.replace("\n", "") for x in tds]
                    tds[0] = tds[0].replace(".", "")
                    if len(tds[0]) == 0:
                        tds[0] = pRank
                    
                try:
                    row = dict(zip(ths, tds))
                except:
                    row = None
                    
                if row is None:
                    try:
                        row = {"Rank": tds[ths.index("Rank")], "Title": tds[ths.index("Title")]}
                    except:
                        print("Headers: {0}".format(ths))
                        print("Values:  {1}".format(tds))
                        raise ValueError("Cannot create row dictionary")

                try:
                    int(row['Rank'])
                except:
                    raise ValueError("There is no Ranking header in this row: {0}".format(row))

                data[row['Title']] = int(row['Rank'])
                pRank = data[row['Title']]
                    
        if debug:
            print("  Found {0} movies".format(len(data)))
                
        return data



    def processWikiFilmYearlyData(self, procYear = None, debug=False):
        outdir = self.getDataDir()
        if procYear == None:
            files = findExt(outdir, ext=".p")
        else:
            files = findPatternExt(outdir, pattern=str(procYear), ext=".p")

        from collections import OrderedDict
        movies = OrderedDict()    
        yearlyData = {}

        for ifile in sorted(files):            
            if debug:
                print("Processing {0}".format(ifile))
            year         = getBaseFilename(ifile)
            movies[year] = self.parseWikiFilmYearlyData(ifile, debug=False)
                
                
            yearlyData[year] = sorted(movies[year].items(), key=operator.itemgetter(1), reverse=False)
            print("---->",year," (Top 5/{0} Movies) <----".format(len(yearlyData[year])))
            for item in yearlyData[year][:5]:
                print(item)
            print('\n')


        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} WikiFilm data to {1}".format(len(yearlyData), savename))
        saveFile(savename, yearlyData)