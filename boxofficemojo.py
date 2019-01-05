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
# Box Office Mojo
##############################################################################################################################
class boxofficemojo(movieDB):
    def __init__(self, basedir=None):
        self.name = "boxofficemojo"
        movieDB.__init__(self, dbdir=self.name)
    
    
    
    ###########################################################################################################################
    # Get Box Office Weekend Files
    ###########################################################################################################################
    def downloadBoxOfficeMojoWeekendData(self, year, week, outdir, debug=False):
        yname = str(year)
        if week < 10:
            wname = "0"+str(week)
        else:
            wname = str(week)

        url="http://www.boxofficemojo.com/weekend/chart/?yr="+yname+"&wknd="+wname+"&p=.htm"
        savename = setFile(outdir, yname+"-"+wname+".p")
        if isFile(savename): return
        if debug:
            print("Downloading/Saving {0}".format(savename))
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(2)

    def getBoxOfficeMojoWeekendData(self, startYear = 1982, endYear = 1982, debug=False):
        outdir = self.getDataDir()
        if debug:
            print("Data Directory: {0}".format(outdir))
        #outdir = setDir(getBoxOfficeDir(), "data")
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        weeks  = range(1,53)
        for year in years:
            for week in weeks:
                self.downloadBoxOfficeMojoWeekendData(year, week, outdir, debug)
                
                
    
    
    ###########################################################################################################################
    # Parse Box Office Weekend Files
    ###########################################################################################################################
    def parseBoxOfficeMojo(self, ifile, debug=False):
        htmldata = getFile(ifile)
        bsdata   = getHTML(htmldata)
        tbl = None
        for table in bsdata.findAll("table"):
            if tbl:
                break
            for tr in table.findAll("tr"):
                if len(tr) >= 10:
                    tbl = table
                    break
                else:
                    break

        #print len(tbl)
        keys = []
        data = []
        for i,tr in enumerate(tbl):
            vals = []
            if i == 0:
                for j,td in enumerate(tr.findAll("td")):
                    for ref in td.findAll("a"):
                        key = ref.string
                        keys.append(key)
            else:
                if len(tr) <= 1: continue
                #print "\n\n\nNext...."
                #print tr
                #print "  tr-->",tr,'\t',len(tr)
                #print i,tr,len(data)
                for j,td in enumerate(tr.findAll("td")):
                    if td.string == None:
                        continue
                    try:
                        if re.search("TOTAL \((\d+) MOVIES\)", td.string):
                            break
                    except:
                        print(j,td.string)
                        raise()
                    key = keys[j]
                    val = td.string
                    vals.append(val)
                    #print j,'\t',keys[j],'\t',td.string
                if len(vals) == 0: break
                if len(vals) != len(keys):
                    print("Mismatch with keys/data")
                    print(len(keys),'\t',keys)
                    print(len(vals),'\t',vals)
                    raise("YO")
                    break
                else:
                    data.append(vals)

        if debug:
            print("Found",len(data),"movies from",ifile)
        return data


    def parseBoxOfficeMojoResults(self, startYear = 1982, endYear = 2017, debug=False):
        outdir = self.getDataDir()
        resultsdir = self.getResultsDir()
        
        if endYear == None: endYear = startYear
        years    = range(int(startYear), int(endYear)+1)
        for year in years:
            retval = []
            files  = findPatternExt(outdir, pattern=str(year), ext=".p")
            for ifile in files:
                result = self.parseBoxOfficeMojo(ifile, debug=debug)
                retval.append(result)

            savename = setFile(resultsdir, str(year)+".json")
            print("Saving",len(retval),"weekends of movie data to",savename)
            saveFile(savename, retval)
                
                
    
    
    ###########################################################################################################################
    # Merge Box Office Weekend Files
    ###########################################################################################################################
    def mergeBoxOfficeMojoResults(self, debug=False):
        retval = {}
        files  = findExt(self.getResultsDir(), ext=".json")
        if debug:
            print("Found {0} files in the results directory".format(len(files)))
        for ifile in sorted(files):
            year = getBaseFilename(ifile)
            try:
                int(year)
            except:
                continue
            data = getFile(ifile)
            retval[year] = data
            if debug:
                print("  Adding {0} entries from {1}".format(len(data), ifile))

        savename = setFile(self.getResultsDir(), "results.json")
        if debug:
            print("Saving",len(retval),"years of movie data to",savename)
        saveFile(savename, retval)
                
                
    
    
    ###########################################################################################################################
    # Merge Box Office Weekend Files
    ###########################################################################################################################
    def processBoxOfficeMojo(self, debug=False):
        outdir   = self.getResultsDir()
        savename = setFile(outdir, "results.json")

        data = getFile(savename)
        movies = {}
        yearlyData = {}
        for i,year in enumerate(sorted(data.keys())):
            movies[year] = {}
            ydata = data[year]
            
            for wdata in ydata:
                for mdata in wdata:
                    movie  = mdata[2]
                    retval = re.search("\((\d+)\)",movie)
                    if retval:
                        stryear  = retval.group()
                        movie = movie.replace(stryear, "").strip()

                    gross  = convertCurrency(mdata[9])
                    weekly = convertCurrency(mdata[4])
                    money  = max(gross, weekly)
                    if movies[year].get(movie) == None:
                        movies[year][movie] = money
                    else:                    
                        movies[year][movie] = max(money, movies[year][movie])

            yearlyData[year] = sorted(movies[year].items(), key=operator.itemgetter(1), reverse=True)
            print("---->",year," (Top 25/{0} Movies) <----".format(len(yearlyData[year])))
            for item in yearlyData[year][:25]:
                print(item)
            print('\n')

        savename = setFile(outdir, "{0}.json".format(self.name))
        print("Saving",len(yearlyData),"yearly results to",savename)
        saveFile(savename, yearlyData)
                
                
    
    
    ###########################################################################################################################
    # Search Box Office
    ###########################################################################################################################
    def searchBoxOfficeMojo(self, movie, debug=False):
        savename = setFile(self.getResultsDir(), "{0}.json".format(self.name))
        data = getFile(savename)
        print("Nearest matches for {0}".format(movie))
        for year,yearlyMovies in data.items():
            result = findNearest(movie, [x[0] for x in yearlyMovies], num=1, cutoff=0.9)
            if len(result) > 0:
                values = [(name, value) for name,value in yearlyMovies if name in result]
                print("{0: <6}{1}".format(year,values))