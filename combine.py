import re
from time import sleep
from collections import OrderedDict
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
        
        self.boxofficemojo       = None
        self.boxofficemojoData   = None
        self.boxofficemojoMovies = None
        
        self.oscar       = None
        self.oscarData   = None
        self.oscarMovies = None
        
        self.wikifilm       = None
        self.wikifilmData   = None
        self.wikifilmMovies = None

        self.rottentomatoes       = None
        self.rottentomatoesData   = None
        self.rottentomatoesMovies = None

        self.ultimatemovierankings       = None
        self.ultimatemovierankingsData   = None
        self.ultimatemovierankingsMovies = None
    
        self.years = []
        
        self.keepIMAX = False
        
        self.movies = None
       
    
    def setOscarData(self, oscar):
        self.oscar       = oscar
        self.oscarData   = None
        self.oscarMovies = None
       
    
    def setWikiFilmData(self, wikifilm):
        self.wikifilm       = wikifilm
        self.wikifilmData   = None
        self.wikifilmMovies = None
       
    
    def setUltimateMovieRankingsData(self, ultimatemovierankings):
        self.ultimatemovierankings       = ultimatemovierankings
        self.ultimatemovierankingsData   = None
        self.ultimatemovierankingsMovies = None
       
    
    def setRottenTomatoesData(self, rottentomatoes):
        self.rottentomatoes       = rottentomatoes
        self.rottentomatoesData   = None
        self.rottentomatoesMovies = None
       
    
    def setBoxOfficeMojoData(self, boxofficemojo):
        self.boxofficemojo       = boxofficemojo
        self.boxofficemojoData   = None
        self.boxofficemojoMovies = None
        
        
    
    
    def getData(self):
        if self.boxofficemojo is not None:
            filename = setFile(self.boxofficemojo.getResultsDir(), "boxofficemojo.json")
            if isFile(filename):
                self.boxofficemojoData = getFile(filename)
                boxofficemojoYears = list(self.boxofficemojoData.keys())
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
        if self.ultimatemovierankings is not None:
            filename = setFile(self.ultimatemovierankings.getResultsDir(), "ultimatemovierankings.json")
            if isFile(filename):
                self.ultimatemovierankingsData = getFile(filename)
                ultimatemovierankingsYears = list(self.ultimatemovierankingsData.keys())
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
        if self.oscar is not None:
            filename = setFile(self.oscar.getResultsDir(), "oscars.json")
            if isFile(filename):
                self.oscarData = getFile(filename)
                oscarYears = list(self.oscarData.keys())
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
        if self.wikifilm is not None:
            filename = setFile(self.wikifilm.getResultsDir(), "wikifilm.json")
            if isFile(filename):
                self.wikifilmData = getFile(filename)
                wikifilmYears = list(self.wikifilmData.keys())
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
        if self.rottentomatoes is not None:
            filename = setFile(self.rottentomatoes.getResultsDir(), "rottentomatoes.json")            
            if isFile(filename):
                self.rottentomatoesData = getFile(filename)
                rottentomatoesYears = list(self.rottentomatoesData.keys())
            else:
                raise ValueError("There is not results file: {0}".format(filename))
                
                
        if self.boxofficemojoData is not None:
            print("Found {0} Years of BoxOfficeMojo Data".format(len(self.boxofficemojoData)))
        else:
            print("Could not find BoxOfficeMojo Data")

        if self.oscarData is not None:
            print("Found {0} Years of Oscar Data".format(len(self.oscarData)))
        else:
            print("Could not find Oscar Data")

        if self.wikifilmData is not None:
            print("Found {0} Years of Wiki Film Data".format(len(self.wikifilmData)))
        else:
            print("Could not find Wiki Film Data")

        if self.ultimatemovierankingsData is not None:
            print("Found {0} Years of Ultimate Movie Rankings Data".format(len(self.ultimatemovierankingsData)))
        else:
            print("Could not find Ultimate Movie Rankings Data")

        if self.rottentomatoesData is not None:
            print("Found {0} Years of RottenTomatoes Data".format(len(self.rottentomatoesData)))
        else:
            print("Could not find RottenTomatoes Data")

        years = sorted(list(set(oscarYears + boxofficemojoYears + rottentomatoesYears + ultimatemovierankingsYears)))
        print("Found Data Between {0} and {1}".format(min(years), max(years)))
        self.years = years


    
    def getYearlyMovies(self, data, year, name, minval, debug=False):
        movies = []
        if data.get(year) is not None:
            movies = [x[0] for x in data[year] if x[1] >= minval]
            if debug:
                print("  {0}  {1: <20}: {2}/{3}".format(year, name, len(movies), len(data[year])))
        else:
            if debug:
                print("  {0}  {1: <20}: None".format(year, name))
        return movies
        
        
            
    def mergeMovies(self, oscarVal, boxofficeVal, rottentomatoesVal, ultimatemovierankingsVal, wikifilmVal, debug=False):
        verydebug=False
        yearlyMovies = OrderedDict()
        movies = OrderedDict()
        for year in self.years:        

            key = "Oscar"
            oscarMovies = self.getYearlyMovies(self.oscarData, year, key, oscarVal, debug=verydebug)
            oscarMovies = [manualRenames(x, int(year), self.keepIMAX) for x in oscarMovies]
            oscarMovies = dict(zip(oscarMovies, repeat(key, len(oscarMovies))))
            
            key = "Box Office"
            boxofficeMovies = self.getYearlyMovies(self.boxofficemojoData, year, key, boxofficeVal, debug=verydebug)
            boxofficeMovies = [manualRenames(x, int(year), self.keepIMAX) for x in boxofficeMovies]
            boxofficeMovies = dict(zip(boxofficeMovies, repeat(key, len(boxofficeMovies))))
            
            key = "Wiki Film"
            wikifilmMovies = self.getYearlyMovies(self.wikifilmData, year, key, wikifilmVal, debug=verydebug)
            wikifilmMovies = [manualRenames(x, int(year), self.keepIMAX) for x in wikifilmMovies]
            wikifilmMovies = dict(zip(wikifilmMovies, repeat(key, len(wikifilmMovies))))

            key = "Rotten Tomatoes"
            rottentomatoesMovies = self.getYearlyMovies(self.rottentomatoesData, year, key, rottentomatoesVal, debug=verydebug)
            rottentomatoesMovies = [manualRenames(x, int(year), self.keepIMAX) for x in rottentomatoesMovies]
            rottentomatoesMovies = dict(zip(rottentomatoesMovies, repeat(key, len(rottentomatoesMovies))))       

            key = "Ultimate Movie Rankings"
            umrMovies = self.getYearlyMovies(self.ultimatemovierankingsData, year, key, ultimatemovierankingsVal, debug=verydebug)
            umrMovies = [manualRenames(x, int(year), self.keepIMAX) for x in umrMovies]
            umrMovies = dict(zip(umrMovies, repeat(key, len(umrMovies))))

            
            ###
            for movie,name in oscarMovies.items():
                key = "{0} [{1}]".format(movie, year)
                movies[key] = name
            for movie,name in rottentomatoesMovies.items():
                key = "{0} [{1}]".format(movie, year)
                if movies.get(key) is None:
                    movies[key] = name
            for movie,name in umrMovies.items():
                key = "{0} [{1}]".format(movie, year)
                if movies.get(key) is None:
                    movies[key] = name
            for movie,name in boxofficeMovies.items():
                key = "{0} [{1}]".format(movie, year)
                if movies.get(key) is None:
                    movies[key] = name
            for movie,name in wikifilmMovies.items():
                key = "{0} [{1}]".format(movie, year)
                if movies.get(key) is None:
                    movies[key] = name


        if debug:
            print("Found {0} movies".format(len(movies)))

        ### Start with Oscar Movies (remove from other categories)
        
        removes = []
        ordering = ["Oscar", "Rotten Tomatoes", "Ultimate Movie Rankings", "Box Office", "Wiki Film"]
        for key,name in movies.items():
            #print(key)
            movie = key[:-7]
            year  = key[-5:-1]
            
            for dy in [1, -1, 2, -2]:
                test   = "{0} [{1}]".format(movie, int(year)+dy)
                result = movies.get(test)
                if result is not None:
                    #print("   <---- {0}".format(test))
                    if ordering.index(result) > ordering.index(name):
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
        
        savename = setFile(self.getResultsDir(), "movies.yaml")
        saveFile(idata=movies, ifile=savename, debug=True)

