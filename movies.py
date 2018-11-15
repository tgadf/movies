# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:42:51 2017

@author: tgadfort
"""


import operator
import sys
import re
from collections import OrderedDict
from time import sleep
from re import search
if '/Users/tgadfort/Python' not in sys.path:
    sys.path.insert(0, '/Users/tgadfort/Python')

from download import getData
from fileio import setFile, setSubFile, isFile, setDir, isDir, mkDir, get, save, getBaseFilename, copyFile
from search import findSubExt, findSubPatternExt
from htmlParser import getHTML
from strops import convertCurrency
from movieRenames import manualRenames


####################################################################################
####################################################################################
#
# Movie Directories
#
####################################################################################
####################################################################################
def getMovieDir():
    return "/Users/tgadfort/Documents/movies"



####################################################################################
####################################################################################
#
# Boxofficemojo.com functions
#
#   1) getBoxOfficeMojoWeekendResults()
#   2) parseBoxOfficeMojoResults()
#   3) mergeBoxOfficeMojoResults()
#   4) processBoxOfficeMojo()
#
####################################################################################
####################################################################################
def getBoxOfficeDir():
    dirname = setDir(getMovieDir(), "boxoffice.com")
    if not isDir(dirname): mkDir(dirname)
    return dirname


def getBoxOfficeMojoWeekendResult(year, week, outdir):
    yname = str(year)
    if week < 10:
        wname = "0"+str(week)
    else:
        wname = str(week)
        
    url="http://www.boxofficemojo.com/weekend/chart/?yr="+yname+"&wknd="+wname+"&p=.htm"
    savename = setFile(outdir, yname+"-"+wname+".p")
    if isFile(savename): return
    getData(base=url, savename=savename, useSafari=False)
    sleep(2)

    

def getBoxOfficeMojoWeekendResults(startYear = 1982, endYear = 2017):
    outdir = setDir(getBoxOfficeDir(), "data")
    if not isDir(outdir): mkDir(outdir)
    years  = range(int(startYear), int(endYear)+1)
    months = range(1,53)
    for year in years:
        for month in months:
            getBoxOfficeMojoWeekendResult(year, month, outdir)



def parseBoxOfficeMojo(ifile):
    htmldata = get(ifile)
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
                    if search("TOTAL \((\d+) MOVIES\)", td.string):
                        break
                except:
                    print j,td.string
                    raise()
                key = keys[j]
                val = td.string
                vals.append(val)
                #print j,'\t',keys[j],'\t',td.string
            if len(vals) == 0: break
            if len(vals) != len(keys):
                print "Mismatch with keys/data"
                print len(keys),'\t',keys
                print len(vals),'\t',vals
                break
            else:
                data.append(vals)

    
    print "Found",len(data),"movies from",ifile            
    return data
            

def parseBoxOfficeMojoResults(startYear = 1982, endYear = 2017):
    outdir   = getBoxOfficeDir()
    if endYear == None: endYear = startYear
    years    = range(int(startYear), int(endYear)+1)
    for year in years:
        retval = []
        files  = findSubPatternExt(outdir, "data", pattern=str(year), ext=".p")
        for ifile in files:
            result = parseBoxOfficeMojo(ifile)
            retval.append(result)

        savename = setSubFile(outdir, "results", str(year)+".json")
        print "Saving",len(retval),"weekends of movie data to",savename
        save(savename, retval)



def mergeBoxOfficeMojoResults():
    outdir = getBoxOfficeDir()
    retval = {}
    files  = findSubExt(outdir, "results", ext=".json")
    for ifile in files:
        year = getBaseFilename(ifile)
        data = get(ifile)
        retval[year] = data
              
    savename = setFile(outdir, "results.json")
    print "Saving",len(retval),"years of movie data to",savename
    save(savename, retval)



def processBoxOfficeMojo():
    outdir   = getBoxOfficeDir()
    savename = setFile(outdir, "results.json")
    
    data = get(savename)
    movies = {}
    yearlyData = {}
    for i,year in enumerate(data.keys()):
        movies[year] = {}
        ydata = data[year]
        for wdata in ydata:
            for mdata in wdata:
                movie  = mdata[2]
                retval = search("\((\d+)\)",movie)
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
        print "---->",year,"<----"
        for item in yearlyData[year][:25]:
            print item
        print '\n'
        
    savename = setFile(outdir, "boxofficemojo.json")
    print "Saving",len(yearlyData),"yearly results to",savename
    save(savename, yearlyData)





####################################################################################
####################################################################################
#
# Rotten Tomatoes.com functions
#
#   1) getRottenTomatoesYearlyResults()
#   2) processRottenTomatoes()
#
#
####################################################################################
####################################################################################
def getRottenTomatoesDir():
    dirname = setDir(getMovieDir(), "rottentomatoes")
    if not isDir(dirname): mkDir(dirname)
    return dirname


def getRottenTomatoesYearlyResult(year, outdir):
    yname = str(year)
    url="https://www.rottentomatoes.com/top/bestofrt/?year="+yname
    savename = setFile(outdir, yname+".p")
    if isFile(savename): return
    getData(base=url, savename=savename, useSafari=True, dtime=10)
    sleep(2)



def getRottenTomatoesYearlyResults(startYear = 1980, endYear = 2017):
    outdir = setDir(getRottenTomatoesDir(), "data")
    if not isDir(outdir): mkDir(outdir)
    
    if endYear == None: endYear = startYear
    years  = range(int(startYear), int(endYear)+1)
    for year in years:
        getRottenTomatoesYearlyResult(year, outdir)



def getRottenTomatoesTop100():
    genres = ["action__adventure", "animation", "art_house__international", 
              "classics", "comedy", "documentary", "drama", "horror", 
              "kids__family", "musical__performing_arts", "mystery__suspense", 
              "romance", "science_fiction__fantasy", "special_interest", 
              "sports__fitness", "television", "western"]
    baseurl="https://www.rottentomatoes.com"
    outdir = setDir(getRottenTomatoesDir(), "top100")
    if not isDir(outdir): mkDir(outdir)
    for genre in genres:
        url = "/top/bestofrt/top_100_"+genre+"_movies/"
        url = baseurl+url
        savename = setFile(outdir, genre+".p")
        if isFile(savename): return
        getData(base=url, savename=savename, useSafari=True, dtime=10)
        sleep(2)



def processRottenTomatoes():
    outdir = getRottenTomatoesDir()
    files  = findSubExt(outdir, "*", ext=".p")
    #files  = glob(join(outdir, "data", "*.p"))
    movies = {}
    yearlyData = {}
    for ifile in files:
        htmldata = get(ifile)
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
                    retval = search("\((\d+)\)",movie)
                    if retval:
                        year  = retval.group()
                        movie = movie.replace(year, "").strip()
                        year  = retval.groups()[0]
                    #retval = search(r'(%d+)', movie)
                    if movies.get(year) == None:
                        movies[year] = {}
                    movies[year][movie] = rating
                    #print year,'\t',rating,'\t',movie
                    
    for year in movies.keys():
        yearlyData[year] = sorted(movies[year].items(), key=operator.itemgetter(1), reverse=True)
        print "---->",year,"<----"
        for item in yearlyData[year][:5]:
            print item
        print '\n'
        
    savename = setFile(outdir, "rottentomatoes.json")
    print "Saving",len(yearlyData),"yearly results to",savename
    save(savename, yearlyData)






####################################################################################
####################################################################################
#
# Wikipedia Functions
#
#   1) getWikipediaOscarData()
#   2) processWikipediaOscarFiles()
#
####################################################################################
####################################################################################
def getWikipediaDir():
    dirname = setDir(getMovieDir(), "wikipedia")
    if not isDir(dirname): mkDir(dirname)
    return dirname



def getWikipediaOscarFile(year, outdir):
    base = "https://en.wikipedia.org/wiki/"
    dmap = {}
    for x in range(1934, 2017+1):
        val = str(x - 1927)+"th_Academy_Awards"
        val = val.replace("1th_", "1st_")
        val = val.replace("2th_", "2nd_")
        val = val.replace("3th_", "3rd_")
        val = val.replace("11st_", "11th_")
        val = val.replace("12nd_", "12th_")
        val = val.replace("13rd_", "13th_")
        dmap[x] = val
    try:
        url = base+dmap[year]
    except:
        print "Could not create url for",year
        return

    print year,'\t',url
    savename = setFile(outdir, str(year)+".p")
    if isFile(savename): return
    getData(base=url, savename=savename, useSafari=False)
    sleep(2)

    
    
def reorderWikipediaOscarData(text, title):
    reorders = ["Best Director", "Best Actress", "Best Actor", 
                "Best Supporting Actor", "Best Supporting Actress"]
    for val in reorders:
        if title.find(val) != -1:
            text = [text[1], text[0]]
            return text
    return text    
    
    
def parseWikipediaOscarDataPre1985(bsdata, debug = False):
    data  = {}
    names = []
    done  = False
    for table in bsdata.findAll("table", {"class": "wikitable"}):
        if done: break
        for i,tr in enumerate(table.findAll("tr")):
            if done: break
            ths = tr.findAll("th")
            if len(ths) > 0: Nth = len(ths)
            for j,th in enumerate(tr.findAll("th")):
                ref = th.find("a")
                if ref:
                    title = ref['title']
                    title = ref.string
                    names.append(title)
                    data[title] = {}
                    if debug: print title,'\t',ref.string

            for j,td in enumerate(tr.findAll("td")):
                title = names[j-Nth]
                #print Nth,'\t',title,'\t',len(names),'\t',len(data)
                if data.get(title): 
                    done = True
                    break
                results = []
                ul = td.find("ul")
                if debug: print title
                for k,li in enumerate(ul.findAll("li")):
                    text = []
                    if k == 0: 
                        for lival in li.findAll("b"):
                            for ref in lival.findAll("a"): 
                                text.append(ref.string)
                    else:
                        for ref in li.findAll("a"):
                            text.append(ref.string)
                    #print title,text
                    if len(text) == 0: continue
                    if len(text) > 2: text = [text[0], ", ".join(text[1:])]
                    #print title,text
                    text = reorderWikipediaOscarData(text, title)
                    results.append(text)

                for k,result in enumerate(results):
                    if isinstance(result, list):
                        if len(result) == 1: results[k] = result[0]

                data[title]["Winner"]   = results[0]
                data[title]["Nominees"] = results[1:]
                if debug:
                    print "      Winner  :",data[title]["Winner"]
                    print "      Nominees:",data[title]["Nominees"]
                    print ""
                    
    for k in data.keys():
        if data[k].get("Winner") == None:
            del data[k]
    return data


def parseWikipediaOscarDataPost1987(bsdata, debug = False):
    data  = {}
    done  = False
    for table in bsdata.findAll("table", {"class": "wikitable"}):
        if done: break
        for i,tr in enumerate(table.findAll("tr")):
            if done: break
            for j,td in enumerate(tr.findAll("td")):
                div = td.find("div")
                if div == None:
                    continue
                    print td
                    raise()
                ref = div.find("a")
                title = ref.string
                data[title] = {}
                if data.get(title): 
                    done = True
                    break
                results = []
                ul = td.find("ul")
                if debug: print title
                for k,li in enumerate(ul.findAll("li")):
                    text = []
                    if k == 0: 
                        for lival in li.findAll("b"):
                            for ref in lival.findAll("a"): 
                                text.append(ref.string)
                    else:
                        for ref in li.findAll("a"):
                            text.append(ref.string)
                    #print title,text
                    if len(text) == 0: continue
                    if len(text) > 2: text = [text[0], ", ".join(text[1:])]
                    #print title,text
                    text = reorderWikipediaOscarData(text, title)
                    results.append(text)

                for k,result in enumerate(results):
                    if isinstance(result, list):
                        if len(result) == 1: results[k] = result[0]

                data[title]["Winner"]   = results[0]
                data[title]["Nominees"] = results[1:]
                if debug:
                    print "      Winner  :",data[title]["Winner"]
                    print "      Nominees:",data[title]["Nominees"]
                    print ""               
    return data
                

    
    
def processWikipediaOscarFiles(procYear = None):
    outdir = getWikipediaDir()
    if procYear == None:
        files = findSubExt(outdir, "data", ext=".p")
        #files = glob(join(outdir, "data", "*.p"))
    else:
        files = findSubPatternExt(outdir, "data", pattern=str(procYear), ext=".p")
        #files = glob(join(outdir, "data", str(procYear)+".p"))

    movies = OrderedDict()    
    for ifile in files:
        print ifile
        year    = getBaseFilename(ifile)
        print year
        #if year == "1985": continue
        htmldata = get(ifile)
        bsdata   = getHTML(htmldata)
        if int(year) <= 1984:
            results = parseWikipediaOscarDataPre1985(bsdata, True)
        elif int(year) >= 1986:
            results = parseWikipediaOscarDataPost1987(bsdata, True)
        else:
            results = parseWikipediaOscarData1985(debug = True)
        movies[year] = results
        for k,v in results.iteritems():
            print "====>",year,'\t',k
            print "      Winner  :",results[k]["Winner"]
            print "      Nominees:",results[k]["Nominees"]
            print ""

    savename = setFile(outdir, "oscars.yaml")
    print "Saving",len(movies),"years of wikipedia oscar data to",savename
    save(savename, movies)
    #yamldata.saveYaml(savename, movies)


def parseWikipediaOscarData1985(debug = True):
    results  = {}

    filename = setSubFile(getWikipediaDir(), "1985", "1985.dat")
    data     = get(filename)
    title    = None
    for line in data:
        if len(line) > 0 and title == None:
            title = line.replace("\t", "")
            title = title.strip()
            results[title] = {}
            continue
        if len(line) == 0:
            title = None
            continue
            if debug:
                print "      Winner  :",data[title]["Winner"]
                print "      Nominees:",data[title]["Nominees"]
                print ""               
        line = line.replace("\xe2\x80\x93", "::")
        vals = line.split(" :: ")
        vals = reorderWikipediaOscarData(vals, title)
        reorders = ["Best Director", "Best Actress", "Best Actor", 
                    "Best Supporting Actor", "Best Supporting Actress"]
        if title in reorders:
            vals[0] = vals[0].split(" as ")[0]

        if results[title].get("Winner") == None:
            results[title]["Winner"] = vals[0]
        else:
            if results[title].get("Nominees") == None:
                results[title]["Nominees"] = []
            results[title]["Nominees"].append(vals[0])

    return results            


def getWikipediaOscarData(startYear = 1934, endYear = 2017):
    outdir = setDir(getWikipediaDir(), "data")
    if not isDir(outdir): mkDir(outdir)

    if endYear == None: endYear = startYear
    years  = range(int(startYear), int(endYear)+1)
    for year in years:
        getWikipediaOscarFile(year, outdir)






####################################################################################
####################################################################################
#
# Sundance functions
#
#   1) getSundanceData()
#
####################################################################################
####################################################################################
def getSundanceDir():
    dirname = setDir(getMovieDir(), "sundance")
    if not isDir(dirname): mkDir(dirname)
    return dirname



def processSundanceData():
    files  = findSubExt(getSundanceDir(), "data", ext=".p")
    data   = OrderedDict()
    for ifile in files:
        htmldata = get(ifile)
        bsdata   = getHTML(htmldata)
        years    = []
        for h2 in bsdata.findAll("h2"):
            span = h2.find("span")
            try:
                year = int(span.string)
            except:
                continue
            years.append(year)

        for j,ul in enumerate(bsdata.findAll("ul")):
            try:
                year = years[j]
            except:
                break
            data[year] = {}
            lis = ul.findAll("li")
            for li in lis:                
                try:
                    txt    = li.text
                    txt    = re.sub("\xe2\x80\x93", " :: ", txt)
                    txt    = re.sub(u"(\u2018|\u2013)", " :: ", txt)
                except:
                    print "Error with",li
                    continue

                vals = txt.split(" :: ")
                if len(vals) > 2:
                    vals[1] = "-".join(vals[1:])
                    vals = vals[:2]
                vals = [x.strip() for x in vals]
                if len(vals) != 2:
                    raise ValueError(vals)

                    
                cat   = vals[0]
                movie = vals[1]
                
                if cat.find("Piper-Heidsieck") != -1:
                    continue
                
                if cat.find("Alfred P. Sloan") != -1:
                    cat = "Alfred P. Sloan Prize"

                
                if cat in ["World Cinema Dramatic Screenwriting Award",
                           "Sundance Institute/Mahindra Global Filmmaking Awards",
                           "World Cinema Documentary Editing Award",
                           "Excellence in Cinematography Award: Documentary",
                           "Excellence in Cinematography Award: Dramatic",
                           "World Cinema Cinematography Award: Documentary",
                           "World Cinema Cinematography Award: Dramatic",
                           "World Cinema Directing Award: Dramatic",
                           "World Cinema Directing Award: Documentary",
                           "World Dramatic Special Jury Prizes for Breakout Performances",
                           "Dramatic Special Jury Prize for Breakout Performance",
                           "Excellence in Cinematography Award Dramatic",
                           "xcellence in Cinematography Award Documentary",
                           "Documentary Editing Award",
                           "Waldo Salt Screenwriting Award: Dramatic",
                           "World Cinema Screenwriting Award",
                           "Directing Award Documentary",
                           "Directing Award Dramatic"]:
                    vals = movie.split(" for ")
                    if len(vals) == 2:
                        movie = vals[1]
                    elif len(vals) == 1:
                        movie = vals[0]
                    else:
                        print "Error in",cat,"===>",movie
                        continue

                if cat in ["Special Jury Prize for Acting"]:
                    movie = movie.replace("for her performance ", "")
                    vals = movie.split(" in ")
                    if len(vals) == 2:
                        movie = vals[1]
                    vals = movie.split(" for ")
                    if len(vals) == 2:
                        movie = vals[1]

                if movie.find("retitled") != -1:
                    movie = movie.split("retitled ")[1]
                    movie = movie[:-1]
                    
                movie = movie.replace(" (tie)", "")
                
                if movie.find(" director of ") != -1:
                    movie = movie.split(" director of ")[1]
                    
                
                print years[j],'\t',cat,'\t\t',movie,'\t\t'
                try:
                    data[year][str(cat)] = str(movie)
                except:
                    data[year][str(cat)] = movie

    savename = setFile(getSundanceDir(), "winners.yaml")
    print "Saving",len(data),"yearly results to",savename
    save(savename, data)


def getSundanceData():
    outdir = getSundanceDir()
    outdir = setDir(outdir(), "data")
    if not isDir(outdir): mkDir(outdir)

    url = "https://en.wikipedia.org/wiki/List_of_Sundance_Film_Festival_award_winners"
    savename = setFile(outdir, "winners.p")
    if isFile(savename): return
    getData(base=url, savename=savename, useSafari=False)
    sleep(2)

    


####################################################################################
####################################################################################
#
# Oscars functions
#
####################################################################################
####################################################################################
def getOscarDir():
    dirname = setDir(getMovieDir(), "oscars")
    if not isDir(dirname): mkDir(dirname)
    return dirname


def correctOscarData():
    print "Checking for unparsed oscar data."
    backupfilename = setFile(getWikipediaDir(), "oscars.yaml.backup")    
    filename = setFile(getWikipediaDir(), "oscars.yaml")
    copyFile(filename, backupfilename)
    data     = get(filename)
    #fixes    = {}
    for year,ydata in data.iteritems():
        print "\n==>",year
        for cat,catdata in ydata.iteritems():
            
            winner = catdata["Winner"]
            if isinstance(winner, list):
                if winner[0].find(",") != -1:
                    print "\t",cat,"\t",winner[0]

            nominees = catdata["Nominees"]
            for nominee in nominees:
                if isinstance(nominee, list):
                    if nominee[0].find(",") != -1:
                        print "\t",cat,"\t",nominee[0]


    savename = setFile(getOscarDir(), "oscars.yaml")
    print "Saving",len(data),"yearly results to",savename
    save(savename, data)


def getOscarData():    
    filename   = setFile(getOscarDir(), "oscars.yaml")
    data       = get(filename)
    yearlyData = {}
    for year,ydata in data.iteritems():
        
        movies = {}
        for category,categorydata in ydata.iteritems():
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
        print "---->",year,"<----"
        for item in yearlyData[year][:15]:
            print item
        print '\n'
        
    savename = setFile(getOscarDir(), "oscars.json")
    print "Saving",len(yearlyData),"yearly results to",savename
    save(savename, yearlyData)
    





####################################################################################
####################################################################################
#
# Combine Movies
#
####################################################################################
####################################################################################


def combineMovies(minOscarVal = 10, minRottenVal = 100, minBoxOfficeVal = 20e6,
                  keepIMAX = False, debug = False):
    outdir             = getMovieDir()
    
    oscarsFile         = setSubFile(outdir, "oscars", "oscars.json")
    boxofficeFile      = setSubFile(outdir, "boxoffice.com", "boxofficemojo.json")
    rottentomatoesFile = setSubFile(outdir, "rottentomatoes", "rottentomatoes.json")
    print oscarsFile
    print boxofficeFile
    print rottentomatoesFile
    
    oscarData          = get(oscarsFile)
    boxofficeData      = get(boxofficeFile)
    rottentomatoesData = get(rottentomatoesFile)
    
    movieCounter = {}    
    
    yearlyMovies = OrderedDict()
    years = sorted(list(set(oscarData.keys() + boxofficeData.keys() + rottentomatoesData.keys())))
    for year in years:        
        
        oscarMovies          = oscarData.get(year)
        boxofficeMovies      = boxofficeData.get(year)
        rottentomatoesMovies = rottentomatoesData.get(year)
        
        if oscarMovies:
            if debug: print year,'\t','Oscars         ','\t',len(oscarMovies),'\t',
            oscarMovies = [x[0] for x in oscarMovies if x[1] >= minOscarVal]
            if debug: print len(oscarMovies)
        else:
            oscarMovies = []
        
        if boxofficeMovies:
            if debug: print year,'\t','Box Office     ','\t',len(boxofficeMovies),'\t',
            boxofficeMovies = [x[0] for x in boxofficeMovies if x[1] >= minBoxOfficeVal]
            if debug: print len(boxofficeMovies)
        else:
            boxofficeMovies = []
            
        if rottentomatoesMovies:
            if debug: print year,'\t','Rotten Tomatoes','\t',len(rottentomatoesMovies),'\t',
            rottentomatoesMovies = [x[0] for x in rottentomatoesMovies if x[1] >= minRottenVal]
            if debug: print len(rottentomatoesMovies)
        else:
            rottentomatoesMovies = []    
                
        movies = OrderedDict()
        for movie in oscarMovies:
            movie = manualRenames(movie, year, keepIMAX)
            if movie:
                movies[movie] = "Oscar"
            
        for movie in boxofficeMovies:
            movie = manualRenames(movie, year, keepIMAX)
            if movie:
                if movies.get(movie): continue
                movies[movie] = "Box Office"
            
        for movie in rottentomatoesMovies:
            if movie:
                movie = manualRenames(movie, year, keepIMAX)
                if movies.get(movie): continue
                movies[movie] = "Rotten Tomatoes"

        for movie in movies.keys():
            uyear = unicode(str(int(year)), 'utf-8')
            testmovie = movie + u" ["+uyear+u"]"
            if movieCounter.get(testmovie):
                print "Removing",movie,"[",year,"] --->",movieCounter[testmovie]
                del movies[movie]
                continue

            stop = False
            for dyear in [1, -1, 2, -2]:
                uyear = unicode(str(int(year)+dyear), 'utf-8')
                testmovie2 = movie + u" ["+uyear+u"]"
                if movieCounter.get(testmovie2):
                    print "Removing",movie,"[",year,"] --->",movieCounter[testmovie2]
                    del movies[movie]
                    stop = True
                    break
            if stop:
                continue

            movieCounter[testmovie] = testmovie #movies[movie]
            
            
        yearlyMovies[year] = movies

        if debug: 
            print year,'\t','   ----->      ','\t\t',len(movies.keys())
            for movie,mtype in movies.iteritems():
                print      '\t','\t',movie,mtype

    for year in yearlyMovies.keys():
        for movie in yearlyMovies[year].keys():
            if movie.find(": ") != -1:
                print "    if movie == \""+movie+"\":"
                print "        return u\""+movie.replace(": ", " ")+"\""

                
    mergeYearlyMovies(outdir, yearlyMovies)
    
    
def mergeYearlyMovies(outdir, yearlyMovies):
    data = OrderedDict()
    for year,ymovies in yearlyMovies.iteritems():
        data[year] = {}
        for movie,movieType in ymovies.iteritems():
            if data[year].get(movieType) == None:
                data[year][movieType] = {}
            data[year][movieType][movie] = None

    savename = setFile(outdir, "officialMovies.yaml")
    print "Saving",len(data),"to",savename
    save(savename, data)