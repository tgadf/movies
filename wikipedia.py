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
class wikipedia(movieDB):
    def __init__(self, basedir=None):
        self.name = "wikipedia"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadWikipediaYearlyData(self, year, outdir, debug=False):

        base = "https://en.wikipedia.org/wiki/"
        dmap = {}
        val = str(int(year) - 1927)+"th_Academy_Awards"
        val = val.replace("1th_", "1st_")
        val = val.replace("2th_", "2nd_")
        val = val.replace("3th_", "3rd_")
        val = val.replace("11st_", "11th_")
        val = val.replace("12nd_", "12th_")
        val = val.replace("13rd_", "13th_")
        try:
            url = base+val
        except:
            print("Could not create url for",year)
            return

        savename = setFile(outdir, str(year)+".p")
        if isFile(savename): return
        if debug:
            print("Downloading {0}".format(url))
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(1)


    def getWikipediaYearlyData(self, startYear = 1934, endYear = 2017, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)
        if startYear < 1934:
            raise ValueError("Must start at or after 1934")
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            self.downloadWikipediaYearlyData(year, outdir, debug)
                

                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################  
    def reorderWikipediaOscarData(self, text, title):
        reorders = ["Best Director", "Best Actress", "Best Actor", 
                    "Best Supporting Actor", "Best Supporting Actress"]
        for val in reorders:
            if title.find(val) != -1:
                if isinstance(text, list):
                    if len(text) >= 2:
                        text = [text[1], text[0]]
                        return text
                    elif len(text) == 1:
                        return text
                    else:
                        raise ValueError("Error reordering {0}".format(text))
                    return text
        return text    


    def parseWikipediaOscarDataSpecial(self, ifile, debug = True):
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
                    text = self.reorderWikipediaOscarData(text, title)
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


    def parseWikipediaOscarData(self, ifile, debug = False):
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
            trs = table.findAll("tr")
            if debug:
                print("   Found {0} rows".format(len(trs)))
            for i,tr in enumerate(trs):
                if done:
                    if debug:
                        print("  Breaking...")
                    break
                    
                tds = tr.findAll("td")
                if debug:
                    print("   Found {0} cols".format(len(tds)))

                for j,td in enumerate(tds):
                    div = td.find("div")
                    if div == None:
                        continue
                        raise()
                    ref = div.find("a")
                    title = ref.string
                    data[title] = {}
                    if debug:
                        print("  Found {0}".format(title))
                        
                    if data.get(title):
                        done = True
                        if debug:
                            print("    Already know about {0}".format(title))
                            print("  Breaking...")
                        break
                        
                    results = []
                    ul = td.find("ul")
                    lis = ul.findAll("li")
                    #if debug:
                    #    print("    Found {0} entries".format(len(lis)))

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
                        text = self.reorderWikipediaOscarData(text, title)
                        results.append(text)
                        

                    if debug:
                        print("Summary\n    {0}: {1}".format(title, results))

                        
                    for k,result in enumerate(results):
                        if isinstance(result, list):
                            if len(result) == 1: results[k] = result[0]

                    data[title]["Winner"]   = results[0]
                    data[title]["Nominees"] = results[1:]
                    if debug:
                        print("      Winner  :",data[title]["Winner"])
                        print("      Nominees:",data[title]["Nominees"])
                        print("")
                    
        return data



    def processWikipediaYearlyData(self, procYear = None, debug=False):
        outdir = self.getDataDir()
        if procYear == None:
            files = findExt(outdir, ext=".p")
        else:
            files = findPatternExt(outdir, pattern=str(procYear), ext=".p")

        from collections import OrderedDict
        movies = OrderedDict()    
        for ifile in files:
            
            if debug:
                print("Processing {0}".format(ifile))
            year    = getBaseFilename(ifile)
            #if year == "1985": continue
            htmldata = getFile(ifile)
            bsdata   = getHTML(htmldata)
            results  = self.parseWikipediaOscarData(ifile, debug=False)
            
            if len(results) == 0:
                results = self.parseWikipediaOscarDataSpecial(ifile, debug=debug)
            if len(results) == 0:
                raise ValueError("No results for {0}".format(ifile))
                
            for k,v in results.items():
                print("====>",year,'\t',k)
                print("      Winner  :",results[k]["Winner"])
                if debug:
                    print("      Nominees:",results[k]["Nominees"])
                    print("")

            savename = setFile(self.getResultsDir(), "{0}.json".format(year))
            print("Saving {0} wikipedia oscar data to {1}".format(year, savename))
            saveFile(savename, results)
        #yamldata.saveYaml(savename, movies)   