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
class flops(movieDB):
    def __init__(self, basedir=None):
        self.name = "flops"
        movieDB.__init__(self, dbdir=self.name)
                

                
    
    
    ###########################################################################################################################
    # Parse Rolling Stone Weekend Files
    ###########################################################################################################################  
    def processFlopsData(self, debug=False):
        outdir = self.getDataDir()
        files = findExt(outdir, ext=".html")

        from collections import OrderedDict
        movies = OrderedDict()
        yearlyData = {}
        for ifile in files:            
            htmldata = getFile(ifile)
            bsdata   = getHTML(htmldata)
            
            tables = bsdata.findAll("table", {"class": "wikitable"})
            for table in tables:
                
                trs = table.findAll("tr")

                try:
                    ths = trs[0].findAll("th")
                    ths = [x.text for x in ths]
                    ths = [x.replace("\n", "") for x in ths]
                except:
                    raise ValueError("Could not get headers")

                print(ths)
                    
                for itr,tr in enumerate(trs[2:]):
                    
                    ths = tr.findAll("th")
                    try:
                        movie = ths[0].text
                        movie = movie.replace("\n", "").strip()
                        movie = movie.replace("[nb 2]", "")
                    except:
                        raise ValueError("Could not find movie in {0}".format(ths))
                        
                    
                    tds = tr.findAll("td")
                    try:
                        year = tds[0].text
                        year = int(year)
                    except:
                        raise ValueError("Could not find year in {0}".format(tds))
                        
                    print(year,'\t',movie)
                
                    if yearlyData.get(year) is None:
                        yearlyData[year] = []
                    yearlyData[year].append(movie)
                
        for year in sorted(yearlyData.keys()):
            movies[year] = []
            for movie in yearlyData[year]:
                movies[year].append([movie, 10])

        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of flops Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)
        #yamldata.saveYaml(savename, movies)   