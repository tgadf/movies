import re
from time import sleep
from collections import OrderedDict, Counter
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findPatternExt, findExt
from strUtils import convertCurrency
from webUtils import getWebData, getHTML
from numpy import repeat
from movieDB import movieDB
from os import getcwd
import operator
from movieRenames import manualRenames



##############################################################################################################################
# Combine Movies
##############################################################################################################################
class combine(movieDB):
    def __init__(self, basedir=None):
        self.name = "combine"
        movieDB.__init__(self, dbdir=self.name)
        
        self.sources           = set()
        self.movieSource       = {}
        self.movieSourceData   = {}
        self.movieSourceMovies = {}
        self.movieSourceYears  = {}
        self.movieSourceVal    = {}
        
        
        self.ordering = ["Oscar", "Rotten Tomatoes", "SAG", "BAFTA", "Rolling Stone", "Razzies", "Canada", "Ultimate Movie Rankings", "Box Office Mojo", "Wiki Film", "Flops"]
    
        self.years = []
        
        self.keepIMAX = False
        
        self.movies = None
        
        
    def getCombinedMovies(self, debug=False):        
        savename = setFile(self.getResultsDir(), "movies.json")
        if not isFile(savename):
            raise ValueErrro("Cannot access {0}".format(savename))
        combinedMovies = getFile(savename)
        if debug:
            print("Found {0} combined movies".format(len(combinedMovies)))
        return combinedMovies
       
    
    def setMovieData(self, key, source, val):
        self.sources.add(key)
        self.movieSource[key]       = source
        self.movieSourceData[key]   = None
        self.movieSourceMovies[key] = None
        self.movieSourceYears[key]  = None
        self.movieSourceVal[key]    = val

    
    def setOscarData(self, source, val=None):
        key = "Oscar"
        self.setMovieData(key, source, val)
       
    def setRazziesData(self, source, val=None):
        key = "Razzies"
        self.setMovieData(key, source, val)
        
    def setBAFTAData(self, source, val=None):
        key = "BAFTA"
        self.setMovieData(key, source, val)
        
    def setSAGData(self, source, val=None):
        key = "SAG"
        self.setMovieData(key, source, val)
        
    def setFlopsData(self, source, val=None):
        key = "Flops"
        self.setMovieData(key, source, val)
        
    def setCanadaData(self, source, val=None):
        key = "Canada"
        self.setMovieData(key, source, val)
        
    def setRollingStoneData(self, source, val=None):
        key = "Rolling Stone"
        self.setMovieData(key, source, val)
       
    def setWikiFilmData(self, source, val=None):
        key = "Wiki Film"
        self.setMovieData(key, source, val)
       
    def setUltimateMovieRankingsData(self, source, val=None):
        key = "Ultimate Movie Rankings"
        self.setMovieData(key, source, val)
       
    def setRottenTomatoesData(self, source, val=None):
        key = "Rotten Tomatoes"
        self.setMovieData(key, source, val)
       
    def setBoxOfficeMojoData(self, source, val=None):
        key = "Box Office Mojo"
        self.setMovieData(key, source, val)
        
        
    
    
    def getData(self):
        years = []
        for key in self.sources:
            resultsDir  = self.movieSource[key].getResultsDir()
            resultsName = self.movieSource[key].name
            filename = setFile(resultsDir, "{0}.json".format(resultsName))
            if isFile(filename):
                self.movieSourceData[key]  = getFile(filename)
                self.movieSourceYears[key] = list(self.movieSourceData[key].keys())
                print("Found {0} Years of {1} Movies".format(len(self.movieSourceYears[key]), key))
                years = years + self.movieSourceYears[key]
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
        
        self.years = sorted(list(set(years)))
        print("Found Data Between {0} and {1}".format(min(self.years), max(self.years)))


    
    def getYearlyMovies(self, data, year, name, minval, debug=False):
        movies = []
        if data.get(year) is not None:
            if minval is not None:
                movies = [x[0] for x in data[year] if x[1] >= minval]
            else:
                movies = [x[0] for x in data[year]]
                
            if debug:
                print("  {0}  {1: <20}: {2}/{3}".format(year, name, len(movies), len(data[year])))
        else:
            if debug:
                print("  {0}  {1: <20}: None".format(year, name))
        return movies
        
        
    def saveCorrections(self, debug=True):
        corrsavename = setFile(self.getDataDir(), "corr.yaml")
        corrData = getFile(corrsavename)        

        try:
            savename = setFile(self.getDataDir(), "saved.yaml")
            savedData = getFile(savename)
        except:
            raise ValueError("Could not access saved data!")
            savedData = {}

        if corrData is None:
            print("There is no corrections data.")
        else:
            print("Found {0} old corrections".format(len(savedData)))
            print("Found {0} new corrections".format(len(corrData)))
            for movie,corrs in corrData.items():
                if savedData.get(movie) is None:
                    if debug:
                        print("Adding {0}".format(movie))
                    savedData[movie] = corrs
                else:
                    newSaved = list(set(savedData[movie] + corrs))
                    if len(newSaved) != len(savedData[movie]):
                        print("Adding new corrections to {0}".format(movie))
                    savedData[movie] = newSaved

            try:
                savename = setFile(self.getDataDir(), "saved.yaml")
                saveFile(idata=savedData, ifile=savename, debug=debug)        
                print("There are {0} total corrections".format(len(savedData)))
            except:
                raise ValueError("There was an error saving the saved corrctions yaml file!")
        #else:
        #    print("Could not process corrected yaml file: {0}".format(corrsavename))
        
            
    def mergeMovies(self, debug=False):
        verydebug=False
        yearlyMovies = OrderedDict()
        movies = OrderedDict()
        nameCntr = Counter()
        
        repData   = {}
        savename  = setFile(self.getDataDir(), "saved.yaml")
        savedData = getFile(savename)
        for corrMovie,corrs in savedData.items():
            for corr in corrs:
                repData[corr] = corrMovie
                       
        keys = OrderedDict()
        for key in self.ordering:
            keys[key] = [self.movieSourceData[key], self.movieSourceVal[key]]
            
        
        for year in self.years:
            keyMovies = {}
            for key in self.ordering:
                keydata = keys[key]
                keyfunc = keydata[0]
                keyVal  = keydata[1]
                keyMovies[key] = self.getYearlyMovies(keyfunc, year, key, keyVal, debug=verydebug)
                keyMovies[key] = [manualRenames(x, int(year), self.keepIMAX) for x in keyMovies[key]]
                keyMovies[key] = dict(zip(keyMovies[key], repeat(key, len(keyMovies[key]))))
                #print(key,year,len(keyMovies[key]))
            

                ###### Merge The Movies
                for movie,name in keyMovies[key].items():
                    if repData.get(movie):
                        movie = repData[movie]
                    moviename = "{0} [{1}]".format(movie, year)
                    if movies.get(moviename) is None:
                        movies[moviename] = name
                        nameCntr[name] += 1

                   
       

        if debug:
            print("Found {0} movies".format(len(movies)))
            for item in nameCntr.most_common():
                print("\t",item)



        ### Start with Oscar Movies (remove from other categories)
        
        removes = []
        for key,name in movies.items():
            #print(key)
            movie = key[:-7]
            year  = key[-5:-1]
            
            #if movie.find("*") != -1: print(key,name)
            
            
            for dy in [1, -1, 2, -2]:
                test   = "{0} [{1}]".format(movie, int(year)+dy)
                result = movies.get(test)
                if result is not None:
                    #print("   <---- {0}".format(test))
                    if self.ordering.index(result) > self.ordering.index(name):
                        if verydebug:
                            print("Removing {0}: {1} because it is already listed as {2}: {3}".format(test,result,key,name))
                        removes.append(test)

        for key in removes:
            try:
                del movies[key]
            except:
                print("Could not remove {0}".format(key))
                
        if debug:
            print("There are {0} final movies".format(len(movies)))
            
        self.movies = movies
        
        savename = setFile(self.getResultsDir(), "movies.json")
        saveFile(idata=movies, ifile=savename, debug=True)