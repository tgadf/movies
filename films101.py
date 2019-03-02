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
# films101
##############################################################################################################################
class films101(movieDB):
    def __init__(self, basedir=None):
        self.name = "films101"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadFilms101YearlyData(self, year, outdir, debug=False):
        url="http://www.films101.com/y{0}r.htm".format(year)
        savename = setFile(outdir, "{0}.p".format(year))
        if isFile(savename): return
        
        try:
            if debug:
                print("Downloading/Saving {0}".format(savename))
            getWebData(base=url, savename=savename, useSafari=False)
        except:
            return
        sleep(2)


    def getFilms101YearlyData(self, startYear = 1900, endYear = 2018, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        #outdir = setDir(getBoxOfficeDir(), "data")
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            self.downloadFilms101YearlyData(year, outdir, debug)
                
                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################
    def parseFilms101YearlyData(self, ifile, debug=False):
        if debug:
            print(ifile)
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
        
        movies = []
        
        headertables = bsdata.findAll("table", {"class": "lsthdg"})
        datatables   = bsdata.findAll("table", {"class": "lstdta"})
        if len(headertables) < len(datatables):
            print(headertables)
            raise ValueError("Found {0} headers and {1} data tables".format(len(headertables), len(datatables)))
            
        if debug:
            print("Found {0} tables".format(len(datatables)))
        for i in range(len(datatables)):
            headertable = headertables[i]
            tds         = headertable.findAll("td")
            headers     = [x.text for x in tds if x is not None]
            headers     = [x.strip() for x in headers]

            datatable   = datatables[i]
            trs         = datatable.findAll("tr")
            expect = len(trs)
            for tr in trs:
                tds = tr.findAll("td")
                tds = [x.text for x in tds if x is not None]
                if len(tds) != len(headers):
                    print(headers)
                    print(tds)
                    1/0

                try:
                    mdata = dict(zip(headers, tds))
                except:
                    print(headers)
                    print(tds)
                    raise ValueError("Could not combine headers and data")

                try:
                    movie = mdata['TITLE']
                except:
                    raise ValueError("Could not get movie name from TITLE key! {0}".format(mdata))

                movies.append(movie)
            
        if debug:
            print("Found {0}/{1} movies".format(len(movies), expect))
            
        return movies
                    


    def parseFilms101Data(self, debug=False):
        outdir = self.getDataDir()
        resultsdir = self.getResultsDir()
        files  = findExt(outdir, ext=".p")
        movies = {}
        
        for ifile in sorted(files):
            year    = getBaseFilename(ifile)
            results = self.parseFilms101YearlyData(ifile, debug=debug)
            movies[year] = []
            for movie in results:
                movies[year].append([movie,10])
            print("Found {0} movies in {1}".format(len(movies[year]),year))
        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of films101 Data to {1}".format(len(movies), savename))
        saveFile(savename, movies)
_, _ = clock("Last Run")