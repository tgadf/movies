import re
from time import sleep
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findPatternExt, findExt, findNearest
from strUtils import convertCurrency
from webUtils import getWebData, getHTML, removeTag
from movieDB import movieDB
from os import getcwd
import operator


##############################################################################################################################
# Box Office Mojo
##############################################################################################################################
class ultimatemovierankings(movieDB):
    def __init__(self, basedir=None):
        self.name = "ultimatemovierankings"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadUltimateMovieRankingsYearlyData(self, year, outdir, debug=False):
        yname = str(year)

        url="https://www.ultimatemovierankings.com/{0}-top-box-office-movies/".format(year)
        url="https://www.ultimatemovierankings.com/top-grossing-movies-of-{0}/".format(year)
        url="https://www.ultimatemovierankings.com/{0}-movies/".format(year)
        url="https://www.ultimatemovierankings.com/{0}-top-grossing-movies/".format(year)
        url="https://www.ultimatemovierankings.com/biggest-box-office-hits-of-{0}/".format(year)
        url="https://www.ultimatemovierankings.com/top-grossing-{0}-movies/".format(year)
        url="https://www.ultimatemovierankings.com/ranking-{0}-movies/".format(year)
        url="https://www.ultimatemovierankings.com/best-worst-movies-{0}/".format(year)
        
        savename = setFile(outdir, yname+".p")
        if isFile(savename): return
        if debug:
            print("Downloading/Saving {0}".format(savename))
        try:
            getWebData(base=url, savename=savename, useSafari=False)
            sleep(2)
        except:
            sleep(0.2)


    def getUltimateMovieRankingsYearlyData(self, startYear = 2017, endYear = 2017, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        #outdir = setDir(getBoxOfficeDir(), "data")
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            if year >= 1988 and year <= 2010:
                continue
            self.downloadUltimateMovieRankingsYearlyData(year, outdir, debug)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def parseUltimateMovieRankingsYearlyData(self, procYear = None, debug = False):
        outdir = self.getDataDir()
        if procYear == None:
            files = findExt(outdir, ext=".p")
        else:
            files = findPatternExt(outdir, pattern=str(procYear), ext=".p")

        from collections import OrderedDict
        movieData = OrderedDict()
        for ifile in sorted(files):
            #ifile = "/Users/tgadfort/Documents/code/movies/ultimatemovierankings/data/2017.p"
            htmldata = getFile(ifile)
            bsdata   = getHTML(htmldata)
            year     = getBaseFilename(ifile)

            data   = {}
            done   = False
            tables = bsdata.findAll("table") #, {"id": "table_3"})
            movies = {}
            for it,table in enumerate(tables):
                ths = table.findAll("th")
                trs = table.findAll("tr")
                for itr,tr in enumerate(trs):
                    tds = tr.findAll("td")
                    if len(tds) == 11:
                        val  = removeTag(tds[1], 'span')
                        film = val.text
                        film = film.replace(" ({0})".format(year), "")
                        try:
                            rank = float(tds[-1].text)
                        except:
                            try:
                                rank = float(tds[-2].text)
                            except:
                                raise ValueError(tds[-1],tds[-2],tr)

                        movies[film] = rank

            movieData[year] = movies



        yearlyData = {}
        for year in sorted(movieData.keys()):
            yearlyData[year] = sorted(movieData[year].items(), key=operator.itemgetter(1), reverse=True)
            print("---->",year," (Top 5/{0} Movies) <----".format(len(yearlyData[year])))
            for item in yearlyData[year][:5]:
                print(item)
            print('\n')

        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving {0} Years of Ultimate Movie Rankings data to {1}".format(len(yearlyData), savename))
        saveFile(savename, yearlyData)