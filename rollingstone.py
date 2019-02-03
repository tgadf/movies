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
class rollingstone(movieDB):
    def __init__(self, basedir=None):
        self.name = "rollingstone"
        movieDB.__init__(self, dbdir=self.name)
                

                
    
    
    ###########################################################################################################################
    # Parse Rolling Stone Weekend Files
    ###########################################################################################################################  
    def processRollingStoneData(self, debug=False):
        outdir = self.getDataDir()
        files = findExt(outdir, ext=".html")

        from collections import OrderedDict
        movies = OrderedDict()
        yearlyData = {}
        for ifile in files:            
            htmldata = getFile(ifile)
            bsdata   = getHTML(htmldata)
            
            h3s = bsdata.findAll("h3", {"class": "c-list__title t-bold"})
            h3s = [x.text for x in h3s]
            h3s = [x.replace("\n", "").strip() for x in h3s]
            for h3 in h3s:
                try:
                    year  = int(h3[-5:-1])
                except:
                    raise ValueError("Could not get year from {0}".format(h3))
                    
                movie = h3[1:-8]
                print(year,'\t',movie)
                
                if yearlyData.get(year) is None:
                    yearlyData[year] = []
                yearlyData[year].append(movie)
                
        for year in sorted(yearlyData.keys()):
            movies[year] = []
            for movie in yearlyData[year]:
                movies[year].append([movie, 10])

        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of rollingstone Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)
        #yamldata.saveYaml(savename, movies)   