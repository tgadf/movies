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
# Oscar
##############################################################################################################################
class oscars(movieDB):
    def __init__(self, wikipedia, basedir=None):
        self.name = "oscar"
        movieDB.__init__(self, dbdir=self.name)
        self.wikiData = wikipedia
        
    
    def getCorrectionsDir(self):
        dirname = setDir(self.getMovieDBDir(), "corrections")
        if not isDir(dirname): mkDir(dirname)
        return dirname
    
    
    def createRawOscarData(self, debug=True):
        print("Checking for poorly parsed oscar data.")
        indir = self.wikiData.getResultsDir()
        files = sorted(findExt(indir, ext=".json"))
        if debug:
            print("Found {0} oscar files".format(len(files)))
        yearlyData = {}
        for ifile in files:
            year = getBaseFilename(ifile)
            yearlyData[year] = getFile(ifile)
            
        savename = setFile(self.getCorrectionsDir(), "saved.yaml")
        if not isFile(savename):
            savedData = {}
        else:
            savedData = getFile(savename)
            
        for year in savedData.keys():
            for title in savedData[year].keys():
                savedWinner   = savedData[year][title].get("Winner")
                savedNominees = savedData[year][title].get("Nominees")
                if savedWinner is not None:
                    print("Overwritting {0} {1} winner".format(year,title))
                    yearlyData[year][title]["Winner"] = savedWinner
                if savedNominees is not None:
                    print("Overwritting {0} {1} nominees".format(year,title))
                    yearlyData[year][title]["Nominees"] = savedNominees
            
        
        savename = setFile(self.getCorrectionsDir(), "raw.yaml")
        saveFile(idata=yearlyData, ifile=savename)
    
    
    def findCorrectedOscarData(self, debug=True):
        savename = setFile(self.getCorrectionsDir(), "raw.yaml")
        if not isFile(savename):
            self.createRawOscarData(debug=debug)
            
        rawData = getFile(savename)
            
        savename = setFile(self.getCorrectionsDir(), "corr.yaml")
        if not isFile(savename):
            raise ValueError("There is no corr.yaml file")
            
        corrData = getFile(savename)
            
        savename = setFile(self.getCorrectionsDir(), "saved.yaml")
        if not isFile(savename):
            savedData = {}
        else:
            savedData = getFile(savename)
            
        oscarData = {}
            
        for year in rawData.keys():
            oscarData[year] = {}
            for title in rawData[year].keys():
                oscarData[year][title] = {}
                
                rawWinner   = rawData[year][title]["Winner"]
                rawNominees = rawData[year][title]["Nominees"]
                
                try:
                    savedWinner = savedData[year][title]["Winner"]
                except:
                    savedWinner = None
                    
                try:
                    savedNominees = savedData[year][title]["Nominees"]
                except:
                    savedNominees = None
                
                try:
                    corrWinner = corrData[year][title]["Winner"]
                except:
                    corrWinner = None
                    
                try:
                    corrNominees = corrData[year][title]["Nominees"]
                except:
                    corrNominees = None

                winner   = None
                nominees = None
                if isinstance(savedWinner, list):
                    winner = savedWinner
                if isinstance(savedNominees, list):
                    nominees = savedNominees
                    
                if winner is None:
                    winner = corrWinner
                    if corrWinner != rawWinner:
                        if savedData.get(year) is None:
                            savedData[year] = {}
                        if savedData[year].get(title) is None:
                            savedData[year][title] = {}
                        savedData[year][title]["Winner"] = corrWinner
                        print("Saving {0} {1}".format(year, title))

                if nominees is None:
                    nominees = corrNominees
                    if corrNominees != rawNominees:
                        if savedData.get(year) is None:
                            savedData[year] = {}
                        if savedData[year].get(title) is None:
                            savedData[year][title] = {}
                        savedData[year][title]["Nominees"] = corrNominees
                        print("Saving {0} {1}".format(year, title))


                oscarData[year][title]["Winner"] = winner
                oscarData[year][title]["Nominees"] = nominees

            
        savename = setFile(self.getCorrectionsDir(), "saved.yaml")
        saveFile(idata=savedData, ifile=savename)
        
        
        savename = setFile(self.getResultsDir(), "{0}.yaml".format(self.name))
        saveFile(idata=oscarData, ifile=savename)



    def showOscarData(self):
        backupfilename = setFile(getWikipediaDir(), "oscars.yaml.backup")
        filename = setFile(getWikipediaDir(), "oscars.yaml")
        copyFile(filename, backupfilename)
        data     = get(filename)
        #fixes    = {}
        for year,ydata in data.iteritems():
            #print "\n==>",year
            for cat,catdata in ydata.iteritems():

                winner = catdata["Winner"]
                if isinstance(winner, list):
                    if winner[0].find(",") != -1:
                        print("\t",cat,"\t",winner[0])

                nominees = catdata["Nominees"]
                for nominee in nominees:
                    if isinstance(nominee, list):
                        if nominee[0].find(",") != -1:
                            print("\t",cat,"\t",nominee[0])


        savename = setFile(getOscarDir(), "oscars.yaml")
        print("Saving",len(data),"yearly results to",savename)
        save(savename, data)


    def processOscarData(self, debug=False):
        savename  = setFile(self.getResultsDir(), "{0}.yaml".format(self.name))
        oscarData = getFile(savename)

        yearlyData = {}
        for year,ydata in oscarData.items():
            movies = {}
            for category,categorydata in ydata.items():
                if category.find("Song") != -1:
                    continue
                sf = 1
                if category.find("Song") != -1:
                    sf = 0
                elif category.find("Picture") != -1:
                    sf = 40
                elif category.find("Animated Feature") != -1:
                    sf = 35
                elif category.find("Director") != -1:
                    sf = 30
                elif category.find("Actor") != -1 or category.find("Actress") != -1:
                    sf = 25
                elif category.find("Screenplay") != -1:
                    sf = 20
                winner = categorydata.get("Winner")
                if winner:
                    #print category,'\t',winner
                    if isinstance(winner, list):                    
                        movie = winner[0]
                    else:
                        movie = winner

                    #print category,'\t',10*sf,'\t',winner
                    if movies.get(movie) == None:
                        movies[movie] = 10*sf
                    else:
                        movies[movie] = max(10*sf, movies[movie])

                nominees = categorydata.get("Nominees")
                if nominees:
                    for nominee in nominees:
                        if isinstance(nominee, list):
                            movie = nominee[0]
                        else:
                            movie = nominee

                        #print category,'\t',sf,'\t',winner
                        if movies.get(movie) == None:
                            movies[movie] = sf
                        else:
                            movies[movie] = max(sf, movies[movie])

            yearlyData[year] = sorted(movies.items(), key=operator.itemgetter(1), reverse=True)
            print("---->",year," (Top 15/{0} Movies) <----".format(len(yearlyData[year])))
            for item in yearlyData[year][:15]:
                print(item)
            print('\n')

        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        print("Saving",len(yearlyData),"yearly results to",savename)
        saveFile(savename, yearlyData)