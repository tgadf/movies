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
class rottentomatoes(movieDB):
    def __init__(self, basedir=None):
        self.name = "rottentomatoes"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadRottenTomatoesYearlyData(self, year, outdir, debug=False):
        yname = str(year)
        url="https://www.rottentomatoes.com/top/bestofrt/?year="+yname
        savename = setFile(outdir, "{0}.p".format(year))
        if isFile(savename): return
        if debug:
            print("Downloading/Saving {0}".format(savename))
        getWebData(base=url, savename=savename, useSafari=False)

    def downloadRottenTomatoesTop100Data(self, genre, outdir, debug=False):
        baseurl="https://www.rottentomatoes.com"
        outdir = setDir(self.getDataDir())
        if not isDir(outdir): mkDir(outdir)
        url = "/top/bestofrt/top_100_"+genre+"_movies/"
        url = baseurl+url
        savename = setFile(outdir, genre+".p")
        if isFile(savename): return
        if debug:
            print("Downloading/Saving {0}".format(savename))
        getWebData(base=url, savename=savename, useSafari=False, dtime=10)
        sleep(2)


    def getRottenTomatoesYearlyData(self, startYear = 1980, endYear = 2017, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        for year in years:
            self.downloadRottenTomatoesYearlyData(year, outdir, debug)
        
    def getRottenTomatoesGenreData(self, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        if not isDir(outdir): mkDir(outdir)
        genres = ["action__adventure", "animation", "art_house__international", 
                  "classics", "comedy", "documentary", "drama", "horror", 
                  "kids__family", "musical__performing_arts", "mystery__suspense", 
                  "romance", "science_fiction__fantasy", "special_interest", 
                  "sports__fitness", "television", "western"]

        for genre in genres:
            self.downloadRottenTomatoesTop100Data(genre, outdir, debug)
                

                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################
    def merge(self, a, b, path=None):
        "merges b into a"
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self.merge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass # same leaf value
                else:
                    raise Exception('Conflict at {0}, {1}'.format(a[key], b[key]))
            else:
                a[key] = b[key]
        return a    
    
    def parseRottenTomatoes(self, debug=False):
        outdir = self.getDataDir()
        files  = findExt(outdir, ext=".p")

        movies = {}
        for ifile in files:
            result = self.parseRottenTomatoesFile(ifile, debug=debug)
            for year, yearlyResult in result.items():
                if movies.get(year) is None:
                    movies[year] = yearlyResult
                else:
                    movies[year] = {**movies[year], **yearlyResult}

        yearlyData = {}
        for year in movies.keys():
            yearlyData[year] = sorted(movies[year].items(), key=operator.itemgetter(1), reverse=True)
            print("---->",year," (Top 5/{0} Movies) <----".format(len(yearlyData[year])))
            for item in yearlyData[year][:5]:
                print(item)
            print('\n')

        savename = setFile(self.getResultsDir(), "rottentomatoes.json")
        print("Saving",len(yearlyData),"yearly results to",savename)
        saveFile(savename, yearlyData)

                
                
    def parseRottenTomatoesFile(self, ifile, debug=False):
        movies = {}
        
        if debug:
            print("Parsing {0}".format(ifile))
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
        table = bsdata.find("table", {"class": "table"})
        if table:
            keys = []
            for tr in table.findAll("tr"):
                if len(keys) == 0:
                    for th in tr.findAll("th"):
                        key = th.string
                        if key == None:
                            key = " ".join([x.string for x in th.findAll("span")])
                        keys.append(key)
                        #print key
                else:
                    line = []
                    for i,td in enumerate(tr.findAll("td")):
                        #print i,'\t',td
                        if i == 0 or i == 3:
                            val = td.string
                        if i == 1:
                            for span in td.findAll("span"):
                                if span.string:
                                    val = span.string
                                    break
                        if i == 2:
                            ref  = td.find("a")
                            #link = ref.attrs["href"]
                            val  = ref.string

                        val = val.strip()
                        line.append(val)
                        #print i,'\t',val.strip()

                    movie  = line[2]
                    rating = line[1]
                    rating = rating.replace("%", "")
                    rating = int(rating)
                    retval = re.search("\((\d+)\)",movie)
                    if retval:
                        year  = retval.group()
                        movie = movie.replace(year, "").strip()
                        year  = retval.groups()[0]
                    #retval = search(r'(%d+)', movie)
                    if movies.get(year) == None:
                        movies[year] = {}
                    movies[year][movie] = rating
                    #print year,'\t',rating,'\t',movie
                    
        return movies