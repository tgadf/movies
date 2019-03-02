import re
from time import sleep
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findPatternExt, findExt, findNearest
from strUtils import convertCurrency
from webUtils import getWebData, getHTML
from movieDB import movieDB
from os import getcwd
import operator


##############################################################################################################################
# Filmsite
##############################################################################################################################
class filmsite(movieDB):
    def __init__(self, basedir=None):
        self.name = "filmsite"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadFilmsiteYearlyData(self, year, outdir, debug=False):
        url="https://www.filmsite.org/{0}.html".format(year)
        savename = setFile(outdir, "{0}.p".format(year))
        if isFile(savename): return
        
        try:
            if debug:
                print("Downloading/Saving {0}".format(savename))
            getWebData(base=url, savename=savename, useSafari=False)
        except:
            return
        sleep(2)


    def getFilmsiteYearlyData(self, startYear = 1902, endYear = 2018, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        #outdir = setDir(getBoxOfficeDir(), "data")
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            self.downloadFilmsiteYearlyData(year, outdir, debug)
                
                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################
    def parseFilmsiteYearlyData(self, ifile, debug=False):
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
        
        movies = []
        
        tables = bsdata.findAll("table")
        tables = tables[1:]
        for table in tables:
            trs = table.findAll("tr")
            trs = trs[1:]
            for tr in trs:
                tds = tr.findAll("td")
                if len(tds) == 2:
                    mdata = tds[1].find("b")
                    if mdata is not None:
                        movie = mdata.text
                        movie = "".join([c for c in movie if ord(c) not in [10,13]])
                        while movie.find("  ") != -1:
                            movie = movie.replace("  ", " ")
                        pos = movie.rfind("(")
                        if pos != -1:
                            movie = movie[:pos].strip()
                        movies.append(movie)
        
        return movies
                    


    def parseFilmsiteData(self, debug=False):
        outdir = self.getDataDir()
        resultsdir = self.getResultsDir()
        files  = findExt(outdir, ext=".p")
        movies = {}
        
        for ifile in sorted(files):
            year    = getBaseFilename(ifile)
            results = self.parseFilmsiteYearlyData(ifile, debug=debug)
            movies[year] = []
            for movie in results:
                movies[year].append([movie,10])
                
            print("Found {0} movies in {1}".format(len(movies[year]),year))
        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of Filmsite Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)