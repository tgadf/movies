#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:18:51 2017

@author: tgadfort
"""

def manualRenames(movie, year, keepIMAX = True):

    if isinstance(movie, str):
        movie = unicode(movie, 'utf-8')

    movie = movie.replace(" as a ", " As A ")
    movie = movie.replace(" of the ", " Of The ")    
    movie = movie.replace(" of a ", " Of A ")
    movie = movie.replace(" for a ", " For A ")
    movie = movie.replace(" with a ", " With A ")
    movie = movie.replace(" with the ", " With The ")    
    movie = movie.replace(" from the ", " From The ")    
    movie = movie.replace(" for the ", " For The ")    
    movie = movie.replace(" to the ", " To The ")
    movie = movie.replace(" on the ", " On The ")
    movie = movie.replace(" of the ", " Of The ")
    movie = movie.replace(" in the ", " In The ")    
    movie = movie.replace(" at the ", " At The ")    
    movie = movie.replace(" is the ", " Is The ")    
    movie = movie.replace(" and the ", " And The ")    
    movie = movie.replace(" in ", " In ") 
    movie = movie.replace(" on ", " On ")
    movie = movie.replace(" our ", " Our ") 
    movie = movie.replace(" by ", " By ") 
    movie = movie.replace(" is ", " Is ")
    movie = movie.replace(" to ", " To ")    
    movie = movie.replace(" of ", " Of ")
    movie = movie.replace(" or ", " Or ")
    movie = movie.replace(" at ", " At ")    
    movie = movie.replace(" as ", " As ")
    movie = movie.replace(" over ", " Over ")
    movie = movie.replace(" for ", " For ")    
    movie = movie.replace(" a ", " A ")    
    movie = movie.replace(" with ", " With ")
    movie = movie.replace(" from ", " From ")
    movie = movie.replace(" and ", " And ")    
    movie = movie.replace(" the ", " The ")        
    
    if not keepIMAX:
        if movie.find("(IMAX)") != -1:
            return None
    
    if movie.find("Maze Runner: ") != -1:
        return movie.replace("Maze Runner: ", "Maze Runner ")
    if movie.find("Alvin And The Chipmunks: ") != -1:
        return movie.replace("Alvin And The Chipmunks: ", "Alvin And The Chipmunks ")   
    if movie.find("The Hobbit: ") != -1:
        return movie.replace("The Hobbit: ", "The Hobbit ")
    if movie.find("Percy Jackson: ") != -1:
        return movie.replace("Percy Jackson: ", "Percy Jackson ")
    if movie.find("Night At The Museum: ") != -1:
        return movie.replace("Night At The Museum: ", "Night At The Museum ")
    if movie.find("Exodus: ") != -1:
        return movie.replace("Exodus: ", "Exodus ")
    if movie.find("Lessons: ") != -1:
        return movie.replace("Lessons: ", "Lessons ")
    if movie.find("Guardians: ") != -1:
        return movie.replace("Guardians: ", "Guardians ")
    if movie.find("Narnia: ") != -1:
        return movie.replace("Narnia: ", "Narnia ")
    if movie.find("Shadows: ") != -1:
        return movie.replace("Shadows: ", "Shadows ")
    if movie.find("Sweeney Todd: ") != -1:
        return movie.replace("Sweeney Todd: ", "Sweeney Todd ")
    if movie.find("High School Musical 3: ") != -1:
        return movie.replace("High School Musical 3: ", "High School Musical 3 ")
    if movie.find("Borat: ") != -1:
        return movie.replace("Borat: ", "Borat ")
    if movie.find("Bridget Jones: ") != -1:
        return movie.replace("Bridget Jones: ", "Bridget Jones ")
    if movie.find("Blade: ") != -1:
        return movie.replace("Blade: ", "Blade ")
    if movie.find("Caribbean: ") != -1:
        return movie.replace("Caribbean: ", "Caribbean ")
    if movie.find("Commander: ") != -1:
        return movie.replace("Commander: ", "Commander ")
    if movie.find("Jonah: ") != -1:
        return movie.replace("Jonah: ", "Jonah ")
    if movie.find("America: ") != -1:
        return movie.replace("America: ", "America ")
    if movie.find("Holmes: ") != -1:
        return movie.replace("Holmes: ", "Holmes ")
    if movie.find("Reacher:") != -1:
        return movie.replace("Reacher: ", "Reacher ")
    if movie.find("Rogue One:") != -1:
        return movie.replace("Rogue One: ", "Rogue One ")
    if movie.find("Lights: ") != -1:
        return movie.replace("Lights: ", "Lights ")
    if movie.find("Arthur: ") != -1:
        return movie.replace("Arthur: ", "Arthur ")
    if movie.find("Kong: ") != -1:
        return movie.replace("Kong: ", "Kong ")
    if movie.find("Underpants: ") != -1:
        return movie.replace("Underpants: ", "Underpants ")
    if movie.find("xXx: ") != -1:
        return movie.replace("xXx: ", "xXx ")
    if movie.find("Hotline: ") != -1:
        return movie.replace("Hotline: ", "Hotline ")
    if movie.find("Mechnanic: ") != -1:
        return movie.replace("Mechanic: ", "Mechanic ")
    if movie.find("River: ") != -1:
        return movie.replace("River: ", "River ")
    if movie.find("300: ") != -1:
        return movie.replace("300: ", "300 ")
    if movie.find("Hitman: ") != -1:
        return movie.replace("Hitman: ", "Hitman ")
    if movie.find("Kingman: ") != -1:
        return movie.replace("Kingman: ", "Kingman ")
    if movie.find("Blart: ") != -1:
        return movie.replace("Blart: ", "Blart ")
    if movie.find("Ouija: ") != -1:
        return movie.replace("Ouija: ", "Ouija ")
    if movie.find("Hansel And Gretel: ") != -1:
        return movie.replace("Hansel And Gretel: ", "Hansel And Gretel ")

    if movie == "O.J.: Made In America":
        return u"OJ Made in America"
    if movie == "* batteries not included":
        return "Batteries Not Included"
    if movie == "The LEGO Movie":
        return u"The Lego Movie"
    if movie == "Birdman Or (The Unexpected Virtue Of Ignorance)":
        return u"Birdman"
    if movie == "Lara Croft: Tomb Raider":
        return u"Lara Croft Tomb Raider 1"
    if movie == "Lara Croft Tomb Raider: The Cradle Of Life":
        return u"Lara Croft Tomb Raider 2 The Cradle Of Life"
    if movie == "Lara Croft Tomb Raider 2: The Cradle Of Life":
        return u"Lara Croft Tomb Raider 2 The Cradle Of Life"
    if movie == "Marvel's The Avengers":
        return u"The Avengers"
    if movie == "The Dark Knight":
        return u"Batman The Dark Knight"
    if movie == "The Dark Knight Rises":
        return u"Batman The Dark Knight Rises"
    if movie == "The Twilight Saga: Breaking Dawn Part 1":
        return u"Twilight Breaking Dawn Part 1"
    if movie == "The Twilight Saga: Breaking Dawn Part 2":
        return u"Twilight Breaking Dawn Part 2"
    if movie == "The Twilight Saga: New Moon":
        return u"Twilight New Moon"
    if movie == "The Twilight Saga: Eclipse":
        return u"Twilight Eclipse"
    if movie == "Y tu mamá también":
        return u"Y Tu Mamá También"
    if movie == "The Lord Of The Rings: The Fellowship Of The Ring":
        return u"The Lord Of The Rings I The Fellowship Of The Ring"
    if movie == "The Lord Of The Rings: The Two Towers":
        return u"The Lord Of The Rings II The Two Towers"
    if movie == "The Lord Of The Rings: The Return Of The King":
        return u"The Lord Of The Rings III The Return Of The King"
        
    if movie == "Star Wars: Episode I - The Phantom Menace":
        return u"Star Wars Episode I The Phantom Menace"
    if movie == "Star Wars: Episode II - Attack Of The Clones":
        return u"Star Wars Episode II Attack Of The Clones"
    if movie == "Star Wars: Episode III - Revenge Of The Sith":
        return u"Star Wars Episode III Revenge Of The Sith"
    if movie == "Star Wars" or movie == "Star Wars (Special Edition)":
        return u"Star Wars Episode IV A New Hope"
    if movie == "Star Wars: Episode IV - A New Hope":
        return u"Star Wars Episode IV A New Hope"
    if movie == "The Empire Strikes Back":
        return u"Star Wars Episode V The Empire Strikes Back"
    if movie == "Return Of The Jedi":
        return u"Star Wars Episode VI Return Of The Jedi"
    if movie == "Star Wars: The Force Awakens":
        return u"Star Wars Episode VII The Force Awakens"
    if movie == "Star Wars: Episode VII - The Force Awakens":
        return u"Star Wars Episode VII - The Force Awakens"
        
    if movie == "South Park - Bigger, Longer And Uncut":
        return u"South Park Bigger, Longer And Uncut"
    if movie == "La Vie en Rose":
        return u"La Vie En Rose"
    if movie == "48 HRS":
        return u"48 Hrs."
    if movie == "Hannah Montana/Miley Cyrus: Best Of Both Worlds Concert Tour":
        return u"Hannah Montana Miley Cyrus Best Of Both Worlds Concert Tour"
    if movie == "Transformers":
        return u"Transformers I"
    if movie == "Transformers: Revenge Of The Fallen":
        return u"Transformers II Revenge Of The Fallen"
    if movie == "Transformers: Dark Of The Moon":
        return u"Transformers III Dark Side Of The Moon"
    if movie == "Transformers: Age Of Extinction" or movie == "Transformers: Age of Extinction":
        return u"Transformers IV Age Of Extinction"
        
    if movie == "Harry Potter And The Sorcerer's Stone":
        return u"Harry Potter 1 And The Sorcerers Stone"
    if movie == "Harry Potter And The Chamber Of Secrets":
        return u"Harry Potter 2 And The Chamber Of Secrets"
    if movie == "Harry Potter And The Prisoner Of Azkaban":
        return u"Harry Potter 3 And The Prisoner Of Azkaban"
    if movie == "Harry Potter And The Goblet Of Fire":
        return u"Harry Potter 4 And The Goblet Of Fire"
    if movie == "Harry Potter And The Order Of The Phoenix":
        return u"Harry Potter 5 And The Order Of The Phoenix"
    if movie == "Harry Potter And The Half-Blood Prince":
        return u"Harry Potter 6 And The Half-Blood Prince"
    if movie == "Harry Potter And The Deathly Hallows Part 1":
        return u"Harry Potter 7 And The Deathly Hallows Part 1"
    if movie == "Harry Potter and the Deathly Hallows Part 2":
        return u"Harry Potter 7 And The Deathly Hallows Part 2"
    if movie == "Harry Potter And The Deathly Hallows Part 2":
        return u"Harry Potter 7 And The Deathly Hallows Part 2"
        
    if movie == "Tinker, Tailor, Soldier, Spy":
        return u"Tinker Tailor Soldier Spy"
    if movie == "Monster-in-Law":
        return u"Monster-In-Law"
    if movie == "The Sea Inside":
        return u"The Sea Inside (Mar Adentro)"
    if movie.find("Precious: Based") != -1:
        return u"Precious"
    if movie == "Departures":
        return u"Departures (Okuribito)"
    if movie == "Scott Pilgrim vs. The World":
        return u"Scott Pilgrim Vs. The World"

    if movie == "Dr. Strangelove Or How I Learned to Stop Worrying and Love the Bomb":
        return u"Dr. Strangelove"
    if movie == "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb":
        return u"Dr. Strangelove"
        
    if movie == "12 Angry Men (Twelve Angry Men)":
        return u"12 Angry Men"
    if movie == "Night at the Museum":
        return u"Night At The Museum"
    if movie == "GETT: The Trial Of Viviane Amsalem":
        return u"Gett The Trial Of Viviane Amsalem"
    if movie == "Lee Daniels' The Butler":
        return u"The Butler"
        
    if movie == "Three Colors: Blue (Trois Couleurs: Bleu)":
        return u"Three Colors Blue (Trois Couleurs Bleu)"
    if movie == "Three Colors: Red (Trois Couleurs: Rouge)":
        return u"Three Colors Red (Trois Couleurs Rouge)"
    if movie == "Three Colors: Red (Trois couleurs: Rouge)" or movie == "Three Colors: Red":
        return u"Three Colors Red (Trois Couleurs Rouge)"
    if movie == "Three Colors: White (Trois Couleurs: Blanc)":
        return u"Three Colors White (Trois Couleurs Blanc)"
        
    if movie == "Raiders Of The Lost Ark" or movie == "Raiders of the Lost Ark":
        return u"Indiana Jones And The Raiders Of The Lost Ark"
    if movie == "The Lion King (in 3D)":
        return u"The Lion King"
        
    if movie == "Licence To Kill":
        return u"James Bond Licence To Kill"
    if movie == "A View To A Kill":
        return u"James Bond A View To A Kill"
    if movie == "The Living Daylights":
        return u"James Bond The Living Daylights"
    if movie == "Octopussy":
        return u"James Bond Octopussy"
    if movie == "Never Say Never Again":
        return u"James Bond Never Say Never Again"
    if movie == "Casino Royale":
        return u"James Bond Casino Royale"
    if movie == "GoldenEye":
        return u"James Bond Goldeneye"
    if movie == "Tomorrow Never Dies":
        return u"James Bond Tomorrow Never Dies"
    if movie == "Die Another Day":
        return u"James Bond Die Another Day"
    if movie == "The World Is Not Enough":
        return u"James Bond The World Is Not Enough"
    if movie == "Quantum Of Solace":
        return u"James Bond Quantum Of Solace"
        
    if movie == "Thirteen Ghosts":
        return u"Thir13En Ghosts"
    if movie == "In A Better World":
        return u"In A Better World (Haevnen)"
    if movie == "Cyrano de Bergerac":
        return u"Cyrano De Bergerac"
    if movie == "The People vs. Larry Flynt":
        return u"The People Vs. Larry Flynt"
    if movie == "Fahrenheit 9/11":
        return u"Fahrenheit 911"
    if movie == "Fast Five":
        return u"Fast And Furious 5"
    if movie == "Up in the Air":
        return u"Up In The Air"
    if movie == "The Secret In their Eyes":
        return u"The Secret In Their Eyes"
    if movie == "The Divergent Series: Insurgent":
        return u"Divergent Insurgent"
    if movie == "The Divergent Series: Allegiant":
        return u"Divergent Allegiant"
    if movie == "Tim Burton's The Nightmare Before Christmas":
        return u"The Nightmare Before Christmas"

    if movie == "A Nightmare On Elm Street":
        if year < 2000:
            return u"A Nightmare On Elm Street 1"
        else:
            return u"A Nightmare On Elm Street 9"            
    if movie == "A Nightmare On Elm Street 2: Freddy's Revenge":
        return u"A Nightmare On Elm Street 2 Freddy's Revenge"
    if movie == "A Nightmare On Elm Street 3: Dream Warriors":
        return u"A Nightmare On Elm Street 3 Dream Warriors"
    if movie == "A Nightmare On Elm Street 4: The Dream Master":
        return u"A Nightmare On Elm Street 4 The Dream Master"
    if movie == "A Nightmare On Elm Street 5: The Dream Child":
        return u"A Nightmare On Elm Street 5 The Dream Child"
    if movie == "Freddy's Dead: The Final Nightmare":
        return u"A Nightmare On Elm Street 6 Freddy's Dead"
    if movie == "A Nightmare On Elm Street 6: Freddy's Dead":
        return u"A Nightmare On Elm Street 6 Freddy's Dead"
    if movie == "A Nightmare On Elm Street 7: The Ascension":
        return u"A Nightmare On Elm Street 7 The Ascension"
    if movie == "A Nightmare On Elm Street 8: Freddy Vs Jason":
        return u"A Nightmare On Elm Street 8 Freddy Vs Jason"
    
    if movie == "Pride And Prejudice":
        return u"Pride & Prejudice"
    if movie == "Jaws 3-D":
        return u"Jaws 3"
    if movie == "Shark Night 3D":
        return u"Shark Night"
    if movie == "First Blood":
        return u"Rambo First Blood"
    if movie == "Thelma And Louise":
        return u"Thelma & Louise"
    if movie == "50/50":
        return u"50-50"
    if movie == "Amelie":
        return u"Amélie"
    if movie == "A Very Harold & Kumar 3D Christmas":
        return u"A Very Harold & Kumar Christmas"
    if movie == "Love with the Proper Stranger":
        return u"Love With The Proper Stranger"
    if movie == "Underworld: Blood Wars":
        return u"Underworld Blood Wars"
    if movie == "D2: The Mighty Ducks":
        return u"The Mighty Ducks 2"
    if movie == "D3: The Mighty Ducks":
        return u"The Mighty Ducks 3"
    if movie == "Friday The 13th - Part V":
        return u"Friday The 13th Part 5 A New Beginning"
    if movie == "Friday The 13th Part III":
        return u"Friday The 13th Part 3"
    if movie == "Friday The 13th Part VI":
        return u"Friday The 13th Part 6 Jason Lives"
    if movie == "Friday The 13th: Final Chapter":
        return u"Friday The 13th Part 4 Final Chapter"
    if movie == "Friday The 13th Part 7":
        return u"Friday The 13th Part 7 The New Blood"
    if movie == "Friday The 13th Part VII":
        return u"Friday The 13th Part 7 The New Blood"
    if movie == "Friday The 13th Part 8":
        return u"Friday The 13th Part 8 Jason Takes Manhattan"
    if movie == "Jason Goes To Hell: The Final Friday":
        return u"Jason Goes To Hell The Final Friday"
        
    if movie == "Kramer vs. Kramer":
        return u"Kramer Vs. Kramer"
        
    if movie == "Scream":
        return u"Scream I"
    if movie == "Scream 2":
        return u"Scream II"
    if movie == "Scream 3":
        return u"Scream III"
    if movie == "Scream 4":
        return u"Scream IV"
        
    if movie == "Blade I":
        return u"Blade"
    if movie == "Blade II":
        return u"Blade 2"
    if movie == "Blade III":
        return u"Blade 3"
        
    if movie == "BUtterfield 8":
        return u"Butterfield 8"
    if movie == "Chico And Rita":
        return u"Chico Y Rita"
    if movie == "Fanny And Alexander":
        return u"Fanny And Alexander (Fanny Och Alexander)"
    if movie == "Aruitemo Aruitemo (Still Walking)":
        return u"Still Walking (Aruitemo Aruitemo)"
    if movie == "Frost/Nixon":
        return u"Frost Nixon"
    if movie == "Face/Off":
        return u"Face Off"

    if movie == "Hellboy":
        return u"Hellboy I"
    if movie == "Hellboy II: The Golden Army (Hellboy 2)":
        return u"Hellboy II The Golden Army"
    if movie == "Hellboy II: The Golden Army":
        return u"Hellboy II The Golden Army"
        
    if movie == "Spy Kids":
        return u"Spy Kids 1"
    if movie == "Spy Kids 2: The Island Of Lost Dreams":
        return u"Spy Kids 2 The Island Of Lost Dreams"
    if movie == "Spy Kids 3D: Game Over":
        return u"Spy Kids 3 Game Over"
    if movie == "Spy Kids 3: Game Over":
        return u"Spy Kids 3 Game Over"
    if movie == "Spy Kids: All The Time In The World":
        return u"Spy Kids 4 All The Time In The World"
        
    if movie == "Back To The Future" or movie == "Back to the Future":
        return u"Back To The Future I"
    if movie == "Back To The Future Part II" or movie == "Back To The Future II":
        return u"Back To The Future II"
    if movie == "Back To The Future Part III" or movie == "Back To The Future III":
        return u"Back To The Future III"
        
    if movie == "John Wick Chapter Two":
        return "John Wick Chapter 2"
    if movie == "La Cage aux Folles":
        return u"La Cage Aux Folles"
    if movie == "...And Justice For All":
        return u"And Justice For All"
    if movie == "Days Of Summer":
        return u"500 Days Of Summer"
    if movie == "Robocop":
        return u"RoboCop"
    if movie == "Big Mommas: Like Father, Like Son":
        return u"Big Momma's Like Father, Like Son"
    if movie == "The Final Destination":
        return u"Final Destination 4 The Final Destination"
    if movie.find("Confessions Of A Marriage Counselor") != -1:
        return u"Temptation Confessions Of A Marriage Counselor"
    if movie.find("Born Into Brothels") != -1:
        return u"Born Into Brothels"
    if movie == "Love & Mercy":
        return u"Love And Mercy"
    
    if movie == "Tyler Perry's Good Deeds":
        return u"Good Deeds"
    if movie == "Tyler Perry's The Family That Preys":
        return u"The Family That Preys"
    if movie == "Tyler Perry's The Single Moms Club":
        return u"The Single Moms Club"
    if movie == "Tyler Perry's Madea's Big Happy Family":
        return u"Madea's Big Happy Family"
    if movie == "Tyler Perry's Madea's Family Reunion":
        return u"Madea's Family Reunion"
    if movie == "Tyler Perry's Madea's Witness Protection":
        return u"Madea's Witness Protection"
    if movie == "Tyler Perry's Why Did I Get Married Too?":
        return u"Why Did I Get Married Too?"
    if movie == "Tyler Perry's I Can Do Bad All By Myself":
        return u"I Can Do Bad All By Myself"
    if movie == "Tyler Perry's Madea Goes To Jail":
        return u"Madea Goes To Jail"
    if movie == "Tyler Perry's Why Did I Get Married?":
        return u"Why Did I Get Married?"
    if movie == "Tyler Perry's Diary Of A Mad Black Woman":
        return u"Diary Of A Mad Black Woman"
    if movie == "Tyler Perry's A Madea Christmas":
        return u"A Madea Christmas"
    if movie == "Tyler Perry's Meet The Browns":
        return u"Meet The Browns"
    if movie == "Tyler Perry's Daddy's Little Girls":
        return u"Daddy's Little Girls"    
    
    if movie == "My Life As A Zucchini":
        return u"My Life As A Zucchini (Ma vie de Courgette)"
    if movie == "The Hunger Games: Mockingjay - Part 1":
        return u"The Hunger Games Mockingjay Part 1"
    if movie == "The Hunger Games: Mockingjay - Part 2":
        return u"The Hunger Games Mockingjay Part 2"
    if movie == "Fog Of War Eleven Lessons From The Life Of Robert S. Mcnamara":
        return u"Fog Of War Eleven Lessons From The Life Of Robert S Mcnamara"
    if movie == "The Truth About Cats & Dogs":
        return u"The Truth About Cats And Dogs"
        
    if movie == "Mission: Impossible":
        return u"Mission Impossible 1"
    if movie == "Mission Impossible II":
        return u"Mission Impossible 2"
    if movie == "Mission: Impossible II":
        return u"Mission Impossible 2"
    if movie == "Mission: Impossible 2":
        return u"Mission Impossible 2"
    if movie == "Mission Impossible III":
        return u"Mission Impossible 3"
    if movie == "Mission: Impossible III":
        return u"Mission Impossible 3"
    if movie == "Mission: Impossible - Ghost Protocol":
        return u"Mission Impossible 4 Ghost Protocol"
    if movie == "Mission: Impossible 4 Ghost Protocol":
        return u"Mission Impossible 4 Ghost Protocol"
    if movie == "Mission: Impossible Ghost Protocol":
        return u"Mission Impossible 4 Ghost Protocol"
    if movie == "Mission: Impossible - Rogue Nation":
        return u"Mission Impossible 5 Rogue Nation"
    if movie == "Mission: Impossible 5 Rogue Nation":
        return u"Mission Impossible 5 Rogue Nation"
    if movie == "Mission: Impossible Rogue Nation":
        return u"Mission Impossible 5 Rogue Nation"
        
    if movie == "My Bloody Valentine 3-D":
        return u"My Bloody Valentine"
        
    if movie == "Batman v Superman: Dawn Of Justice":
        return u"Batman V Superman Dawn Of Justice"
    if movie == "Batman V Superman: Dawn Of Justice":
        return u"Batman V Superman Dawn Of Justice"
        
    if movie == "Lethal Weapon":
        return u"Lethal Weapon 1"
        
    if movie == u"Le goût des autres (The Taste Of Others)":
        return u"The Taste Of Others (Le goût des autres)"
    if movie.find("The Taste Of Others") != -1:
        return u"The Taste Of Others (Le goût des autres)"
        
    if movie == "Aliens Vs. Predator - Requiem":
        return u"Aliens Vs. Predator Requiem"
    if movie == "Alien Resurrection":
        return u"Alien 4 Resurrection"
        
    if movie == "Hustle And Flow":
        return u"Hustle & Flow"
    if movie == "Pride And Prejudice":
        return u"Pride & Prejudice"
    if movie == "sex, lies And videotape":
        return u"Sex, Lies And Videotape"
    if movie == "3:10 To Yuma" or movie == "3:10 to Yuma":
        return u"3 10 To Yuma"
    if movie == "American Reunion":
        return u"American Pie American Reunion"
    if movie == "Les Miserables":
        return u"Les Misérables"
        
    if movie == "Resident Evil":
        return u"Resident Evil 1"
    if movie == "Resident Evil Apocalypse":
        return u"Resident Evil 2 Apocalypse"
    if movie == "Resident Evil: Apocalypse":
        return u"Resident Evil 2 Apocalypse"
    if movie == "Resident Evil Extinction":
        return u"Resident Evil 3 Extinction"
    if movie == "Resident Evil: Extinction":
        return u"Resident Evil 3 Extinction"
    if movie == "Resident Evil Afterlife":
        return u"Resident Evil 4 Afterlife"
    if movie == "Resident Evil: Afterlife":
        return u"Resident Evil 4 Afterlife"
    if movie == "Resident Evil Retribution":
        return u"Resident Evil 5 Retribution"
    if movie == "Resident Evil: Retribution":
        return u"Resident Evil 5 Retribution"
    if movie == "Resident Evil The Final Chapter":
        return u"Resident Evil 6 The Final Chapter"
    if movie == "Resident Evil: The Final Chapter":
        return u"Resident Evil 6 The Final Chapter"
    
    if movie == "Il Postino: The Postman":
        return u"Il Postino (The Postman)"
    if movie == "Victor/Victoria":
        return u"Victor Victoria"
    if movie == "Scary Movie 3":
        return u"Scary Movie 3 5"
    if movie == "As Above/So Below":
        return u"As Above, So Below"
    if movie == "Dr. Seuss' The Lorax":
        return u"The Lorax"
    if movie == "9":
        return u"Nine"
    if movie == "Mrs Brown":
        return u"Mrs. Brown"
    if movie == "The Nut Job 2: Nutty By Nature":
        return u"The Nut Job 2 Nutty By Nature"
    if movie == "Transformers: The Last Knight":
        return u"Transformers The Last Knight"
    if movie == "John Wick: Chapter Two":
        return u"John Wick Chapter Two"
    if movie.find("Diary Of A Wimpy Kid: ") != -1:
        return movie.replace("Diary Of A Wimpy Kid: ", "Diary Of A Wimpy Kid ")
    if movie.find("Annabelle: ") != -1:
        return movie.replace("Annabelle: ", "Annabelle ")
    if movie.find("Seymour: ") != -1:
        return movie.replace("Seymour: ", "Seymour ")
    if movie == "The Lady In Number 6: Music Saved My Life":
        return u"The Lady In Number 6 Music Saved My Life"
    if movie == "Everyday Sunshine: The Story Of Fishbone":
        return u"Everyday Sunshine The Story Of Fishbone"
    if movie == "Star Wars: The Clone Wars":
        return u"Star Wars The Clone Wars"
    if movie == "Barnyard: The Original Party Animals":
        return u"Barnyard The Original Party Animals"
    if movie == "Garfield: A Tail Of Two Kitties":
        return u"Garfield A Tail Of Two Kitties"
    if movie == "The Moon And The Son: An Imagined Conversation":
        return u"The Moon And The Son An Imagined Conversation"
    if movie == "A Note Of Triumph: The Golden Age Of Norman Corwin":
        return u"A Note Of Triumph The Golden Age Of Norman Corwin"
    if movie == "Born Into Brothels: Calcutta's Red Light Kids":
        return u"Born Into Brothels Calcutta's Red Light Kids"
    if movie == "Mighty Times: The Children's March":
        return u"Mighty Times The Children's March"
    if movie == "Barbershop 2: Back In Business":
        return u"Barbershop 2 Back In Business"
    if movie == "Looney Tunes: Back In Action":
        return u"Looney Tunes Back In Action"
    if movie == "Exorcist: The Beginning":
        return u"Exorcist The Beginning"
    if movie == "The Fog Of War: Eleven Lessons From The Life Of Robert S. McNamara":
        return u"The Fog Of War Eleven Lessons From The Life Of Robert S. McNamara"
    if movie == "Jackass: The Movie":
        return u"Jackass The Movie"
    if movie == "Into The Arms Of Strangers: Stories Of The Kindertransport":
        return u"Into The Arms Of Strangers Stories Of The Kindertransport"
    if movie == "Pokemon: The Movie 2000":
        return u"Pokemon The Movie 2000"
        
    if movie == "The Lost World Jurassic Park":
        return u"Jurassic Park II The Lost World"
    if movie == "The Lost World: Jurassic Park":
        return u"Jurassic Park II The Lost World"
    if movie == "The Lost World" and int(year) == 1997:
        return u"Jurassic Park II The Lost World"
    if movie == "2001: A Space Odyssey":
        return u"2001 A Space Odyssey"
        
    if movie == "Airplane II: The Sequel":
        return u"Airplane II The Sequel"
    if movie == "Porky's II: The Next Day":
        return u"Porky's II The Next Day"
        
    if movie == "Star Trek II: The Wrath Of Khan":
        return u"Star Trek II The Wrath Of Khan"
    if movie == "Star Trek III: The Search For Spock":
        return u"Star Trek III The Search For Spock"
    if movie == "Star Trek IV: The Voyage Home":
        return u"Star Trek IV The Voyage Home"
    if movie == "Star Trek V: The Final Frontier":
        return u"Star Trek V The Final Frontier"
    if movie == "Star Trek VI: The Undiscovered Country":
        return u"Star Trek VI The Undiscovered Country"
        
    if movie == "Star Trek" and int(year) > 2000:
        return u"Star Trek The Future Begins"
    if movie == "Star Trek" and int(year) < 2000:
        return u"Star Trek I"
        
    if movie == "Star Trek: Generations":
        return u"Star Trek Generations"
    if movie == "Star Trek: First Contact":
        return u"Star Trek First Contact"
    if movie == "Star Trek: Insurrection":
        return u"Star Trek Insurrection"
    if movie == "Star Trek: Nemesis":
        return u"Star Trek Nemesis"

    if movie == "Rambo: First Blood Part II":
        return u"Rambo First Blood Part II"
    if movie == "Poltergeist II: The Other Side":
        return u"Poltergeist II The Other Side"
        
    if movie == "Police Academy 2: Their First Assignment":
        return u"Police Academy 2 Their First Assignment"
    if movie == "Police Academy 3: Back In Training":
        return u"Police Academy 3 Back In Training"
    if movie == "Police Academy 4: Citizens On Patrol":
        return u"Police Academy 4 Citizens On Patrol"
    if movie == "Police Academy 5: Assignment: Miami Beach":
        return u"Police Academy 5 Assignment Miami Beach"
    if movie == "Police Academy 6: City Under Siege":
        return u"Police Academy 6 City Under Siege"
        
    if movie == "Tucker: The Man And His Dream":
        return u"Tucker The Man And His Dream"
    if movie == "Gremlins 2: The New Batch":
        return u"Gremlins 2 The New Batch"
        
    if movie == "Terminator 2: Judgment Day":
        return u"Terminator 2 Judgment Day"
    if movie == "Terminator 3: Rise Of The Machines":
        return u"Terminator 3 Rise Of The Machines"
    if movie == "Terminator: Genisys":
        return u"Terminator Genisys"

    if movie == "Die Hard 2: Die Harder":
        return u"Die Hard 2 Die Harder"
    if movie == "Die Hard: With A Vengeance":
        return u"Die Hard 3 Die Hard With A Vengeance"
    if movie == "Live Free Or Die Hard":
        return u"Die Hard 4 Live Free Or Die Hard"
    if movie == "A Good Day To Die Hard":
        return u"Die Hard 5 A Good Day To Die Hard"
        
    if movie == "Robin Hood: Prince Of Thieves":
        return u"Robin Hood Prince Of Thieves"
    if movie == "Home Alone 2: Lost In New York":
        return u"Home Alone 2 Lost In New York"
    if movie == "Stop! Or My Mom Will Shoot!":
        return u"Stop! Or My Mom Will Shoot"
    if movie == "Sister Act 2: Back In The Habit":
        return u"Sister Act 2 Back In The Habit"
    if movie == "Dragon: The Bruce Lee Story":
        return u"Dragon The Bruce Lee Story"
    if movie == "Ace Ventura: Pet Detective":
        return u"Ace Ventura Pet Detective"
    if movie == "The Crow: City Of Angels":
        return u"The Crow 2 City Of Angels"
            
    if movie == "Saw":
        return u"Saw I"
    if movie == "Saw 3D":
        return u"Saw VII"
    if movie == "Saw 7":
        return u"Saw VII"
    
    if movie == "Halloween II":
        return u"Halloween 2"
    if movie == "Halloween III: Season Of The Witch":
        return u"Halloween 3 Season Of The Witch"
    if movie == "Halloween 4: The Return Of Michael Myers":
        return u"Halloween 4 The Return Of Michael Myers"
    if movie == "Halloween: The Curse Of Michael Myers":
        return u"Halloween 6 The Curse Of Michael Myers"
    if movie == "Halloween: H20":
        return u"Halloween 7 H20 20 Years Later"
    if movie == "Halloween: Resurrection":
        return u"Halloween 8 Resurrection"

    if movie == "How To be A Latin Lover":
        return u"How To Be A Latin Lover"
    if movie == "Rivers And Tides: Andy Goldsworthy Working With Time":
        return u"Rivers And Tides Andy Goldsworthy Working With Time"
    if movie == "Ace Ventura: When Nature Calls":
        return u"Ace Ventura When Nature Calls"
    if movie == "Under Siege 2: Dark Territory":
        return u"Under Siege 2 Dark Territory"
    if movie == "Homeward Bound II: Lost In San Francisco":
        return u"Homeward Bound II Lost In San Francisco"
    if movie == "Mortal Kombat: Annihilation":
        return u"Mortal Kombat Annihilation"
    if movie == "Speed 2: Cruise Control":
        return u"Speed 2 Cruise Control"
    if movie == "Beverly Hills Ninja":
        return u"Beverly Hills Ninja "
    if movie == "Austin Powers: International Man Of Mystery":
        return u"Austin Powers International Man Of Mystery"
    if movie == "Ever After: A Cinderella Story":
        return u"Ever After A Cinderella Story"
    if movie == "Deuce Bigalow: Male Gigolo":
        return u"Deuce Bigalow Male Gigolo"
    if movie == "Austin Powers: The Spy Who Shagged Me":
        return u"Austin Powers The Spy Who Shagged Me"
    if movie == "Rugrats In Paris: The Movie":
        return u"Rugrats In Paris The Movie"
    if movie == "The Nutty Professor II: The Klumps":
        return u"The Nutty Professor II The Klumps"
    if movie == "Jimmy Neutron: Boy Genius":
        return u"Jimmy Neutron Boy Genius"
    if movie == "Atlantis: The Lost Empire":
        return u"Atlantis The Lost Empire"
    if movie == "Final Fantasy: The Spirits Within":
        return u"Final Fantasy The Spirits Within"
    if movie == "Spirit: Stallion Of The Cimarron":
        return u"Spirit Stallion Of The Cimarron"
    if movie == "Star Wars: Episode II Attack Of The Clones":
        return u"Star Wars Episode II Attack Of The Clones"
    if movie == "K-19: The Widowmaker":
        return u"K-19 The Widowmaker"
    if movie == "The Crocodile Hunter: Collision Course":
        return u"The Crocodile Hunter Collision Course"
    if movie == "Charlie's Angels: Full Throttle":
        return u"Charlie's Angels Full Throttle"
    if movie == "Dickie Roberts: Former Child Star":
        return u"Dickie Roberts Former Child Star"
    if movie == "Dumb And Dumberer: When Harry Met Lloyd":
        return u"Dumb And Dumberer When Harry Met Lloyd"
    if movie == "Legally Blonde 2: Red, White And Blonde":
        return u"Legally Blonde 2 Red, White And Blonde"
    if movie == "DodgeBall: A True Underdog Story":
        return u"DodgeBall A True Underdog Story"
    if movie == "The Princess Diaries 2: Royal Engagement":
        return u"The Princess Diaries 2 Royal Engagement"
    if movie == "Agent Cody Banks 2: Destination London":
        return u"Agent Cody Banks 2 Destination London"
    if movie == "Scooby-Doo 2: Monsters Unleashed":
        return u"Scooby-Doo 2 Monsters Unleashed"
    if movie == "Anacondas: The Hunt For The Blood Orchid":
        return u"Anacondas The Hunt For The Blood Orchid"
    if movie == "Anchorman: The Legend Of Ron Burgundy":
        return u"Anchorman The Legend Of Ron Burgundy"
    if movie == "Garfield: The Movie":
        return u"Garfield The Movie"
    if movie == "XXX: State Of The Union":
        return u"XXX State Of The Union"
    if movie == "Dreamer: Inspired By A True Story":
        return u"Dreamer Inspired By A True Story"
    if movie == "Herbie: Fully Loaded":
        return u"Herbie Fully Loaded"
    if movie == "Star Wars: Episode III Revenge Of The Sith":
        return u"Star Wars Episode III Revenge Of The Sith"
    if movie == "Deuce Bigalow: European Gigolo":
        return u"Deuce Bigalow European Gigolo"
    if movie == "Miss Congeniality 2: Armed And Fabulous":
        return u"Miss Congeniality 2 Armed And Fabulous"
    if movie == "Jackass: Number Two":
        return u"Jackass Number Two"
    if movie == "The Fast And The Furious: Tokyo Drift":
        return u"The Fast And The Furious Tokyo Drift"
    if movie == "Talladega Nights: The Ballad Of Ricky Bobby":
        return u"Talladega Nights The Ballad Of Ricky Bobby"
    if movie == "Underworld: Evolution":
        return u"Underworld Evolution"
    if movie == "The Texas Chainsaw Massacre: The Beginning":
        return u"The Texas Chainsaw Massacre The Beginning"
    if movie == "X-Men: The Last Stand":
        return u"X-Men The Last Stand"
    if movie == "The Santa Clause 3: The Escape Clause":
        return u"The Santa Clause 3 The Escape Clause"
    if movie == "Ice Age: The Meltdown":
        return u"Ice Age The Meltdown"
    if movie == "Elizabeth: The Golden Age":
        return u"Elizabeth The Golden Age"
    if movie == "Fantastic Four: Rise Of The Silver Surfer":
        return u"Fantastic Four Rise Of The Silver Surfer"
    if movie == "National Treasure: Book Of Secrets":
        return u"National Treasure Book Of Secrets"
    if movie == "The X-Files: I Want To Believe":
        return u"The X-Files I Want To Believe"
    if movie == "Madagascar: Escape 2 Africa":
        return u"Madagascar Escape 2 Africa"
    if movie == "The Mummy: Tomb Of The Dragon Emperor":
        return u"The Mummy Tomb Of The Dragon Emperor"
    if movie == "Ice Age: Dawn Of The Dinosaurs":
        return u"Ice Age Dawn Of The Dinosaurs"
    if movie == "G.I. Joe: The Rise Of Cobra":
        return u"G.I. Joe The Rise Of Cobra"
    if movie == "X-Men Origins: Wolverine":
        return u"X-Men Origins Wolverine"
    if movie == "Underworld: Rise Of The Lycans":
        return u"Underworld Rise Of The Lycans"
    if movie == "Wall Street: Money Never Sleeps":
        return u"Wall Street Money Never Sleeps"
    if movie == "Cats & Dogs: The Revenge Of Kitty Galore":
        return u"Cats & Dogs The Revenge Of Kitty Galore"
    if movie == "Wallace & Gromit In A Close Shave":
        return u"Wallace And Gromit In A Close Shave"
    if movie == "Wallace & Gromit: The Curse Of The Were-Rabbit":
        return u"Wallace And Gromit The Curse Of The Were-Rabbit"
    if movie == "Prince Of Persia: The Sands Of Time":
        return u"Prince Of Persia The Sands Of Time"
    if movie == "Battle: Los Angeles":
        return u"Battle Los Angeles"
    if movie == "Justin Bieber: Never Say Never":
        return u"Justin Bieber Never Say Never"
    if movie == "Ice Age: Continental Drift":
        return u"Ice Age Continental Drift"
    if movie == "Katy Perry: Part Of Me":
        return u"Katy Perry Part Of Me"
    if movie == "Journey 2: The Mysterious Island":
        return u"Journey 2 The Mysterious Island"
    if movie == "Madagascar 3: Europe's Most Wanted":
        return u"Madagascar 3 Europe's Most Wanted"
    if movie == "Ghost Rider: Spirit Of Vengeance":
        return u"Ghost Rider Spirit Of Vengeance"
    if movie == "Abraham Lincoln: Vampire Hunter":
        return u"Abraham Lincoln Vampire Hunter"
    if movie == "August: Osage County":
        return u"August Osage County"
    if movie == "Thor: The Dark World":
        return u"Thor The Dark World"
    if movie == "The Hunger Games: Catching Fire":
        return u"The Hunger Games Catching Fire"
    if movie == "The Mortal Instruments: City Of Bones":
        return u"The Mortal Instruments City Of Bones"
    if movie == "Kevin Hart: Let Me Explain":
        return u"Kevin Hart Let Me Explain"
    if movie == "One Direction: This Is Us":
        return u"One Direction This Is Us"
    if movie == "Jackass Presents: Bad Grandpa":
        return u"Jackass Presents Bad Grandpa"
    if movie == "G.I. Joe: Retaliation":
        return u"G.I. Joe Retaliation"
    if movie == "Anchorman 2: The Legend Continues":
        return u"Anchorman 2 The Legend Continues"
    if movie == "Planes: Fire & Rescue":
        return u"Planes Fire & Rescue"
    if movie == "Paranormal Activity: The Marked Ones":
        return u"Paranormal Activity The Marked Ones"
    if movie == "Jack Ryan: Shadow Recruit":
        return u"Jack Ryan Shadow Recruit"
    if movie == "X-Men: Days Of Future Past":
        return u"X-Men Days Of Future Past"
    if movie == "The SpongeBob Movie: Sponge Out Of Water":
        return u"The SpongeBob Movie Sponge Out Of Water"
    if movie == "The Woman In Black 2: Angel Of Death":
        return u"The Woman In Black 2 Angel Of Death"
    if movie == "Kingsman: The Secret Service":
        return u"Kingsman The Secret Service"
    if movie == "Avengers: Age Of Ultron":
        return u"Avengers Age Of Ultron"
    if movie == "The Huntsman: Winter's War":
        return u"The Huntsman Winter's War"
    if movie == "Ice Age: Collision Course":
        return u"Ice Age Collision Course"
    if movie == "Kevin Hart: What Now?":
        return u"Kevin Hart What Now?"
    if movie == "Mechanic: Resurrection":
        return u"Mechanic Resurrection"
    if movie == "Neighbors 2: Sorority Rising":
        return u"Neighbors 2 Sorority Rising"
    if movie == "13 Hours: The Secret Soldiers Of Benghazi":
        return u"13 Hours The Secret Soldiers Of Benghazi"
    if movie == "Batman V Superman: Dawn Of Justice":
        return u"Batman V Superman Dawn Of Justice"
    if movie == "Independence Day: Resurgence":
        return u"Independence Day Resurgence"
    if movie == "Barbershop: The Next Cut":
        return u"Barbershop The Next Cut"
    if movie == "Ferngully: The Last Rainforest":
        return u"Ferngully The Last Rainforest"
    if movie == "Babe: Pig In The City":
        return u"Babe Pig In The City"

    if movie == "The Purge: Election Year":
        return u"The Purge Election Year"
    if movie == "The Purge: Anarchy":
        return u"The Purge Anarchy"

    if movie == "Mad Max: Fury Road":
        return u"Mad Max Fury Road"
    if movie == "Mad Max Beyond Thunderdome":
        return u"Mad Max 3 Beyond Thunderdome"
    if movie == "The Road Warrior":
        return u"Mad Max 2 The Road Warrior"
    if movie == "Mad Max 2: The Road Warrior":
        return u"Mad Max 2 The Road Warrior"

    if movie == "Highlander 2: The Quickening":
        return u"Highlander 2 The Quickening"
    if movie == "Highlander: Endgame":
        return u"Highlander Endgame"
    if movie == "Highlander 3: The Final Dimension":
        return u"Highlander 3 The Final Dimension"

    if movie == "The Lord Of The Flies":
        return u"Lord Of The Flies"
    if movie == "Larry The Cable Guy: Health Inspector":
        return u"Larry The Cable Guy Health Inspector"
    if movie == "The Water Horse: Legend Of The Deep":
        return u"The Water Horse Legend Of The Deep"
    if movie == "Paranormal Activity: The Ghost Dimension":
        return u"Paranormal Activity The Ghost Dimension"
    if movie == "Middle School: The Worst Years Of My Life":
        return u"Middle School The Worst Years Of My Life"

    if movie == "How To Make an American Quilt ":
        return u"How To Make An American Quilt"
        
    if movie == "X2: X-Men United":
        return u"X2 X-Men United"
    if movie == "Reno 911!: Miami":
        return u"Reno 911! Miami"
    if movie == "Walk Hard: The Dewey Cox Story":
        return u"Walk Hard The Dewey Cox Story"
    if movie == "Step Up 3-D":
        return u"Step Up 3D"
    if movie == "Jonas Brothers: The 3D Concert Experience":
        return u"Jonas Brothers The 3D Concert Experience"
    if movie == "George A. Romero's Land Of The Dead":
        return u"Land Of The Dead"
    if movie == "crazy/beautiful":
        return u"Crazy, Beautiful"
    if movie == "The Titan: Story Of Michelangelo":
        return u"The Titan Story Of Michelangelo"
    if movie == "Robert Frost: A Lover's Quarrel With The World":
        return u"Robert Frost A Lover's Quarrel With The World"
    if movie == "Dr. Strangelove or: How I Learned To Stop Worrying And Love The Bomb":
        return u"Dr. Strangelove or How I Learned To Stop Worrying And Love The Bomb"
    if movie == "Casals Conducts: 1964":
        return u"Casals Conducts 1964"
    if movie == "The Dot And The Line: A Romance In Lower Mathematics":
        return u"The Dot And The Line A Romance In Lower Mathematics"
    if movie == "Princeton: A Search For Answers":
        return u"Princeton A Search For Answers"
    if movie == "Paul Robeson: Tribute To an Artist":
        return u"Paul Robeson Tribute To an Artist"
    if movie == "Karl Hess: Toward Liberty":
        return u"Karl Hess Toward Liberty"
    if movie == "From Mao To Mozart: Isaac Stern In China":
        return u"From Mao To Mozart Isaac Stern In China"
    if movie == "Star Wars: Episode V The Empire Strikes Back":
        return u"Star Wars Episode V The Empire Strikes Back"
    if movie == "E.T.: The Extra-Terrestrial":
        return u"E.T. The Extra-Terrestrial"
    if movie == "Richard Pryor: Live On The Sunset Strip":
        return u"Richard Pryor Live On The Sunset Strip"
    if movie == "Pink Floyd: The Wall":
        return u"Pink Floyd The Wall"
    if movie == "Amityville II: The Possession":
        return u"Amityville II The Possession"
    if movie == "Twilight Zone: The Movie":
        return u"Twilight Zone The Movie"
    if movie == "Spacehunter: Adventures In The Forbidden Zone":
        return u"Spacehunter Adventures In The Forbidden Zone"
    if movie == "Richard Pryor: Here And Now":
        return u"Richard Pryor Here And Now"
    if movie == "Greystoke: The Legend Of Tarzan, Lord Of The Apes":
        return u"Greystoke The Legend Of Tarzan, Lord Of The Apes"
    if movie == "Greystoke: The Legend Of Tarzan":
        return u"Greystoke The Legend Of Tarzan"
    if movie == "Witness To War: Dr. Charlie Clements":
        return u"Witness To War Dr. Charlie Clements"
    if movie == "Santa Claus: The Movie":
        return u"Santa Claus The Movie"
    if movie == "Breakin' 2: Electric Boogaloo":
        return u"Breakin' 2 Electric Boogaloo"
    if movie == "Remo Williams: The Adventure Begins":
        return u"Remo Williams The Adventure Begins"
    if movie == "Baby: Secret Of The Lost Legend":
        return u"Baby Secret Of The Lost Legend"
    if movie == "Artie Shaw: Time Is All You've Got":
        return u"Artie Shaw Time Is All You've Got"
    if movie == "Gaby: A True Story":
        return u"Gaby A True Story"
    if movie == "The Ten-Year Lunch: The Wit And Legend Of The Algonquin Round Table":
        return u"The Ten-Year Lunch The Wit And Legend Of The Algonquin Round Table"
    if movie == "Revenge Of The Nerds II: Nerds In Paradise":
        return u"Revenge Of The Nerds II Nerds In Paradise"
    if movie == "Jaws IV: The Revenge":
        return u"Jaws IV The Revenge"
    if movie == "Superman IV: The Quest For Peace":
        return u"Superman IV The Quest For Peace"
    if movie == "Hôtel Terminus: The Life And Times Of Klaus Barbie":
        return u"Hôtel Terminus The Life And Times Of Klaus Barbie"
        
    if movie == "The Naked Gun: From The Files Of Police Squad!":
        return u"The Naked Gun"
    if movie == "The Naked Gun 2 1 2: The Smell Of Fear":
        return u"The Naked Gun 2 1 2 The Smell Of Fear"
    if movie == "The Naked Gun 2 1/2: The Smell Of Fear" or movie == "The Naked Gun 2 1/2: The Smell of Fear":
        return u"The Naked Gun 2 1 2 The Smell Of Fear"
    if movie == "The Naked Gun 33 1/3: The Final Insult":
        return u"The Naked Gun 33 1 3 The Final Insult"
    if movie == "The Naked Gun 33 1 3: The Final Insult":
        return u"The Naked Gun 33 1 3 The Final Insult"
        
    if movie == "MIB 3":
        return u"Men In Black 3"

    if movie == "Children Of The Corn":
        return u"Children Of The Corn I"
    if movie == "Cocoon: The Return":
        return u"Cocoon The Return"
    if movie == "Arthur 2: On The Rocks":
        return u"Arthur 2 On The Rocks"
    if movie == "Common Threads: Stories From The Quilt":
        return u"Common Threads Stories From The Quilt"
    if movie == "Tales From The Darkside: The Movie":
        return u"Tales From The Darkside The Movie"
    if movie == "Jetsons: The Movie":
        return u"Jetsons The Movie"
    if movie == "Duck Tales: The Movie":
        return u"Duck Tales The Movie"
    if movie == "Deadly Deception: General Electric, Nuclear Weapons And Our Environment":
        return u"Deadly Deception General Electric, Nuclear Weapons And Our Environment"
    if movie == "An American Tail: Fievel Goes West":
        return u"An American Tail Fievel Goes West"
    if movie == "Madonna: Truth Or Dare":
        return u"Madonna Truth Or Dare"
    if movie == "I Am A Promise: The Children Of Stanton Elementary School":
        return u"I Am A Promise The Children Of Stanton Elementary School"
    if movie == "Homeward Bound: The Incredible Journey":
        return u"Homeward Bound The Incredible Journey"
    if movie == "Robin Hood: Men In Tights":
        return u"Robin Hood Men In Tights"
    if movie == "Geronimo: An American Legend":
        return u"Geronimo An American Legend"
    if movie == "Maya Lin: A Strong Clear Vision":
        return u"Maya Lin A Strong Clear Vision"
    if movie == "City Slickers II: The Legend Of Curly's Gold":
        return u"City Slickers II The Legend Of Curly's Gold"
    if movie == "Free Willy 2: The Adventure Home":
        return u"Free Willy 2 The Adventure Home"
    if movie == "Candyman: Farewell To The Flesh":
        return u"Candyman Farewell To The Flesh"
    if movie == "Fairy Tale: A True Story":
        return u"Fairy Tale A True Story"
    if movie == "Pokemon: The First Movie":
        return u"Pokemon The First Movie"
    if movie == "The Rage: Carrie 2":
        return u"The Rage Carrie 2"
    if movie == "The Messenger: The Story Of Joan Of Arc":
        return u"The Messenger The Story Of Joan Of Arc"
    if movie == "Universal Soldier: The Return":
        return u"Universal Soldier The Return"
    if movie == "Mr. Death: The Rise And Fall Of Fred A. Leuchter, Jr.":
        return u"Mr. Death The Rise And Fall Of Fred A. Leuchter, Jr."
    if movie == "Urban Legends: Final Cut":
        return u"Urban Legends Final Cut"
    if movie == "Recess: School's Out":
        return u"Recess School's Out"
    if movie == "Pokemon 3: The Movie":
        return u"Pokemon 3 The Movie"
    if movie == "Martin Lawrence Live: Runteldat":
        return u"Martin Lawrence Live Runteldat"
    if movie == "Ballistic: Ecks vs. Sever":
        return u"Ballistic Ecks vs. Sever"
    if movie == "Wes Craven Presents: They":
        return u"Wes Craven Presents They"
    if movie == "Lara Croft Tomb Raider 2: The Cradle Of Life":
        return u"Lara Croft Tomb Raider 2 The Cradle Of Life"
    if movie == "Sinbad: Legend Of The Seven Seas":
        return u"Sinbad Legend Of The Seven Seas"
    if movie == "Dirty Dancing: Havana Nights":
        return u"Dirty Dancing Havana Nights"
    if movie == "Wallace And Gromit: The Curse Of The Were-Rabbit":
        return u"Wallace And Gromit The Curse Of The Were-Rabbit"
    if movie == "Pathfinder: Legend Of The Ghost Warrior":
        return u"Pathfinder Legend Of The Ghost Warrior"
    if movie == "Hannah Montana Miley Cyrus: Best Of Both Worlds Concert Tour":
        return u"Hannah Montana Miley Cyrus Best Of Both Worlds Concert Tour"
    if movie == "Kit Kittredge: An American Girl":
        return u"Kit Kittredge An American Girl"
    if movie == "The Goods: Live Hard, Sell Hard":
        return u"The Goods Live Hard, Sell Hard"
    if movie == "Capitalism: A Love Story":
        return u"Capitalism A Love Story"
    if movie == "Cirque du Freak: The Vampire's Assistant":
        return u"Cirque du Freak The Vampire's Assistant"
    if movie == "Crank: High Voltage":
        return u"Crank High Voltage"
    if movie == "Percy Jackson & The Olympians: The Lightning Thief":
        return u"Percy Jackson & The Olympians The Lightning Thief"
    if movie == "Avatar: Special Edition":
        return u"Avatar Special Edition"
    if movie == "The Boondock Saints II: All Saints Day":
        return u"The Boondock Saints II All Saints Day"
    if movie == "X-Men: First Class":
        return u"X-Men First Class"
    if movie == "Silent Hill: Revelation 3D":
        return u"Silent Hill Revelation"
    if movie == "Cirque Du Soleil: Worlds Away":
        return u"Cirque Du Soleil Worlds Away"
    if movie == "Frank Miller's Sin City: A Dame To Kill For":
        return u"Frank Miller's Sin City A Dame To Kill For"
    if movie == "X-Men: Apocalypse":
        return u"X-Men Apocalypse"
    if movie == "Spider-Man: Homecoming":
        return u"Spider-Man Homecoming"
    if movie == "Alien: Covenant":
        return u"Alien Covenant"
    if movie == "Smurfs: The Lost Village":
        return u"Smurfs The Lost Village"
        
    if movie == "Goal! The Dream Begins (Goal!: The Impossible Dream)":
        return u"Goal! The Dream Begins (Goal! The Impossible Dream)"
    
    if movie == "Teenage Mutant Ninja Turtles: Out Of The Shadows":
        return u"Teenage Mutant Ninja Turtles Out Of The Shadows"
    if movie == "Teenage Mutant Ninja Turtles II":
        return u"Teenage Mutant Ninja Turtles II The Secret Of The Ooze"
    if movie == "Teenage Mutant Ninja Turtles: The Movie":
        return u"Teenage Mutant Ninja Turtles The Movie"        
        
    if movie == "Hellraiser III: Hell On Earth":
        return u"Hellraiser 3 Hell On Earth"
    if movie == "Hellbound: Hellraiser II":
        return u"Hellraiser 2 Hellbound"
    if movie == "Hellraiser 4: Bloodline":
        return u"Hellraiser 4 Bloodline"
        
    if movie == "Baahubali 2: The Conclusion":
        return u"Baahubali 2 The Conclusion"
    if movie == "Star Wars: Episode V The Empire Strikes Back":
        return u"Star Wars Episode V The Empire Strikes Back"
    if movie == "Hôtel Terminus: The Life And Times Of Klaus Barbie":
        return u"Hôtel Terminus The Life And Times Of Klaus Barbie"
    if movie == "Hannah Montana Miley Cyrus: Best Of Both Worlds Concert Tour":
        return u"Hannah Montana Miley Cyrus Best Of Both Worlds Concert Tour"
    if movie == "Sunrise: A Song Of Two Humans":
        return u"Sunrise A Song Of Two Humans"
    if movie == "Missing In Action II: The Beginning":
        return u"Missing In Action II The Beginning"
    if movie == "Evil Dead 2: Dead By Dawn":
        return u"Evil Dead 2 Dead By Dawn"
    if movie == "Hôtel Terminus: The Life And Times Of Klaus Barbie":
        return u"Hôtel Terminus The Life And Times Of Klaus Barbie"
    if movie == "U2: Rattle And Hum":
        return u"U2 Rattle And Hum"
        
        
    if movie == "Far From Home: The Adventures Of Yellow Dog":
        return u"Far From Home The Adventures Of Yellow Dog"
    if movie == "Dracula: Dead And Loving It":
        return u"Dracula Dead And Loving It"
    if movie == "Digimon: The Movie":
        return u"Digimon The Movie"
    if movie == "Lagaan: Once Upon A Time In India":
        return u"Lagaan Once Upon A Time In India"
    if movie == "Chavez: Inside The Coup":
        return u"Chavez Inside The Coup"
    if movie == "Super Babies: Baby Geniuses 2":
        return u"Super Babies Baby Geniuses 2"
    if movie == "End Of The Century: The Story Of The Ramones":
        return u"End Of The Century The Story Of The Ramones"
    if movie == "Enron: The Smartest Guys In The Room":
        return u"Enron The Smartest Guys In The Room"
    if movie == "Tenacious D in: The Pick Of Destiny":
        return u"Tenacious D in The Pick Of Destiny"
    if movie == "The Seeker: The Dark Is Rising":
        return u"The Seeker The Dark Is Rising"
    if movie == "Code Name: The Cleaner":
        return u"Code Name The Cleaner"
    if movie == "Burma VJ: Reporter i et Lukket Land (Burma VJ: Reporting From A Closed Country)":
        return u"Burma VJ Reporter i et Lukket Land (Burma VJ Reporting From A Closed Country)"
    if movie == "Street Fighter: The Legend Of Chun-Li":
        return u"Street Fighter The Legend Of Chun-Li"
    if movie == "Being Elmo: A Puppeteer's Journey":
        return u"Being Elmo A Puppeteer's Journey"
    if movie == "Mea Maxima Culpa: Silence In The House Of God":
        return u"Mea Maxima Culpa Silence In The House Of God"
    if movie == "Ai Weiwei: Never Sorry":
        return u"Ai Weiwei Never Sorry"
    if movie == "Marina Abramovic: The Artist Is Present":
        return u"Marina Abramovic The Artist Is Present"
    if movie == "Legends Of Oz: Dorothy's Return":
        return u"Legends Of Oz Dorothy's Return"
    if movie == "Mandela: Long Walk To Freedom":
        return u"Mandela Long Walk To Freedom"
    if movie == "Elaine Stritch: Shoot Me":
        return u"Elaine Stritch Shoot Me"
    if movie == "Kurt Cobain: Montage Of Heck":
        return u"Kurt Cobain Montage Of Heck"
    if movie == "Popstar: Never Stop Never Stopping":
        return u"Popstar Never Stop Never Stopping"
    if movie == "The Beatles: Eight Days A Week - The Touring Years":
        return u"The Beatles Eight Days A Week The Touring Years"
    if movie == "The B-Side: Elsa Dorfman's Portrait Photography":
        return u"The B-Side Elsa Dorfman's Portrait Photography"
    if movie == "Nosferatu: Phantom der Nacht (Nosferatu The Vampyre)":
        return u"Nosferatu Phantom der Nacht (Nosferatu The Vampyre)"
    if movie == "Star Wars: Episode V - The Empire Strikes Back":
        return u"Star Wars Episode V The Empire Strikes Back"
    if movie == "Star Wars: Episode VI - Return Of The Jedi":
        return u"Star Wars Episode VI Return Of The Jedi"
    if movie == "Henry: Portrait Of A Serial Killer":
        return u"Henry Portrait Of A Serial Killer"
    if movie == "Hôtel Terminus: The Life And Times Of Klaus Barbie":
        return u"Hôtel Terminus The Life And Times Of Klaus Barbie"
    if movie == "Léon: The Professional":
        return u"Léon The Professional"
    if movie == "Mystery Science Theater 3000: The Movie":
        return u"Mystery Science Theater 3000 The Movie"
    if movie == "South Park: Bigger, Longer & Uncut":
        return u"South Park Bigger, Longer & Uncut"
    if movie == "Exorcist: The Version You've Never Seen":
        return u"Exorcist The Version You've Never Seen"
    if movie == "Code Unknown (Code inconnu: Récit incomplet de divers voyages)":
        return u"Code Unknown (Code inconnu Récit incomplet de divers voyages)"
    if movie == "Kandahar: Le soleil derrière la lune":
        return u"Kandahar Le soleil derrière la lune"
    if movie == "Porn Star: The Legend Of Ron Jeremy":
        return u"Porn Star The Legend Of Ron Jeremy"
    if movie == "Atanarjuat: The Fast Runner (Atanarjuat)":
        return u"Atanarjuat The Fast Runner (Atanarjuat)"
    if movie == "Blind Spot: Hitler's Secretary":
        return u"Blind Spot Hitler's Secretary"
    if movie == "Ultimate X: The Movie":
        return u"Ultimate X The Movie"
    if movie == "Alien: The Director's Cut":
        return u"Alien The Director's Cut"
    if movie == "Dracula: Pages From A Virgin's Diary":
        return u"Dracula Pages From A Virgin's Diary"
    if movie == "Tibet: Cry Of The Snow Lion":
        return u"Tibet Cry Of The Snow Lion"
    if movie == "Zatôichi (The Blind Swordsman: Zatoichi)":
        return u"Zatôichi (The Blind Swordsman Zatoichi)"
    if movie == "Kill Bill: Volume 1":
        return u"Kill Bill Volume 1"
    if movie == "Bukowski: Born into This":
        return u"Bukowski Born into This"
    if movie == "Stoked: The Rise And Fall Of Gator":
        return u"Stoked The Rise And Fall Of Gator"
    if movie == "Tupac: Resurrection":
        return u"Tupac Resurrection"
    if movie == "Fellini: I'm A Born Liar":
        return u"Fellini I'm A Born Liar"
    if movie == "Donnie Darko: The Director's Cut":
        return u"Donnie Darko The Director's Cut"
    if movie == "Going Upriver: The Long War Of John Kerry":
        return u"Going Upriver The Long War Of John Kerry"
    if movie == "Metallica: Some Kind Of Monster":
        return u"Metallica Some Kind Of Monster"
    if movie == "Guerrilla: The Taking Of Patty Hearst":
        return u"Guerrilla The Taking Of Patty Hearst"
    if movie == "Aileen: Life And Death Of A Serial Killer":
        return u"Aileen Life And Death Of A Serial Killer"
    if movie == "Outfoxed: Rupert Murdoch's War On Journalism":
        return u"Outfoxed Rupert Murdoch's War On Journalism"
    if movie == "Kill Bill: Volume 2":
        return u"Kill Bill Volume 2"
    if movie == "Broadway: The Golden Age":
        return u"Broadway The Golden Age"
    if movie == "Tae Guk Gi: The Brotherhood Of War":
        return u"Tae Guk Gi The Brotherhood Of War"
    if movie == "Uncovered: The War On Iraq":
        return u"Uncovered The War On Iraq"
    if movie == "NASCAR: The IMAX Experience":
        return u"NASCAR The IMAX Experience"
    if movie == "Tristram Shandy: A Cock & Bull Story":
        return u"Tristram Shandy A Cock & Bull Story"
    if movie == "Shake Hands With The Devil: The Journey Of Romeo Dallaire":
        return u"Shake Hands With The Devil The Journey Of Romeo Dallaire"
    if movie == "Ong-Bak (Ong Bak: Muay Thai Warrior)":
        return u"Ong-Bak (Ong Bak Muay Thai Warrior)"
    if movie == "CSA: The Confederate States Of America":
        return u"CSA The Confederate States Of America"
    if movie == "Neil Young: Heart Of Gold":
        return u"Neil Young Heart Of Gold"
    if movie == "Sophie Scholl: The Final Days":
        return u"Sophie Scholl The Final Days"
    if movie == "Once In A Lifetime: The Extraordinary Story Of The New York Cosmos":
        return u"Once In A Lifetime The Extraordinary Story Of The New York Cosmos"
    if movie == "Joe Strummer: The Future Is Unwritten":
        return u"Joe Strummer The Future Is Unwritten"
    if movie == "ShowBusiness: The Road To Broadway":
        return u"ShowBusiness The Road To Broadway"
    if movie == "When The Road Bends: Tales Of A Gypsy Caravan":
        return u"When The Road Bends Tales Of A Gypsy Caravan"
    if movie == "Dear Zachary: A Letter To A Son About His Father":
        return u"Dear Zachary A Letter To A Son About His Father"
    if movie == "Not Quite Hollywood: The Wild, Untold Story Of Ozploitation!":
        return u"Not Quite Hollywood The Wild, Untold Story Of Ozploitation!"
    if movie == "Roman Polanski: Wanted And Desired":
        return u"Roman Polanski Wanted And Desired"
    if movie == "Gonzo: The Life And Work Of Hunter S. Thompson":
        return u"Gonzo The Life And Work Of Hunter S. Thompson"
    if movie == "Flow: For Love Of Water":
        return u"Flow For Love Of Water"
    if movie == "Che: Part Two (Guerrilla)":
        return u"Che Part Two (Guerrilla)"
    if movie == "OSS 117: Le Caire Nid d'Espions (OSS 117: Cairo, Nest Of Spies)":
        return u"OSS 117 Le Caire Nid d'Espions (OSS 117 Cairo, Nest Of Spies)"
    if movie == "Bad Lieutenant: Port Of Call New Orleans":
        return u"Bad Lieutenant Port Of Call New Orleans"
    if movie == "No Impact Man: The Documentary":
        return u"No Impact Man The Documentary"
    if movie == "Client 9: The Rise And Fall Of Eliot Spitzer":
        return u"Client 9 The Rise And Fall Of Eliot Spitzer"
    if movie == "Joan Rivers: A Piece Of Work":
        return u"Joan Rivers A Piece Of Work"
    if movie == "Rare Exports: A Christmas Tale":
        return u"Rare Exports A Christmas Tale"
    if movie == "Mesrine: Public Enemy #1":
        return u"Mesrine Public Enemy #1"
    if movie == "Mesrine: Killer Instinct (L'instinct de mort)":
        return u"Mesrine Killer Instinct (L'instinct de mort)"
    if movie == "OSS 117: Rio ne répond plus (Lost In Rio)":
        return u"OSS 117 Rio ne répond plus (Lost In Rio)"
    if movie == "Elite Squad: The Enemy Within":
        return u"Elite Squad The Enemy Within"
    if movie == "Corman's World: Exploits Of A Hollywood Rebel":
        return u"Corman's World Exploits Of A Hollywood Rebel"
    if movie == "Beats Rhymes & Life: The Travels Of A Tribe Called Quest":
        return u"Beats Rhymes & Life The Travels Of A Tribe Called Quest"
    if movie == "POM Wonderful Presents: The Greatest Movie Ever Sold":
        return u"POM Wonderful Presents The Greatest Movie Ever Sold"
    if movie == "Diana Vreeland: The Eye Has To Travel":
        return u"Diana Vreeland The Eye Has To Travel"
    if movie == "Electric Boogaloo: The Wild, Untold Story Of Cannon Films":
        return u"Electric Boogaloo The Wild, Untold Story Of Cannon Films"
    if movie == "The Raid: Redemption":
        return u"The Raid Redemption"
    if movie == "We Steal Secrets: The Story Of Wikileaks":
        return u"We Steal Secrets The Story Of Wikileaks"
    if movie == "Happy People: A Year In The Taiga":
        return u"Happy People A Year In The Taiga"
    if movie == "The Internet's Own Boy: The Story Of Aaron Swartz":
        return u"The Internet's Own Boy The Story Of Aaron Swartz"
    if movie == "Live Die Repeat: Edge Of Tomorrow":
        return u"Live Die Repeat Edge Of Tomorrow"
    if movie == "Going Clear: Scientology And The Prison Of Belief":
        return u"Going Clear Scientology And The Prison Of Belief"
    if movie == "The Black Panthers: Vanguard Of The Revolution":
        return u"The Black Panthers Vanguard Of The Revolution"
    if movie == "Janis: Little Girl Blue":
        return u"Janis Little Girl Blue"
    if movie == "Peggy Guggenheim: Art Addict":
        return u"Peggy Guggenheim Art Addict"
    if movie == "Miss Hokusai (Sarusuberi: Miss Hokusai)":
        return u"Miss Hokusai (Sarusuberi Miss Hokusai)"
    if movie == "Citizen Jane: Battle For The City":
        return u"Citizen Jane Battle For The City"
    if movie == "Abacus: Small Enough To Jail":
        return u"Abacus Small Enough To Jail"
    if movie == "John Wick: Chapter 2":
        return u"John Wick Chapter 2"
    if movie == "David Lynch: The Art Life":
        return u"David Lynch The Art Life"
    if movie == "Norman (Norman: The Moderate Rise And Tragic Fall Of A New York Fixer)":
        return u"Norman (Norman The Moderate Rise And Tragic Fall Of A New York Fixer)"
    if movie == "Whitney: Can I Be Me":
        return u"Whitney Can I Be Me"

    if movie == "Ninja 3: The Domination":
        return u"Ninja 3 The Domination"
    if movie == "Christopher Columbus: The Discovery":
        return u"Christopher Columbus The Discovery"
    if movie == "White Fang II: Myth Of The White Wolf":
        return u"White Fang II Myth Of The White Wolf"
    if movie == "Turbo: A Power Rangers Movie":
        return u"Turbo A Power Rangers Movie"
    if movie == "Kandahar: Le soleil derrière la lune":
        return u"Kandahar Le soleil derrière la lune"
    if movie == "Punisher: War Zone":
        return u"Punisher War Zone"
    if movie == "Expelled: No Intelligence Allowed":
        return u"Expelled No Intelligence Allowed"
    if movie == "Dolphins And Whales: Tribes Of The Ocean 3D":
        return u"Dolphins And Whales Tribes Of The Ocean 3D"
    if movie == "Kevin Hart: Laugh At My Pain":
        return u"Kevin Hart Laugh At My Pain"
    if movie == "Sea Rex 3D: Journey To A Prehistoric World":
        return u"Sea Rex 3D Journey To A Prehistoric World"
    if movie == "Dragon Ball Z: Resurrection 'F'":
        return u"Dragon Ball Z Resurrection 'F'"
    if movie == "Baahubali: The Beginning":
        return u"Baahubali The Beginning"
        
    if movie == "Transformers: The Movie":
        return u"Transformers The Movie"
    if movie == "Wanted: Dead Or Alive":
        return u"Wanted Dead Or Alive"
        
    if movie == "Death Wish 4: The Crackdown":
        return u"Death Wish 4 The Crackdown"
    if movie == "Braddock: Missing In Action III":
        return u"Braddock Missing In Action III"
    if movie == "Shag: The Movie":
        return u"Shag The Movie"
    if movie == "Leatherface: The Texas Chainsaw Massacre III":
        return u"Leatherface The Texas Chainsaw Massacre III"
    if movie == "Delta Force 2: Operation Stranglehold":
        return u"Delta Force 2 Operation Stranglehold"
    if movie == "1492: Conquest Of Paradise":
        return u"1492 Conquest Of Paradise"
    if movie == "Batman: Mask Of The Phantasm":
        return u"Batman Mask Of The Phantasm"
    if movie == "Gold Diggers: Secret Of Bear Mountain":
        return u"Gold Diggers Secret Of Bear Mountain"
    if movie == "Air Bud: Golden Receiver":
        return u"Air Bud Golden Receiver"
    if movie == "Megiddo: The Omega Code II":
        return u"Megiddo The Omega Code II"
    if movie == "Ong Bak: The Thai Warrior":
        return u"Ong Bak The Thai Warrior"
    if movie == "National Lampoon's Van Wilder: The Rise Of Taj":
        return u"National Lampoon's Van Wilder The Rise Of Taj"
    if movie == "In The Name Of The King: A Dungeon Siege Tale":
        return u"In The Name Of The King A Dungeon Siege Tale"
    if movie == "OSS 117: Rio ne répond plus (Lost In Rio)":
        return u"OSS 117 Rio ne répond plus (Lost In Rio)"
    if movie == "Atlas Shrugged: Part I":
        return u"Atlas Shrugged Part I"
    if movie == "Absolutely Fabulous: The Movie":
        return u"Absolutely Fabulous The Movie"
    
    if movie == "Yor: Hunter From The Future":
        return u"Yor Hunter From The Future"
    if movie == "Starchaser: The Legend Of Orin":
        return u"Starchaser The Legend Of Orin"
    if movie == "Critters 2: The Main Course":
        return u"Critters 2 The Main Course"
    if movie == "Imagine: John Lennon":
        return u"Imagine John Lennon"
    if movie == "Mannequin Two: On The Move":
        return u"Mannequin Two On The Move"
    if movie == "Warlock: The Armageddon":
        return u"Warlock The Armageddon"
    if movie == "Lawnmower Man 2: Beyond Cyberspace":
        return u"Lawnmower Man 2 Beyond Cyberspace"
    if movie == "Major League: Back To The Minors":
        return u"Major League Back To The Minors"
    if movie == "Ghost Dog: Way Of The Samurai":
        return u"Ghost Dog Way Of The Samurai"
    if movie == "Kandahar: Le soleil derrière la lune":
        return u"Kandahar Le soleil derrière la lune"
    if movie == "The Endurance: Shackleton's Antarctic Adventure":
        return u"The Endurance Shackleton's Antarctic Adventure"
    if movie == "Bobby Jones: Stroke Of Genius":
        return u"Bobby Jones Stroke Of Genius"
    if movie == "Therese: The Story Of Saint Therese Of Lisieux":
        return u"Therese The Story Of Saint Therese Of Lisieux"
    if movie == "Trailer Park Boys: The Movie":
        return u"Trailer Park Boys The Movie"
    if movie == "After Dark's Horror Fest: 8 Films To Die For":
        return u"After Dark's Horror Fest 8 Films To Die For"
    if movie == "The Work And The Glory II: American Zion":
        return u"The Work And The Glory II American Zion"
    if movie == "Bucky Larson: Born To Be A Star":
        return u"Bucky Larson Born To Be A Star"
    if movie == "Atlas Shrugged: Part II":
        return u"Atlas Shrugged Part II"
    if movie == "The Admiral: Roaring Currents":
        return u"The Admiral Roaring Currents"
    if movie == "Dragon Ball Z: Battle Of Gods":
        return u"Dragon Ball Z Battle Of Gods"
    if movie == "Norman: The Moderate Rise And Tragic Fall Of A New York Fixer":
        return u"Norman The Moderate Rise And Tragic Fall Of A New York Fixer"
    if movie == "An Inconvenient Sequel: Truth To Power":
        return u"An Inconvenient Sequel Truth To Power"
    if movie == "T2: Trainspotting":
        return u"T2 Trainspotting"

    if movie == "Squanto: A Warrior's Tale":
        return u"Squanto A Warrior's Tale"
    if movie == "Kids In The Hall: Brain Candy":
        return u"Kids In The Hall Brain Candy"
    if movie == "MVP: Most Valuable Primate":
        return u"MVP Most Valuable Primate"
    if movie == "El Vacilon: The Movie":
        return u"El Vacilon The Movie"
    if movie == "Sarah Silverman: Jesus Is Magic":
        return u"Sarah Silverman Jesus Is Magic"
    if movie == "Tristram Shandy: A Cock And Bull Story":
        return u"Tristram Shandy A Cock And Bull Story"
    if movie == "The Work And The Glory III: A House Divided":
        return u"The Work And The Glory III A House Divided"
    if movie == "Blade Runner: The Final Cut":
        return u"Blade Runner The Final Cut"
    if movie == "Valentino: The Last Emperor":
        return u"Valentino The Last Emperor"
    if movie == "Beats, Rhymes & Life: The Travels Of A Tribe Called Quest":
        return u"Beats, Rhymes & Life The Travels Of A Tribe Called Quest"
    if movie == "Dylan Dog: Dead Of Night":
        return u"Dylan Dog Dead Of Night"
    if movie == "Page One: A Year Inside The New York Times":
        return u"Page One A Year Inside The New York Times"
    if movie == "Woman Thou Art Loosed!: On The 7th Day":
        return u"Woman Thou Art Loosed! On The 7th Day"
    if movie == "Awake: The Life Of Yogananda":
        return u"Awake The Life Of Yogananda"
    if movie == "M.S. Dhoni: The Untold Story":
        return u"M.S. Dhoni The Untold Story"
    if movie == "Mojin: The Lost Legend":
        return u"Mojin The Lost Legend"
    if movie == "Papa: Hemingway In Cuba":
        return u"Papa Hemingway In Cuba"
    if movie == "Toilet: Ek Prem Katha":
        return u"Toilet Ek Prem Katha"
    if movie == "Newsies: The Broadway Musical":
        return u"Newsies The Broadway Musical"
    if movie == "Sword Art Online: The Movie - Ordinal Scale":
        return u"Sword Art Online The Movie - Ordinal Scale"
    
    if movie == "GoBots: Battle Of The Rock Lords":
        return u"GoBots Battle Of The Rock Lords"
    if movie == "Hello Mary Lou: Prom Night II":
        return u"Hello Mary Lou Prom Night II"
    if movie == "Aces: Iron Eagle III":
        return u"Aces Iron Eagle III"
    if movie == "Death Wish V: The Face Of Death":
        return u"Death Wish V The Face Of Death"
    if movie == "Free Willy 3: The Rescue":
        return u"Free Willy 3 The Rescue"
    if movie == "Xiu Xiu: The Sent Down Girl":
        return u"Xiu Xiu The Sent Down Girl"
    if movie == "Karmina 2: L'enfer de Chabot":
        return u"Karmina 2 L'enfer de Chabot"
    if movie == "Ghost In The Shell 2: Innocence":
        return u"Ghost In The Shell 2 Innocence"
    if movie == "Zatoichi: The Blind Swordsman":
        return u"Zatoichi The Blind Swordsman"
    if movie == "Alex Rider: Operation Stormbreaker":
        return u"Alex Rider Operation Stormbreaker"
    if movie == "Emma Smith: My Story":
        return u"Emma Smith My Story"
    if movie == "Vince Vaughn's Wild West Comedy Show: 30 Days & 30 Nights - From Hollywood To The Heartland":
        return u"Vince Vaughn's Wild West Comedy Show 30 Days & 30 Nights - From Hollywood To The Heartland"
    if movie == "Noah's Arc: Jumping The Broom":
        return u"Noah's Arc Jumping The Broom"
    if movie == "The Cross: The Arthur Blessit Story":
        return u"The Cross The Arthur Blessit Story"
    if movie == "Mesrine: Killer Instinct":
        return u"Mesrine Killer Instinct"
    if movie == "Sholem Aleichem: Laughing In The Darkness":
        return u"Sholem Aleichem Laughing In The Darkness"
    if movie == "Atlas Shrugged Part III: Who Is John Galt?":
        return u"Atlas Shrugged Part III Who Is John Galt?"
    if movie == "Nymphomaniac: Volume I":
        return u"Nymphomaniac Volume I"
    if movie == "Walking The Camino: Six Ways To Santiago":
        return u"Walking The Camino Six Ways To Santiago"
    if movie == "On Any Sunday: The Next Chapter":
        return u"On Any Sunday The Next Chapter"
    if movie == "Gett: The Trial Of Viviane Amsalem":
        return u"Gett The Trial Of Viviane Amsalem"
    if movie == "Boruto: Naruto The Movie":
        return u"Boruto Naruto The Movie"
    if movie == "Brothers: Blood Against Blood":
        return u"Brothers Blood Against Blood"
    if movie == "Patterns Of Evidence: The Exodus":
        return u"Patterns Of Evidence The Exodus"
    if movie == "Chaar Sahibzaade: Rise Of Band Singh Bahadur":
        return u"Chaar Sahibzaade Rise Of Band Singh Bahadur"
    if movie == "Terminator 2: Judgment Day 3D":
        return u"Terminator 2 Judgment Day 3D"
    if movie == "Journey To The West: The Demons Strike Back":
        return u"Journey To The West The Demons Strike Back"
    if movie == "Chris Brown: Welcome To My Life":
        return u"Chris Brown Welcome To My Life"
    if movie == "Fairy Tail: Dragon Cry":
        return u"Fairy Tail Dragon Cry"    

    if movie == "Dr. Seuss' Horton Hears A Who!":
        return u"Horton Hears A Who!"

    if movie == "Nutcracker: The Motion Picture":
        return u"Nutcracker The Motion Picture"
    if movie == "Little Nemo: Adventures In Slumberland":
        return u"Little Nemo Adventures In Slumberland"
    if movie == "The Second Jungle Book: Mowgli And Baloo":
        return u"The Second Jungle Book Mowgli And Baloo"
    if movie == "Steam: Turkish Bath":
        return u"Steam Turkish Bath"
    if movie == "Cinema Paradiso: The New Version":
        return u"Cinema Paradiso The New Version"
    if movie == "Armaan: The Desire":
        return u"Armaan The Desire"
    if movie == "Still, We Believe: The Boston Red Sox Movie":
        return u"Still, We Believe The Boston Red Sox Movie"
    if movie == "Ju-On: The Grudge":
        return u"Ju-On The Grudge"
    if movie == "Bukowski: Born Into This":
        return u"Bukowski Born Into This"
    if movie == "Short Cut To Nirvana: Kumbh Mela":
        return u"Short Cut To Nirvana Kumbh Mela"
    if movie == "DOA: Dead Or Alive":
        return u"DOA Dead Or Alive"
    if movie == "Romeo & Juliet: Sealed With A Kiss":
        return u"Romeo & Juliet Sealed With A Kiss"
    if movie == "Provoked: A True Story":
        return u"Provoked A True Story"
    if movie == "Wristcutters: A Love Story":
        return u"Wristcutters A Love Story"
    if movie == "Billy: The Early Years Of Billy Graham":
        return u"Billy The Early Years Of Billy Graham"
    if movie == "OSS 117: Cairo, Nest Of Spies":
        return u"OSS 117 Cairo, Nest Of Spies"
    if movie == "La Danse: Le Ballet de L'Opera de Paris":
        return u"La Danse Le Ballet de L'Opera de Paris"
    if movie == "Turtle: The Incredible Journey":
        return u"Turtle The Incredible Journey"
    if movie == "Puella Magi Madoka Magica The Movie: Rebellion":
        return u"Puella Magi Madoka Magica The Movie Rebellion"
    if movie == "Nymphomaniac: Volume II":
        return u"Nymphomaniac Volume II"
    if movie == "Jimi: All Is By My Side":
        return u"Jimi All Is By My Side"
    if movie == "Steve Jobs: The Man In The Machine":
        return u"Steve Jobs The Man In The Machine"
    if movie == "Black Panthers: Vanguard Of The Revolution":
        return u"Black Panthers Vanguard Of The Revolution"
    if movie == "Eat That Question: Frank Zappa In His Own Words":
        return u"Eat That Question Frank Zappa In His Own Words"
    if movie == "L.O.R.D: Legend Of Ravaging Dynasties":
        return u"L.O.R.D Legend Of Ravaging Dynasties"
    if movie == "Chasing Trane: The John Coltrane Documentary":
        return u"Chasing Trane The John Coltrane Documentary"
    if movie == "One Piece Film: Gold":
        return u"One Piece Film Gold"


    if movie == "Code Name: Emerald":
        return u"Code Name Emerald"
    if movie == "Babar: The Movie":
        return u"Babar The Movie"
    if movie == "American Ninja 3: Blood Hunt":
        return u"American Ninja 3 Blood Hunt"
    if movie == "American Ninja 4: The Annihilation":
        return u"American Ninja 4 The Annihilation"
    if movie == "Ram Dass: Fierce Grace":
        return u"Ram Dass Fierce Grace"
    if movie == "Power And Terror: Noam Chomsky In Our Times":
        return u"Power And Terror Noam Chomsky In Our Times"
    if movie == "Dominion: Prequel To The Exorcist":
        return u"Dominion Prequel To The Exorcist"
    if movie == "The Keeper: The Legend Of Omar Khayyam":
        return u"The Keeper The Legend Of Omar Khayyam"
    if movie == "Fur: An Imaginary Portrait Of Diane Arbus":
        return u"Fur An Imaginary Portrait Of Diane Arbus"
    if movie == "Goal 2: Living The Dream":
        return u"Goal 2 Living The Dream"
    if movie == "Blood: The Last Vampire":
        return u"Blood The Last Vampire"
    if movie == "Larger than Life In 3D: Dave Matthews Band, Ben Harper And Gogol Bordello":
        return u"Larger than Life In 3D Dave Matthews Band, Ben Harper And Gogol Bordello"
    if movie == "Jean-Michel Basquiat: The Radiant Child":
        return u"Jean-Michel Basquiat The Radiant Child"
    if movie == "Mesrine: Public Enemy No. 1":
        return u"Mesrine Public Enemy No. 1"
    if movie == "The Black Power Mix Tape: 1967-1975":
        return u"The Black Power Mix Tape 1967-1975"
    if movie == "Phil Ochs: There But For Fortune":
        return u"Phil Ochs There But For Fortune"
    if movie == "Gainsbourg: A Heroic Life":
        return u"Gainsbourg A Heroic Life"
    if movie == "Ip Man 2: Legend Of The Grandmaster":
        return u"Ip Man 2 Legend Of The Grandmaster"
    if movie == "Something From Nothing: The Art Of Rap":
        return u"Something From Nothing The Art Of Rap"
    if movie == "El Bulli: Cooking In Progress":
        return u"El Bulli Cooking In Progress"
    if movie == "Kundo: Age Of The Rampant":
        return u"Kundo Age Of The Rampant"
    if movie == "Tazza: The Hidden Card":
        return u"Tazza The Hidden Card"
    if movie == "The Galapagos Affair: Satan Came To Eden":
        return u"The Galapagos Affair Satan Came To Eden"
    if movie == "Supermensch: The Legend Of Shep Gordon":
        return u"Supermensch The Legend Of Shep Gordon"
    if movie == "Antarctica: A Year On Ice":
        return u"Antarctica A Year On Ice"
    if movie == "Attack On Titan: Part 2":
        return u"Attack On Titan Part 2"
    if movie == "Kingsglaive: Final Fantasy: XV":
        return u"Kingsglaive Final Fantasy XV"
    if movie == "Oasis: Supersonic":
        return u"Oasis Supersonic"
    if movie == "Jimmy Vestvood: Amerikan Hero":
        return u"Jimmy Vestvood Amerikan Hero"
    if movie == "Sailor Moon R: The Movie":
        return u"Sailor Moon R The Movie"
    

    if movie == "3 Ninjas: High Noon At Mega Mountain":
        return u"3 Ninjas High Noon At Mega Mountain"
    if movie == "Code Unknown (Code inconnu: Récit incomplet de divers voyages)":
        return u"Code Unknown (Code inconnu Récit incomplet de divers voyages)"
    if movie == "Series 7: The Contenders":
        return u"Series 7 The Contenders"
    if movie == "Gigantic: A Tale Of Two Johns":
        return u"Gigantic A Tale Of Two Johns"
    if movie == "Howard Zinn: You Can't Be Neutral On A Moving Train":
        return u"Howard Zinn You Can't Be Neutral On A Moving Train"
    if movie == "Games People Play: New York":
        return u"Games People Play New York"
    if movie == "In The Face Of Evil: Reagan's War In Word And Deed":
        return u"In The Face Of Evil Reagan's War In Word And Deed"
    if movie == "Carlos Castaneda: Enigma Of A Sorcerer":
        return u"Carlos Castaneda Enigma Of A Sorcerer"
    if movie == "Awesome: I F%!#in' Shot That":
        return u"Awesome I F%!#in' Shot That"
    if movie == "Mountain Patrol: Kekexili":
        return u"Mountain Patrol Kekexili"
    if movie == "What The Bleep?: Down The Rabbit Hole":
        return u"What The Bleep? Down The Rabbit Hole"
    if movie == "Be Here To Love Me: A Film About Townes Van Zandt":
        return u"Be Here To Love Me A Film About Townes Van Zandt"
    if movie == "Jonestown: The Life And Death Of Peoples Temple":
        return u"Jonestown The Life And Death Of Peoples Temple"
    if movie == "Al Franken: God Spoke":
        return u"Al Franken God Spoke"
    if movie == "Rise: Blood Hunter":
        return u"Rise Blood Hunter"
    if movie == "FLOW: For Love Of Water":
        return u"FLOW For Love Of Water"
    if movie == "Repo: The Genetic Opera":
        return u"Repo The Genetic Opera"
    if movie == "Another Gay Sequel: Gays Gone Wild":
        return u"Another Gay Sequel Gays Gone Wild"
    if movie == "Youssou N'Dour: I Bring What I Love":
        return u"Youssou N'Dour I Bring What I Love"
    if movie == "Ong Bak 2: The Beginning":
        return u"Ong Bak 2 The Beginning"
    if movie == "Nick Saban: Gamechanger":
        return u"Nick Saban Gamechanger"
    if movie == "Genius Within: The Inner Life Of Glenn Gould":
        return u"Genius Within The Inner Life Of Glenn Gould"
    if movie == "The Man Nobody Knew: In Search Of My Father, CIA Spymaster William Colby":
        return u"The Man Nobody Knew In Search Of My Father, CIA Spymaster William Colby"
    if movie == "Sex And Zen 3D: Extreme Ecstasy":
        return u"Sex And Zen 3D Extreme Ecstasy"
    if movie == "Evangelion 2.0: You Can (Not) Advance":
        return u"Evangelion 2.0 You Can (Not) Advance"
    if movie == "Eames: The Architect And The Painter":
        return u"Eames The Architect And The Painter"
    if movie == "The Human Centipede 2: Full Sequence":
        return u"The Human Centipede 2 Full Sequence"
    if movie == "Fullmetal Alchemist: The Sacred Star Of Milos":
        return u"Fullmetal Alchemist The Sacred Star Of Milos"
    if movie == "Monumental: In Search Of America's National Treasure":
        return u"Monumental In Search Of America's National Treasure"
    if movie == "Warriors Of The Rainbow: Seediq Bale":
        return u"Warriors Of The Rainbow Seediq Bale"
    if movie == "Follow Me: The Yoni Netanyahu Story":
        return u"Follow Me The Yoni Netanyahu Story"
    if movie == "Steve Jobs: The Lost Interview":
        return u"Steve Jobs The Lost Interview"
    if movie == "Cinco De Mayo: La Batalla":
        return u"Cinco De Mayo La Batalla"
    if movie == "Deceptive Practice: The Mysteries And Mentors Of Ricky Jay":
        return u"Deceptive Practice The Mysteries And Mentors Of Ricky Jay"
    if movie == "Spark: A Burning Man Story":
        return u"Spark A Burning Man Story"
    if movie == "Ain't In It For My Health: A Film About Levon Helm":
        return u"Ain't In It For My Health A Film About Levon Helm"
    if movie == "Big Star: Nothing Can Hurt Me":
        return u"Big Star Nothing Can Hurt Me"
    if movie == "Evangelion: 3.0 You Can (Not) Redo":
        return u"Evangelion 3.0 You Can (Not) Redo"
    if movie == "Alan Partridge: The Movie":
        return u"Alan Partridge The Movie"
    if movie == "Godzilla: The Japanese Original":
        return u"Godzilla The Japanese Original"
    if movie == "Gore Vidal: United States Of Amnesia":
        return u"Gore Vidal United States Of Amnesia"
    if movie == "Final: The Rapture":
        return u"Final The Rapture"
    if movie == "NAS: Time Is Illmatic":
        return u"NAS Time Is Illmatic"
    if movie == "Sinbad: The Fifth Voyage":
        return u"Sinbad The Fifth Voyage"
    if movie == "Detective K: Secret Of The Lost Island":
        return u"Detective K Secret Of The Lost Island"
    if movie == "Escobar: Paradise Lost":
        return u"Escobar Paradise Lost"
    if movie == "Backstreet Boys: Show 'Em What You're Made Of":
        return u"Backstreet Boys Show 'Em What You're Made Of"
    if movie == "Don't Think I've Forgotten: Cambodia's Lost Rock And Roll":
        return u"Don't Think I've Forgotten Cambodia's Lost Rock And Roll"
    if movie == "Asura: The City Of Madness":
        return u"Asura The City Of Madness"
    if movie == "Hieronymus Bosch: Touched By The Devil":
        return u"Hieronymus Bosch Touched By The Devil"
    if movie == "Vaxxed: From Cover-Up To Catastrophe":
        return u"Vaxxed From Cover-Up To Catastrophe"
    if movie == "Embrace: The Documentary":
        return u"Embrace The Documentary"
    if movie == "Ingrid Bergman: In Her Own Words":
        return u"Ingrid Bergman In Her Own Words"
    if movie == "Spark: A Space Tail":
        return u"Spark A Space Tail"
    if movie == "Mr. Gaga: A True Story Of Love And Dance":
        return u"Mr. Gaga A True Story Of Love And Dance"
    if movie == "Restless Creature: Wendy Whelan":
        return u"Restless Creature Wendy Whelan"
    if movie == "Marie Curie: The Courage Of Knowledge":
        return u"Marie Curie The Courage Of Knowledge"
    if movie == "Buena Vista Social Club: Adios":
        return u"Buena Vista Social Club Adios"
    if movie == "Rumble: The Indians Who Rocked The World":
        return u"Rumble The Indians Who Rocked The World"
    if movie == "Dawson City: Frozen Time":
        return u"Dawson City Frozen Time"
    if movie == "Bolshoi Ballet: Hero Of Our Time":
        return u"Bolshoi Ballet Hero Of Our Time"    

    if movie == "The Toxic Avenger Part III: The Last Temptation Of Toxie":
        return u"The Toxic Avenger Part III The Last Temptation Of Toxie"
    if movie == "Kama Sutra: A Tale Of Love":
        return u"Kama Sutra A Tale Of Love"
    if movie == "Das Boot: The Director's Cut":
        return u"Das Boot"
    if movie == "Les Couloirs du Temps: Les Visiteurs 2":
        return u"Les Couloirs du Temps Les Visiteurs 2"
    if movie == "Nijinsky: The Diaries of...":
        return u"Nijinsky The Diaries of..."
    if movie == "Boys Life 4: Four Play":
        return u"Boys Life 4 Four Play"
    if movie == "Aileen: The Life And Death Of A Serial Killer":
        return u"Aileen The Life And Death Of A Serial Killer"
    if movie == "Celsius 41.11: The Truth Behind The Lies Of Fahrenheit 9/11":
        return u"Celsius 41.11 The Truth Behind The Lies Of Fahrenheit 9/11"
    if movie == "Ginger Snaps II: Unleashed":
        return u"Ginger Snaps II Unleashed"
    if movie == "On The Run: Trilogy 1":
        return u"On The Run Trilogy 1"
    if movie == "Crossing The Bridge: The Sound Of Istanbul":
        return u"Crossing The Bridge The Sound Of Istanbul"
    if movie == "Shoujyo: The Adolescent":
        return u"Shoujyo The Adolescent"
    if movie == "That Man: Peter Berlin":
        return u"That Man Peter Berlin"
    if movie == "Pete Seeger: The Power Of Song":
        return u"Pete Seeger The Power Of Song"
    if movie == "Behind The Mask: The Rise Of Leslie Vernon":
        return u"Behind The Mask The Rise Of Leslie Vernon"
    if movie == "Louise Bourgeois: The Spider, The Mistress And The Tangerine":
        return u"Louise Bourgeois The Spider, The Mistress And The Tangerine"
    if movie == "CSNY: Deja Vu":
        return u"CSNY Deja Vu"
    if movie == "Stranded: I Have Come From A Plane That Crashed On The Mountains":
        return u"Stranded I Have Come From A Plane That Crashed On The Mountains"
    if movie == "Boogie Man: The Lee Atwater Story":
        return u"Boogie Man The Lee Atwater Story"
    if movie == "Crips And Bloods: Made In America":
        return u"Crips And Bloods Made In America"
    if movie == "The Boys: The Sherman Brothers' Story":
        return u"The Boys The Sherman Brothers' Story"
    if movie == "8: The Mormon Proposition":
        return u"8 The Mormon Proposition"
    if movie.find("OSS 117") != -1:
        return u"OSS 117 Lost In Rio"
    if movie == "The Sun Behind The Clouds: Tibet's Struggle For Freedom":
        return u"The Sun Behind The Clouds Tibet's Struggle For Freedom"
    if movie == "See What I'm Saying: The Deaf Entertainers Documentary":
        return u"See What I'm Saying The Deaf Entertainers Documentary"
    if movie == "Harlan: In The Shadow Of Jew Suss":
        return u"Harlan In The Shadow Of Jew Suss"
    if movie == "American: The Bill Hicks Story":
        return u"American The Bill Hicks Story"
    if movie == "Vidal Sassoon: The Movie":
        return u"Vidal Sassoon The Movie"
    if movie == "Strange Powers: Stephin Merritt And The Magnetic Fields":
        return u"Strange Powers Stephin Merritt And The Magnetic Fields"
    if movie == "Trigun: Badlands Rumble":
        return u"Trigun Badlands Rumble"
    if movie == "If A Tree Falls: A Story Of The Earth Liberation Front":
        return u"If A Tree Falls A Story Of The Earth Liberation Front"
    if movie == "One Track Heart: The Story Of Krishna Das":
        return u"One Track Heart The Story Of Krishna Das"
    if movie == "Young Detective Dee: Rise Of The Sea Dragon":
        return u"Young Detective Dee Rise Of The Sea Dragon"
    if movie == "Don't Stop Believin': Everyman's Journey":
        return u"Don't Stop Believin' Everyman's Journey"
    if movie == "Gregory Crewdson: Brief Encounters":
        return u"Gregory Crewdson Brief Encounters"
    if movie == "Beyond Sight: The Derek Rabelo Story":
        return u"Beyond Sight The Derek Rabelo Story"
    if movie == "Anohana The Movie: The Flower We Saw That Day":
        return u"Anohana The Movie The Flower We Saw That Day"
    if movie == "Penton: The John Penton Story":
        return u"Penton The John Penton Story"
    if movie == "Whitey: USA v. James J. Bulger":
        return u"Whitey USA v. James J. Bulger"
    if movie == "Going Attractions: The Definitive Story Of The American Drive-in Movie":
        return u"Going Attractions The Definitive Story Of The American Drive-in Movie"
    if movie == "Drunk Stoned Brilliant Dead: The Story Of The National Lampoon":
        return u"Drunk Stoned Brilliant Dead The Story Of The National Lampoon"
    if movie == "Dark Star: H.R. Giger's World":
        return u"Dark Star H.R. Giger's World"
    if movie == "Sagrada: The Mystery Of Creation":
        return u"Sagrada The Mystery Of Creation"
    if movie == "Seed: The Untold Story":
        return u"Seed The Untold Story"
    if movie == "Seondal: The Man Who Sells The River":
        return u"Seondal The Man Who Sells The River"
    if movie == "So Young 2: Never Gone":
        return u"So Young 2 Never Gone"
    if movie == "No One's Life Is Easy: So I Married an Anti-Fan":
        return u"No One's Life Is Easy So I Married an Anti-Fan"
    if movie == "Author: The JT LeRoy Story":
        return u"Author The JT LeRoy Story"
    if movie == "Vita Activa: The Spirit Of Hannah Arendt":
        return u"Vita Activa The Spirit Of Hannah Arendt"
    if movie == "Raiders!: The Story Of The Greatest Fan Film Ever Made":
        return u"Raiders! The Story Of The Greatest Fan Film Ever Made"
    if movie == "Norman Lear: Just Another Version Of You":
        return u"Norman Lear Just Another Version Of You"
    if movie == "DONGJU: The Portrait Of A Poet":
        return u"DONGJU The Portrait Of A Poet"
    if movie == "Voyage Of Time: The IMAX Experience":
        return u"Voyage Of Time The IMAX Experience"
    if movie == "Vanishing Time: A Boy Who Returned":
        return u"Vanishing Time A Boy Who Returned"
    if movie == "Stefan Zweig: Farewell To Europe":
        return u"Stefan Zweig Farewell To Europe"
    if movie == "Harold And Lillian: A Hollywood Love Story":
        return u"Harold And Lillian A Hollywood Love Story"
    if movie == "Mifune: The Last Samurai":
        return u"Mifune The Last Samurai"    
    
    
    if movie == "Star Wars: Episode I - The Phantom Menace (in 3D)":
        return None
    if movie == "Beauty And The Beast (3D)":
        return None
    if movie == "Finding Nemo (3D)":
        return None
    if movie == "Monsters, Inc. (3D)":
        return None
    if movie == "Jurassic Park 3D":
        return None
    if movie == "Snow White And The Seven Dwarfs (Re-issue)":
        return None
    if movie == "Toy Story / Toy Story 2 (3D)":
        return None
    if movie == "E.T. (20th Anniversary)":
        return None
    if movie == "Fantasia 2000 (35mm & IMAX)":
        return None
    if movie == "The Empire Strikes Back (Special Edition)":
        return None
    if movie == "101 Dalmatians (Re-issue)":
        return None
    if movie.find("(Special Edition)") != -1:
        return None
    if movie.find("(Re-issue)") != -1:
        return None
    if movie.find("(re-issue)") != -1:
        return None
    if movie == "Titanic" and int(year) > 2000:
        return None
    if movie == "Titanic 3D":
        return None
        
    
    if movie.find("Attack Of The Clones") != -1:
        print movie
        raise()
    
    return movie