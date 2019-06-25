import re
from time import sleep
from collections import OrderedDict
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile, moveFile
from fileUtils import getBaseFilename, getDirname, getFileBasics
from searchUtils import findSubPatternExt, findPatternExt, findExt, findNearest
from strUtils import convertCurrency
from webUtils import getWebData, getHTML
from numpy import repeat
from movieDB import movieDB
from os import getcwd
from os.path import join
from glob import glob
import operator
from movieRenames import manualRenames

##############################################################################################################################
# Combine Movies
##############################################################################################################################
class mymovies(movieDB):
    def __init__(self, basedir=None):
        self.name = "mymovies"
        movieDB.__init__(self, dbdir=self.name)
        self.combine       = None
        self.missingMovies = None
        self.status        = None
        self.renames       = None
        
    def setCombinedMovies(self, combine):
        self.combine = combine
        
    def getCombinedMovies(self, debug=False):        
        savename = setFile(self.combine.getResultsDir(), "movies.json")
        if not isFile(savename):
            raise ValueErrro("Cannot access {0}".format(savename))
        combinedMovies = getFile(savename)
        if debug:
            print("Found {0} combined movies".format(len(combinedMovies)))
        return combinedMovies
        
    def getCombinedMoviesByYear(self, debug=False): 
        combmovies = self.getCombinedMovies()
        moviesByYear = {}
        for movie in combmovies.keys():
            name = movie[:-7]
            try:
                year = int(movie[-5:-1])
            except:
                raise ValueError("Error with {0} --> {1}".format(movie, combmovies[movie]))
            if moviesByYear.get(year) is None:
                moviesByYear[year] = {}
            if moviesByYear[year].get(name) is not None:
                raise ValueError("You have a duplicate movie for {0}!".format(movie))
            moviesByYear[year][name] = combmovies[movie]
            
        moviesByYear = self.removeDuplicates(moviesByYear)
        return moviesByYear

    def removeDuplicates(self, combinedMovies):
        cmovies  = combinedMovies
        ordering = self.combine.getOrdering()
        years    = cmovies.keys()

        drops  = {}
        iDrops = 0
        while len(drops) > 0 or iDrops == 0:
            #print("Iteration: {0}".format(iDrops))
            if iDrops > 0:
                drops = {}

            for year in years:
                movies = cmovies[year]

                for name,source in movies.items():
                    key = " :: ".join([str(year),name,source])

                    if len(name.strip()) == 0:
                        if drops.get(key) is None:
                            drops[key] = []
                        drops[key].append(key)
                        continue

                    if name.endswith(" 3D"):
                        if drops.get(key) is None:
                            drops[key] = []
                        drops[key].append(key)
                        continue

                    key = " :: ".join([str(year),name,source])
                    for yearval in [year-x for x in [-2,-1,1,2]]:
                        if cmovies.get(yearval) is not None:
                            if cmovies[yearval].get(name) is not None:
                                foundsource = cmovies[yearval][name]
                                fKey = " :: ".join([str(yearval),name,foundsource])


                                #print(year,'\t',name,'\tFound from {0} in {1} from {2}'.format(source,yearval,foundsource), end="\t\t")

                                iSource  = ordering.index(source)
                                ifSource = ordering.index(foundsource)                    

                                if iSource == ifSource:
                                    if yearval > year:
                                        #print("\t====> Keeping",end="")
                                        if drops.get(key) is None:
                                            drops[key] = []
                                        drops[key].append(fKey)



                                if iSource < ifSource:
                                    #print("\t====> Keeping",end="")
                                    if drops.get(key) is None:
                                        drops[key] = []
                                    drops[key].append(fKey)

                                #print("")

            for key,drop in drops.items():
                for fKey in drop:
                    year,name,source = fKey.split(" :: ")
                    try:
                        del cmovies[int(year)][name]
                    except:
                        pass
                        #print("Could not delete {0}/{1}".format(year,name))

            iDrops += 1

        return cmovies

    
    def printMissingMoviesByYear(self, year, movies):
        print("")
        for movie in sorted(movies):
            print("{0: <10}{1: <100}".format(year, movie))


    def printMissingMovies(self, year=None):
        missingMovies = self.getMissingMovies()
        print("====================== Missing Movies ======================")
        print("{0: <10}{1: <100}".format("Year", "Movie"))
        print("{0: <10}{1: <100}".format("----", "-----"))

        if year is None:
            for year in missingMovies.keys():
                self.printMissingMoviesByYear(missingMovies[year])
        else:        
            self.printMissingMoviesByYear(year, missingMovies[year])    


    
    def setMissingMovies(self, missing):
        self.missingMovies = missing
        
    def getMissingMovies(self):
        return self.missingMovies

    
    def setCombinedMovieStatus(self, status):
        self.status = status
        
    def getCombinedMovieStatus(self):
        return self.status

    
    def setMovieRenames(self, renames):
        self.renames = renames
        
    def getMovieRenames(self):
        return self.renames
        
        
    def getMyMovies(self, debug=False): 
        savename = setFile(self.getDataDir(), "mymovies.json")
        if not isFile(savename):
            raise ValueError("Cannot access {0}".format(savename))
        mine = getFile(savename)
        if debug:
            print("Found {0} my movies".format(len(mine)))
        return mine
        
        
    def getMyMoviesByYear(self, debug=False): 
        mymovies = self.getMyMovies()
        moviesByYear = {}
        for movie in mymovies.keys():
            name = movie[:-7]
            try:
                year = int(movie[-5:-1])
            except:
                raise ValueError("Error with {0} --> {1}".format(movie, mymovies[movie]))
            if moviesByYear.get(year) is None:
                moviesByYear[year] = {}
            if moviesByYear[year].get(name) is not None:
                raise ValueError("You have a duplicate movie for {0}!".format(movie))
            moviesByYear[year][name] = mymovies[movie]
            
        return moviesByYear
            
            
    def findMyMovies(self, debug=False):
        movies = glob("/Volumes/*/Movies/*.*")
        mine   = dict(zip([getBaseFilename(x) for x in movies], movies))
        print("Found {0} movies on my disks".format(len(movies)))
        savename = setFile(self.getDataDir(), "mymovies.json")
        saveFile(idata=mine, ifile=savename, debug=True)
        
        
    def searchMyMovies(self, movie, year, cutoff=0.8, num=3):
        moviesMine = self.getMyMovies()
        key = "{0} [{1}]".format(movie, year)
        result     = findNearest(key, moviesMine.keys(), num, 0.95)
        if len(result) > 0:
            print("{0}  --->  {1}".format(movie, result))
            location = moviesMine[result[0]]
            print("moveFile(src=\"{0}\", dst=\"{1}\", debug=True)\n".format(location, location))
            return
        else:
            key = "{0} [{1}]".format(movie, year)
            result = findNearest(key, moviesMine.keys(), num, cutoff)
            if len(result) > 0:
                print("{0}  --->  {1}".format(movie, result))
                location = moviesMine[result[0]]
                print("moveFile(src=\"{0}\", dst=\"{1}\", debug=True)\n".format(location, location))
                return
        print("No match found")
        return
    
    
    def suggestRenames(self):

        movies = glob("/Volumes/Download/MoviesFinished/*.*")
        for movie in movies:
            fileInfo = getFileBasics(movie)
            name = fileInfo[1]
                        
            ps=["1080", "720", "480"]
            for p in ps:
                name = name.replace("{0}p".format(p), "")

            xs=['264']
            for x in xs:
                name = name.replace("x{0}".format(x), "")
            
            ts=["BluRay", "BRrip", "WEBRip", "HDTVRip", "GAZ", "BrRip"]
            for t in ts:
                name = name.replace("{0}".format(t), "")
                
            vs=["-[YTS.AG]", "-[YTS.AM]", "YIFY", "[YTS.AG]"]
            for v in vs:
                name = name.replace("{0}".format(v), "")
                
            vs=["of", "and", "the", "a"]
            for v in vs:
                name = name.replace(" {0} ".format(v), " {0} ".format(v.title()))
                
            name = name.replace(".", " ")
            name=name.strip()

            dst = join(fileInfo[0], "".join([name, fileInfo[2]]))
            if name != fileInfo[1]:
                moveFile(src=movie, dst=dst, debug=True)


        movies = glob("/Volumes/Download/MoviesFinished/*.*")   
        for movie in movies:
            fileInfo = getFileBasics(movie)            
            name  = fileInfo[1][:-4].strip()
            year  = fileInfo[1][-4:]
            
            try:
                int(year)
                name = "{0} [{1}]".format(name, year)
            except:
                print("Cannot rename {0}".format(movie))
                continue
            
            src = movie
            dst = join(fileInfo[0], "".join([name, fileInfo[2]]))
            moveFile(src=src, dst=dst, debug=True)
            print("")
            
            
    
    def showCombinedMovieStatus(self, year=None):
        locations = self.getCombinedMovieStatus()
        years = sorted(locations.keys())
        if year is not None:
            years = [year]

        print("{0: <6}{1: <3}{2: <100}{3: <20}".format("Year", u'\u2713', "Movie", "Source"))


        for year in years:
            print('\n',129*'-')
            for name,sourcedata in locations[year].items():
                location = sourcedata[0]
                source   = sourcedata[1]
                print("{0: <6}{1: <3}{2: <100}{3: <20}".format(year, location, name, source))

        
        
    def mergeMovies(self, toFile=False, movie=None, source=None, year=None):
        combinedMovies = self.getCombinedMoviesByYear()
        
        myMovies       = self.getMyMoviesByYear()
        renames        = {}
        filename = setFile(self.getResultsDir(), "mymovies.dat")
        
        
        yearcut = year
        sourcecut = source
        moviecut = movie

        pYear = None
        yearRenames = {}
        
        locations = {}
        toGet = {}
        

        years = sorted(combinedMovies.keys())
        for year in years:
            locations[year] = {}
            movies = combinedMovies[year]
            #print("Analyzing {0} movies from {1}".format(len(movies), year))

            for name,source in movies.items():
                key = "{0} [{1}]".format(name, year)
                locations[year][name] = [None, source]
                
                for yearval in [year+y for y in [0,1,-1,2,-2]]:
                    try:
                        location = myMovies[yearval][name]
                        break
                    except:
                        location = None

                exact    = False
                if location is not None:
                    location = u'\u2713'
                    exact    = True
                else:
                    nearbyMovies = []
                    for yearval in [year+y for y in [0,1,-1]]:
                        yearlyMovies = myMovies.get(yearval)                        
                        if isinstance(yearlyMovies, dict):
                            result = findNearest(name, yearlyMovies.keys(), 1, 0.98)
                            if len(result) > 0:
                                location = u'\u2248'
                                
                                myMovie = myMovies[yearval][result[0]]
                                fileInfo = getFileBasics(myMovie)
                                newMovieKey = "{0} [{1}]".format(name, year)
                                yearRenames[myMovie] = join(fileInfo[0], "".join([newMovieKey, fileInfo[2]]))

                    if location is None:
                        for yearval in [year+y for y in [0,1,-1]]:
                            yearlyMovies = myMovies.get(yearval)
                            if isinstance(yearlyMovies, dict):
                                result = findNearest(name, yearlyMovies.keys(), 1, 0.90)
                                if len(result) > 0:
                                    location = u'\u2047'

                                    myMovie = myMovies[yearval][result[0]]
                                    fileInfo = getFileBasics(myMovie)
                                    newMovieKey = "{0} [{1}]".format(name, year)
                                    yearRenames[myMovie] = join(fileInfo[0], "".join([newMovieKey, fileInfo[2]]))

                    if location is None:
                        location = ""
                        
                    if exact is False:
                        if toGet.get(year) is None:
                            toGet[year] = {}
                        toGet[year][name] = source
                
                locations[year][name][0] = location
         
        
        self.setCombinedMovieStatus(locations)
        self.setMissingMovies(toGet)
        self.setMovieRenames(yearRenames)