# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:48:09 2016

@author: tgadfort
"""

import requests
import glob
import json

def clean(value):
    pos = value.find("<")
    if pos != -1:
        value = value[:pos].strip()
    value = value.replace("&rsquo;", "'")
    value = value.replace("&amp;", "and")
    return value

def isName(value):
    if value.find(">") != -1 or value.find("<") != -1:
        return False
    return True


def getHTML(url, savename):
    page = requests.get(url)
    doc=page.text
    f = open(savename, "w")
    f.write(doc.encode('utf-8'))
    f.close()




def parseHTML(htmlfile):
    lines = open(htmlfile).readlines()
    lines = [x.replace("\n","") for x in lines]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.find("<table width=\"90%\"") != -1:
            while line.find("<tr") == -1:
                i += 1
                line = lines[i]
            break
        i += 1

    titles=[]
    while lines[i].find("</tr>") == -1:
        titles.append(lines[i])
        i += 1
    i += 1
    # Skip 2nd line
    while lines[i].find("</tr") == -1:
        i += 1
    
    yearlydata=[]
    while i < len(lines):
        if lines[i+1].find("</table>") != -1: break
        while lines[i].find("<tr") == -1:
            i += 1
        yeardata=[]
        keep = False
        while lines[i].find("</tr") == -1:
            if lines[i].find(".jpg") != -1: keep = True
            yeardata.append(lines[i])
            i += 1            
        if keep:
            print 'len ->',len(yeardata)
            yearlydata.append(yeardata)
        else:
            break
    return yearlydata
    
#    while i < len(lines):
#        if 
        
        
def parseData(yearlydata):
    bestdata={}
    for ydata in yearlydata:
        line = " ".join(ydata)
        pos = -1
        nvals = 0
        line = line.strip()
 #       print line
 #       print ''
        yeardata=[]
        while len(line) > 4:
            pos1 = line.find("<td")
            if pos1 == -1: break
            pos2 = line.find("</td>", pos1+1)
 #           print pos1,pos2
            tddata = line[pos1+3:pos2]
            yeardata.append(tddata)
            line = line[pos2+4:].strip()
#            print tddata,' <----\t',len(line)
#            print ''
            nvals += 1
            if nvals > 7: f()
#        print len(yeardata)
        
        ## Year <-> 0
        line = yeardata[0]
        pos1 = line.find(".html\">")
        pos2 = line.find("</a>", pos1+1)
        year = line[pos1+7:pos2].strip()
        year = year.replace("<strong>", "")
        year = year.replace("</strong>", "")
        year = year.replace("<font size=\"2\">", "")
        year = year.replace("</font>", "")
        year = year.replace("<b>", "")
        year = year.replace("</b>", "")
        
        ## Picture
        line  = yeardata[1]
        pos1  = line.find("<b>")
        
        pos2a  = line.find("</font></b>", pos1+1)
        pos2b  = line.find("</b>", pos1+1)
        if pos2a < pos2b and pos2a > 0:
            pos2 = pos2a
        else:
            pos2 = pos2b
        movie = line[pos1+3:pos2]
        if movie.find("redstar.gif") != -1:
            movie = movie[movie.find("redstar.gif")+1:]        
        if movie.find(">") != -1:
            movie = movie[movie.find(">")+1:]
        if movie.find("<") != -1:
            movie = movie[:movie.find("<")]
        movie = movie.strip()
        mvals = movie.split()
        movie = " ".join(mvals)

        if year == "1967":
            movie = "In the Heat of the Night"
        if year == "1976":
            movie = "Rocky"
        if year == "1983":
            movie = "Terms of Endearment"
        if year == "2008":
            movie = "Slumdog Millionaire"
        if year == "2009":
            movie = "The Hurt Locker"
        if len(movie) < 2:
            print year
            print yeardata[1]
            
            f()
        
        print year,'\t',movie
        
        bestdata[year] = movie        
    return bestdata        
    
    
def formatMovie(movie):
    movie = movie.replace("&quot;", "").strip()
    if movie.find("<b>") != -1:
        pos1 = movie.find("<b>")
        pos2 = movie.find("</b>")
        movie = movie[pos1+3:pos2]
    if movie.find("[") != -1 and movie.find("]") != -1:
        pos1 = movie.find("[")
        movie = movie[:pos1]                
    if movie.find("(also") != -1:
        pos1  = movie.find("(also")
        movie = movie[:pos1].strip()
    movie = movie.replace("<br />", "").strip()
    movie = movie.replace("\"", "").strip()

    return movie

def formatMovies(vals):
    movies={}
    movies["Winner"]=[]
    movies["Nominees"]=[]
    for val in vals:
        if len(val) == 1:
            movie = formatMovie(val[0])
            if movie.upper() == movie:
                movies["Winner"].append([movie])
            else:
                movies["Nominees"].append([movie])
            continue
        
        if len(val) != 2 and len(val) != 3:
            print len(val)
            print 'val --->',val
            f()
            
        
        if val[1].count("\"") >= 1:
            movie = formatMovie(val[1])
            recep = val[0]
            if recep.upper() == recep:
                movies["Winner"].append([recep, movie])
            else:
                movies["Nominees"].append([recep, movie])
        else:
            print "Need to parse this:"
            print "Vals: ",len(vals)
            print "Count:",val[1].count("\"")
            print "Val1: ",val[1]
            f()
            
    print "Formatted movies:"     
    print movies
    print ''
    return movies
            
    
    
def getMovies(award,line):
    
    #print "OG -->",line
    #print ''
    while line.find("<img") != -1:
        pos1 = line.find("<img")
        pos2 = line.find(">", pos1+1)
        line1 = line[:pos1]
        line2 = line[pos2+1:]
        line  = line1 + line2
    
    line = line.replace("&quot;", "\"")
    if line.find("(also") != -1:
        pos1 = line.find("(also")
        pos2 = line.find(")", pos1+1)
        line1 = line[:pos1]
        line2 = line[pos2+1:]
        line  = line1 + line2
        
    while line.find("<a") != -1:
        pos1 = line.find("<a")
        pos2 = line.find(">", pos1+1)
        line1 = line[:pos1]
        line2 = line[pos2+1:]
        line  = line1 + line2
        
    #print 'movies ->',line
    line = line.replace("</a>", "")
    line = line.replace("<b>", "")
    line = line.replace("</b>", "")
    line = line.replace("<br />", "")
    line = line.replace("</font>", "")
    line = line.replace("  ", " ")
    line = line.replace(",\" ", "\", ")
    if line.find("Teresa Wright in \"The Little Foxes, Margaret") != -1:
        line = line.replace("Teresa Wright in \"The Little Foxes, Margaret", "Teresa Wright in \"The Little Foxes\", Margaret")
    
    #print 'movies ->',line
    
    if line.find("),") != -1:
        if line.find("KATHARINE HEPBURN in \"The Lion in Winter\" and BARBRA STREISAND in \"Funny Girl\" (tie),") != -1:
            line = line.replace("KATHARINE HEPBURN in \"The Lion in Winter\" and BARBRA STREISAND in \"Funny Girl\" (tie),", "KATHARINE HEPBURN in \"The Lion in Winter\", BARBRA STREISAND in \"Funny Girl\",")            
        elif line.find("Life is Beautiful\" (Best Foreign Language Film winner)") != -1:
            line = line.replace("Life is Beautiful\" (Best Foreign Language Film winner)", "Life is Beautiful\"")
        else:
            print "---->",line
            f()
    movies = line.split("\",")
    movies = [x.strip() for x in movies]
    movies = [x +"\"" for x in movies]
    movies = [x.replace("\"\"", "\"") for x in movies]


    
    #print "\n --->",award,":::"
    #print "\t LINE ---->",line
    #print "\t SPLIT --->",movies
    #print ''
    
    moviedata=[]
    for movie in movies:
        vals = None
        if movie.find(" for \"") != -1:
            vals = movie.split(" for \"")
            
        if movie.find(" in \"") != -1:
            vals = movie.split(" in \"")
        if vals == None:
            if award == "Production (Picture)" or award == "Picture":
                vals = [movie]
            elif award == "Animated Feature Film":
                vals = [movie]
            else:
                print movie,"    needs parsing"
                continue
        moviedata.append(vals)
        
    #print "\t PARSE --->",moviedata
    moviedata = formatMovies(moviedata)
    
    return moviedata
        
        
def parseOscars(htmlfile):
    if htmlfile == "amc/oscars2010.html": return
        
    lines = open(htmlfile).readlines()
    lines = [x.replace("\n","") for x in lines]
    lines = [x.replace("\r","") for x in lines]
    
    old=0
    if htmlfile == "amc/oscars2000.html": old = 1
    if htmlfile == "amc/oscars2010.html": old = 2
        
            
    odata={}
    
    nyears = 0


    for i in range(len(lines)):
        if lines[i].find("<hr") != -1:
            print i,'\t',lines[i]


    i = 0
    start = 0
    while i < len(lines):

        if old == 0:
            while lines[i].find("<blockquote>") == -1:
                i += 1
                if i >= len(lines): break
            start = i
            if i >= len(lines): break
            i += 1
            yeardata=[]
            while lines[i].find("</blockquote>") == -1:
                yeardata.append(lines[i])
                i += 1
        elif old == 1:
            if start == 0:
                while lines[i].find("<blockquote>") == -1:
                    i += 1
                    if i >= len(lines): break
                #print i,'\t',lines[i]
                start = i
            else:
                #print "HERE",i,'\t',lines[i]
                while lines[i].find("<hr") == -1:
                    i += 1
                    if i >= len(lines): break
                start = i

            #print 'i->',i                
            if i >= len(lines): break
            i += 1
            yeardata=[]
            while lines[i].find("<hr") == -1:
                if len(lines[i].strip()) < 1:
                    i += 1
                    continue
                yeardata.append(lines[i])
                i += 1
                if i >= len(lines): break
            #print 'yeardata ---->',len(yeardata),'\t',start,'\t',i
            i -= 1
        elif old == 2:
            if start == 0:
                while lines[i].find("<h2 align") == -1:
                    i += 1
                    if i >= len(lines): break
#                print i,'\t',lines[i]
                i -= 1
                start = i                
#                f()
            else:
                #print "HERE",i,'\t',lines[i]
                while lines[i].find("<hr") == -1:
                    i += 1
                    if i >= len(lines): break
                start = i

            #print 'i->',i                
            if i >= len(lines): break
            i += 1
            yeardata=[]
            while lines[i].find(".html") == -1:
                i += 1
            while lines[i].find("<hr") == -1:
                yeardata.append(lines[i])
                i += 1
                if i >= len(lines): break
            print 'yeardata ---->',len(yeardata),'\t',start,'\t',i
            i -= 1
#            f()
#        i += 1
#        continue

        if len(yeardata) == 0 and nyears == 10:
            break
            print htmlfile
            print 'i ->',i
            print 'years ->',nyears
            f()

#        i += 1
#        continue


        ## year
        line = yeardata[0]
        pos1 = line.find(".html\">")
        pos2 = line.find("</a>", pos1+1)
        year = line[pos1+7:pos2].strip()
        
        odata[year] = {}
        try:
            ynum = int(year)
        except:
            print 'line --->',line
            print 'year --->',year
            print yeardata
            continue
        
        
        yeardata = yeardata[1:]
        
        print '\n\n\n'
        print "==========================",year,"=========================="
        print "   ===> [",start,'/',len(lines),']'
        print ''
        i += 1
        nyears += 1
#        continue
        ## picture/production
        summary={}
        summary["Production (Picture)"] = []
        summary["Picture"] = []
        summary["Actor"]    = []
        summary["Actress"]  = []
        summary["Supporting Actor"]    = []
        summary["Supporting Actress"]  = []
        summary["Director"] = []
        summary["Animated Feature Film"] = []
        for award in summary.keys():
            check = award + ":"
            for k in range(len(yeardata)):
                if yeardata[k].find(check) != -1:
                    print yeardata[k]
                    k2 = k+1
                    while yeardata[k2].find(":<") == -1 and yeardata[k2].find("<hr") == -1:
                        summary[award].append(yeardata[k2])
                        k2 += 1
                        if k2 >= len(yeardata): break
                    break
            
        #print summary
        print ''
        for award in summary.keys():
            results = summary[award]
            results = [x.strip() for x in results]
            results = " ".join(results)
#            print award,'\t',results
            movies  = getMovies(award, results)
            odata[year][award] = movies

        if len(summary["Picture"]) > 0 and len(summary["Production (Picture)"]) == 0:
            del summary["Production (Picture)"]
        elif len(summary["Picture"]) == 0 and len(summary["Production (Picture)"]) > 0:
            summary["Picture"] = summary["Production (Picture)"]
            del summary["Production (Picture)"]
        else:
            print "No best picture data...."
            print summary
            f()

        for award in odata[year].keys():
            print " >>",award,"<<  \t",odata[year][award]


    return odata        
     


def Fix(award,year,wins,noms):
    if award == "Actor" and int(year) == 2003:
        wins = wins[:2]
        noms.insert(0, ["Johnny Depp", "Pirates of the Caribbean: The Curse of the Black Pearl"])
    if award == "Actor" and int(year) == 2011:
        wins = [wins[0], "The Artist"]
        noms.insert(0, ["Demian Bichir", "A Better Life"])
    if award == "Actor" and int(year) == 2012:
        noms[0] = ["Bradley Cooper", "Silver Linings Playbook"]
        noms.insert(1, ["Hugh Jackman", "Les Miserables"])
    if award == "Supporting Actor" and int(year) == 2013:
        wins = ["JARED LETO","Dallas Buyers Club"]
        noms.insert(0, ["Barkhad Abdi", "Captain Phillips"])
    if award == "Supporting Actress" and int(year) == 2014:
        noms[3] = ["Meryl Streep", "Into the Woods"]
        noms = noms[:4]
    if award == "Actor" and int(year) == 2014:
        noms[3] = ["Michael Keaton", "Birdman"]
        noms = noms[:4]
    if award == "Director" and int(year) == 1991:
        noms.append(["John Singleton", "Boyz N the Hood"])
        noms.append(["Oliver Stone", "JFK"])
    if award == "Director" and int(year) == 1992:
        noms[2] = ["James Ivory", "Howards End"]
        noms.append(["Neil Jordan", "The Crying Game"])
    if award == "Director" and int(year) == 1993:
        noms.append(["Jim Sheridan","In the Name of the Father"])
    if award == "Director" and int(year) == 1994:
        noms.append(["Quentin Tarantino", "Pulp Fiction"])
    if award == "Actor" and int(year) == 1994:
        noms.insert(0, ["Morgan Freeman","The Shawshank Redemption"])
    if award == "Director" and int(year) == 1995:
        noms.append(["Chris Noonan", "Babe"])
        noms.append(["Michael Radford", "Il Postino"])
        noms.append(["Tim Robbins", "Dead Man Walking"])
    if award == "Director" and int(year) == 1997:
        noms.append(["Gus Van Sant", "Good Will Hunting"])
    if award == "Director" and int(year) == 1998:
        noms.append(["Peter Weir", "The Truman Show"])
    if award == "Director" and int(year) == 1999:
        noms.append(["M. Night Shyamalan", "The Sixth Sense"])
    if award == "Actor" and int(year) == 2000:
        noms[3] = ["Geoffrey Rush", "Quills"]
        noms = noms[:4]
    if award == "Actress" and int(year) == 1982:
        noms.insert(1, ["Julie Andrews", "Victor/Victoria"])
    if award == "Director" and int(year) == 1982:
        noms.append(["Steven Spielberg" , "E.T. - The Extra-Terrestrial"])
    if award == "Director" and int(year) == 1983:
        noms.append(["Mike Nichols", "Silkwood"])
        noms.append(["Peter Yates", "The Dresser"])
    if award == "Director" and int(year) == 1984:
        noms[2] = ["Roland Joffe", "The Killing Fields"]
        noms.append(["David Lean for", "A Passage to India"])
    if award == "Director" and int(year) == 1985:
        noms.append(["John Huston", "Prizzi's Honor"])
        noms.append(["Akira Kurosawa", "Ran"])
        noms.append(["Peter Weir", "Witness"])
    if award == "Director" and int(year) == 1987:
        noms.append(["Adrian Lyne", "Fatal Attraction"])
    if award == "Director" and int(year) == 1988:
        noms.append(["Martin Scorsese", "The Last Temptation of Christ"])
    if award == "Director" and int(year) == 1989:
        noms.append(["Peter Weir", "Dead Poets Society"])
    if award == "Director" and int(year) == 1971:
        noms[2] = ["Stanley Kubrick", "A Clockwork Orange"]
        noms.append(["John Schlesinger", "Sunday, Bloody Sunday"])
    if award == "Director" and int(year) == 1972:
        noms.append(["Jan Troell", "The Emigrants"])
    if award == "Director" and int(year) == 1973:
        noms[2] = ["William Friedkin", "The Exorcist"]
        noms.append(["George Lucas", "American Graffiti"])
    if award == "Director" and int(year) == 1975:
        noms.append(["Stanley Kubrick", "Barry Lyndon"])
        noms.append(["Sidney Lumet", "Dog Day Afternoon"])
    if award == "Director" and int(year) == 1978:
        noms.append(["Warren Beatty", "Heaven Can Wait"])
        noms.append(["Alan Parker", "Midnight Express"])
    if award == "Director" and int(year) == 1979:
        noms.append(["Edouard Molinaro", "La Cage Aux Folles"])
        noms.append(["Peter Yates", "Breaking Away"])
    if award == "Director" and int(year) == 1980:
        noms.append(["Martin Scorsese", "Raging Bull"])
    if award == "Director" and int(year) == 1962:
        noms.append(["Frank Perry", "David and Lisa"])
    if award == "Director" and int(year) == 1963:
        noms.append(["Elia Kazan", "America, America"])
        noms.append(["Otto Preminger", "The Cardinal"])
        noms.append(["Martin Ritt", "Hud"])
    if award == "Director" and int(year) == 1964:
        noms.append(["Robert Stevenson", "Mary Poppins"])
    if award == "Director" and int(year) == 1966:
        noms.append(["Mike Nichols", "Who's Afraid of Virginia Woolf?"])
    if award == "Supporting Actor" and int(year) == 1967:
        noms[3] = ["Michael J. Pollard", "Bonnie And Clyde"]
        noms = noms[:4]
    if award == "Actress" and int(year) == 1968:
        noms.insert(0, ["BARBRA STREISAND", "Funny Girl"])
    if award == "Director" and int(year) == 1968:
        noms.append(["Franco Zeffirelli", "Romeo and Juliet"])
    if award == "Director" and int(year) == 1969:
        noms.append(["Sydney Pollack", "They Shoot Horses, Don't They?"])
    if award == "Director" and int(year) == 1970:
        noms[2] = ["Arthur Hiller", "Love Story"]
        noms.append(["Ken Russell", "Women in Love"])
    if award == "Director" and int(year) == 1960:
        noms.append(["Alfred Hitchcock", "Psycho"])
        noms.append(["Fred Zinnemann", "The Sundowners"])
    if award == "Director" and int(year) == 1950:
        noms.append(["Billy Wilder", "Sunset Boulevard"])
    if award == "Director" and int(year) == 1951:
        noms.append(["Vincente Minnell", "An American in Paris"])
        noms.append(["William Wyler", "Detective Story"])
    if award == "Director" and int(year) == 1953:
        noms.append(["William Wyler", "Roman Holiday"])
    if award == "Director" and int(year) == 1954:
        noms.append(["William Wellman", "The High and the Mighty"])
        noms.append(["Billy Wilder", "Sabrina"])
    if award == "Director" and int(year) == 1955:
        noms.append(["John Sturges", "Bad Day at Black Rock"])
    if award == "Director" and int(year) == 1957:
        noms.append(["Mark Robson", "Peyton Place"])
        noms.append(["Billy Wilder", "Witness for the Prosecution"])
    if award == "Director" and int(year) == 1958:
        noms.append(["Robert Wise", "I Want to Live!"])
    if award == "Director" and int(year) == 1959:
        noms.append(["Billy Wilder", "Some Like It Hot"])
        noms.append(["Fred Zinnemann", "The Nun's Story"])
    if award == "Director" and int(year) == 1941:
        noms.append(["Orson Welles", "Citizen Kane"])
        noms.append(["William Wyler", "The Little Foxes"])
    if award == "Director" and int(year) == 1942:
        noms.append(["Mervyn LeRoy", "Random Harvest"])
        noms.append(["Sam Wood", "Kings Row"])
    if award == "Director" and int(year) == 1943:
        noms.append(["George Stevens", "The More the Merrier"])
    if award == "Director" and int(year) == 1945:
        noms.append(["Leo McCarey", "The Bells of St. Mary's"])
        noms.append(["Jean Renoir", "The Southerner"])
    if award == "Director" and int(year) == 1946:
        noms[2] = ["David Lean", "Brief Encounter"]
        noms.append(["Robert Siodmak", "The Killers"])
    if award == "Director" and int(year) == 1948:
        noms.append(["Fred Zinnemann", "The Search"])
    if award == "Director" and int(year) == 1949:
        noms.append(["William A. Wellman", "Battleground"])
        noms.append(["William Wyler", "The Heiress"])
    if award == "Director" and int(year) == 1939:
        noms.append(["William Wyler", "Wuthering Heights"])
    if award == "Director" and int(year) == 1937:
        noms.append(["William Wellmann", "A Star is Born"])
    if award == "Animated Feature Film" and int(year) == 2005:
        wins = "WALLACE & GROMIT IN THE CURSE OF THE WERE-RABBIT"
    if award == "Animated Feature Film" and int(year) == 2014:
        noms[3] = "The Tale of the Princess Kaguya"
        noms = noms[:4]
    if award == "Animated Feature Film" and int(year) == 2013:
        noms[2] = "Ernest and Celestine"
        noms.append("The Wind Rises")
    if award == "Picture" and int(year) == 1969:
        noms.append("Z")
    if award == "Picture" and int(year) == 1970:
        noms.append("M*A*S*H")
    if award == "Picture" and int(year) == 1991:
        noms.insert(2, "JFK")
    if award == "Picture" and int(year) == 1998:
        wins = "SHAKESPEARE IN LOVE"
        noms.insert(0, "Elizabeth")
    if award == "Picture" and int(year) == 1979:
        wins = "Kramer vs. Kramer"
    if award == "Picture" and int(year) == 2007:
        noms[2] = "Michael Clayton"
        noms.append("There Will Be Blood")
    if award == "Supporting Actor" and int(year) == 2014:
        noms[3] = ["Mark Ruffalo", "Foxcatcher"]
    return wins,noms




def checkAMC(amcfile):
    amcdata={}
    moviedata = json.load(open(amcfile))
    years = sorted(moviedata.keys())
    for year in years:
        try:
            int(year)
        except:
            print "Bad year",year
            del moviedata[year]
            continue
        print ""
        print "==>",year
        if int(year) < 1930: continue
        #if int(year) > 1950: f()
        amcdata[year] = {}
        try:
            del moviedata[year]["Production (Picture)"]
        except:
            if int(year) < 2010:
                print "No Production (Picture)"
                continue
        for k,v in moviedata[year].iteritems():
#            if k == "Animated Feature Film":
#                print v
#            continue
            
            if k == "Picture" or k == "Animated Feature Film":
                print '\t',k
                winner   = v["Winner"]
                nominees = v["Nominees"]
                if len(winner) == 0:
                    winner = nominees[0]
                    nominees.pop(0)
                if isinstance(winner,list):
                    winner = clean(winner[0][0])
                noms=[]
                for nom in nominees:
                    if isinstance(nom, list):
                        noms.append(clean(nom[0]))
                nominees = noms
                winner,nominees= Fix(k,int(year), winner,nominees)
                if k == "Picture":
                    if int(year) >= 1950 and int(year) <= 2008:
                        if len(nominees) != 4:
                            print winner
                            print nominees
                            f()
                    if int(year) >= 2009:
                        if len(nominees) < 7:
                            print "Less than 7 nominees"
                            print "  Winner",winner
                            print "  Nominees",nominees
                            f()

                print '\t\tWinner   ->',winner
                print '\t\tNominees ->',nominees
                amcdata[year][k]={}
                amcdata[year][k]["Winner"]   = winner
                amcdata[year][k]["Nominees"] = nominees
            else:
                print '\t',k
                winner   = v["Winner"]
                nominees = v["Nominees"]
                wins=[]
                noms=[]
                try:
                    winner = winner[0]
                    recep  = winner[0]
                    movie  = clean(winner[1])
                except:
                    continue
                if not isName(recep) or not isName(movie):
                    print recep
                    print movie
                    f()
                wins = [recep,movie]
                    
                for nominee in nominees:
                    try:
                        recep  = nominee[0]
                        movie  = clean(nominee[1])
                    except:
                        print nominee
                        f()
                    if not isName(recep) or not isName(movie):
                        print recep
                        print movie
                        f()
                    noms.append([recep,movie])
                wins,noms = Fix(k,int(year), wins,noms)
                if len(noms) != 4 and int(year) >= 1937:
                    print wins
                    print noms
                    f()
                winner = wins
                nominees = noms
                amcdata[year][k]={}
                amcdata[year][k]["Winner"]   = winner
                amcdata[year][k]["Nominees"] = nominees
                print '\t\tWinner   ->',winner
                print '\t\tNominees ->',nominees
                
    
    print "Saving",len(amcdata),"fixed years to oscardata-amc-fixed.json"
    json.dump(amcdata, open("oscardata-amc-fixed.json", "w"))    




def getBond():     
    lines = open("bond.dat").readlines()
    lines = [x.replace("\n", "") for x in lines]

    i = 0
    movies=[]
    while i < len(lines):
        line = lines[i][:-1]
        try:
            num = int(line)
            movie = lines[i+1]
            pos = movie.find(")")
            movie = movie[:pos+1]
            movies.append(movie)
        except:
            movie = None
        i += 1
    print movies
    print len(movies)
    print "Saving",len(movies),"movies to bond.json"
    json.dump(movies, open("bond.json", "w"))
     
     
def getSnub():     
    lines = open("snub.dat").readlines()
    lines = [x.replace("\n", "") for x in lines]
    
    i = 0
    movies=[]
    while i < len(lines):
        try:
            num = int(lines[i])
            movie = lines[i+1]
            movies.append(movie)
        except:
            movie = None
        i += 1
    print "Saving",len(movies),"movies to snubs.json"
    json.dump(movies, open("snubs.json", "w"))

     
     
def getContra():     
    lines = open("contra.dat").readlines()
    lines = [x.replace("\n", "") for x in lines]
    
    i = 0
    movies=[]
    while i < len(lines):
        try:
            num = int(lines[i])
            movie = lines[i+1]
            movies.append(movie)
        except:
            movie = None
        i += 1
    print movies
    print len(movies)
    print "Saving",len(movies),"movies to controversial.json"
    json.dump(movies, open("controversial.json", "w"))
    
    
def inList(item, litems):
    for litem in litems:
        if litem == item:
            return True
    return False
    
def parseOscarData(datfile):
    lines = open(datfile).readlines()
    lines = [x.replace("\n", "") for x in lines]
    
    i = 0
    movies=[]
    yeardata={}
    
    while i < len(lines):
        print i,len(lines)
        if i >= len(lines): break
        if len(lines[i]) < 2:
            i += 1
            continue
        try:
            year = int(lines[i])
            yeardata[year] = []
        except:                
            yeardata[year].append(lines[i])
        i += 1

    amcdata = {}
    for year,ydata in yeardata.iteritems():
        year = str(year)
        summary={}
        summary["Production (Picture)"] = []
        summary["Picture"] = []
        summary["Best Picture"] = []
        summary["Actor"]    = []
        summary["Actress"]  = []
        summary["Supporting Actor"]    = []
        summary["Supporting Actress"]  = []
        summary["Director"] = []
        summary["Animated Feature Film"] = []
        summary["Best Animated Feature Film"] = []
        amcdata[year] = {}
        i = 0
        print year
        while i < len(ydata):
            line = ydata[i].strip()
            print line
            rline = line.replace(":","")
            if inList(rline, summary.keys()):
                award = rline.replace("Best ", "")
                print 'Award ->',award,'\t',year
                if award == "Picture" or award == "Animated Feature Film":
                    i += 1
                    rline = ydata[i].strip().replace(":","")
                    while not inList(rline, summary.keys()):
                        #print '-->',rline
                        summary[award].append(ydata[i].strip())
                        #print award,'=>',summary[award]
                        i += 1
                        rline = ydata[i].strip().replace(":","")
                        if len(summary[award])>10:
                            print summary[award]
                            f()
                            
                    print summary[award]
                    #summary[award] = getMovies(award, ", ".join(summary[award]))
                    #print summary[award]
                    #f()
                else:
                    i += 1
                    rline = ydata[i].strip().replace(":","")
                    summary[award] = ydata[i].strip()
                    i += 1

        for award,awarddata in summary.iteritems():
            if len(awarddata) == 0:
                continue
            print award,awarddata
            if award == "Picture" or award == "Animated Feature Film":
                awarddata = [x.replace(" ("+year+")", "") for x in awarddata]
                winner   = [[awarddata[0]]]
                nominees = [ [x] for x in awarddata[1:] ]
                amcdata[year][award]={}
                amcdata[year][award]["Winner"]   = winner
                amcdata[year][award]["Nominees"] = nominees
            else:   
                amcdata[year][award] = getMovies(award, awarddata)
        #amcdata[year]["Production (Picture)"]={}
    return amcdata
        
##
## Do this every year after the oscars
## 
#getHTML("http://www.filmsite.org/oscars2010.html", "amc/oscars2010.html")


#getSnub()
#getBond()
#getContra()

oscardata={}
for ofile in glob.glob("amc/oscars*.html"):    
    osdata=parseOscars(ofile)
    if isinstance(osdata, dict):
        oscardata.update(osdata)
for ofile in glob.glob("amc/oscars*.dat"):
    osdata=parseOscarData(ofile)
    if isinstance(osdata, dict):
        oscardata.update(osdata)
        

print "Writing",len(oscardata),"to oscardata-amc.json"
#print oscardata.keys()
json.dump(oscardata, open("oscardata-amc.json", "w"))

checkAMC("oscardata-amc.json")

print "All Done!"