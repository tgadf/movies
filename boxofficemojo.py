import re
from time import sleep
from timeUtils import clock, elapsed
from ioUtils import saveFile, getFile
from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile
from fileUtils import getBaseFilename
from searchUtils import findSubPatternExt, findExt
from strUtils import convertCurrency
from webUtils import getWebData, getHTML
from os import getcwd
import operator


##############################################################################################################################
# Box Office Mojo
##############################################################################################################################
class boxofficemojo():
    def __init__(self, basedir=None):
        if basedir is None:
            from os import getcwd
            self.basedir = getcwd()
        else:
            self.basedir = basedir
            
    def getMovieDir(self):
        dirname = self.basedir
        if not isDir(dirname): mkDir(dirname)
        return dirname
    
    def getBoxOfficeDir(self):
        dirname = setDir(getMovieDir(), "boxoffice.com")
        if not isDir(dirname): mkDir(dirname)
        return dirname

    def getDataDir(self):
        dirname = setDir(self.getBoxOfficeDir(), "data")
        if not isDir(dirname): mkDir(dirname)
        return dirname

    def getResultsDir(self):
        dirname = setDir(self.getBoxOfficeDir(), "results")
        if not isDir(dirname): mkDir(dirname)
        return dirname
    
    
    
    ##############################################################################################################################
    # Get Box Office Weekend Files
    ##############################################################################################################################
    def getBoxOfficeMojoWeekendResult(self, year, week, outdir):
        yname = str(year)
        if week < 10:
            wname = "0"+str(week)
        else:
            wname = str(week)

        url="http://www.boxofficemojo.com/weekend/chart/?yr="+yname+"&wknd="+wname+"&p=.htm"
        savename = setFile(outdir, yname+"-"+wname+".p")
        if isFile(savename): return
        getWebData(base=url, savename=savename, useSafari=False)
        sleep(2)

    def getBoxOfficeMojoWeekendResults(self, startYear = 1982, endYear = 1982):
        outdir = setDir(getBoxOfficeDir(), "data")
        if not isDir(outdir): mkDir(outdir)
        years  = range(int(startYear), int(endYear)+1)
        weeks  = range(1,53)
        for year in years:
            for week in weeks:
                self.getBoxOfficeMojoWeekendResult(year, week, outdir)
                
                
    
    
    ##############################################################################################################################
    # Parse Box Office Weekend Files
    ##############################################################################################################################
    def parseBoxOfficeMojo(self, ifile):
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
                    break
                else:
                    data.append(vals)


        print("Found",len(data),"movies from",ifile            )
        return data


    def parseBoxOfficeMojoResults(self, startYear = 1982, endYear = 2017):
        outdir   = self.getBoxOfficeDir()
        if endYear == None: endYear = startYear
        years    = range(int(startYear), int(endYear)+1)
        for year in years:
            retval = []
            files  = findSubPatternExt(outdir, "data", pattern=str(year), ext=".p")
            for ifile in files:
                result = self.parseBoxOfficeMojo(ifile)
                retval.append(result)

            savename = setFile(getResultsDir(), str(year)+".json")
            print("Saving",len(retval),"weekends of movie data to",savename)
            saveFile(savename, retval)
                
                
    
    
    ##############################################################################################################################
    # Merge Box Office Weekend Files
    ##############################################################################################################################
    def mergeBoxOfficeMojoResults(self):
        retval = {}
        files  = findExt(self.getResultsDir(), ext=".json")
        print("Found {0} files in the results directory".format(len(files)))
        for ifile in files:
            year = getBaseFilename(ifile)
            data = getFile(ifile)
            retval[year] = data

        savename = setFile(self.getBoxOfficeDir(), "results.json")
        print("Saving",len(retval),"years of movie data to",savename)
        saveFile(savename, retval)
                
                
    
    
    ##############################################################################################################################
    # Merge Box Office Weekend Files
    ##############################################################################################################################
    def processBoxOfficeMojo(self):
        outdir   = self.getBoxOfficeDir()
        savename = setFile(outdir, "results.json")

        data = getFile(savename)
        movies = {}
        yearlyData = {}
        for i,year in enumerate(data.keys()):
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
            print("---->",year,"<----")
            for item in yearlyData[year][:25]:
                print(item)
            print('\n')

        savename = setFile(outdir, "boxofficemojo.json")
        print("Saving",len(yearlyData),"yearly results to",savename)
        saveFile(savename, yearlyData)