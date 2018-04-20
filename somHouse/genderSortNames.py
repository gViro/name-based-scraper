import os # is this necessary? isn't open() part of standard lib?

# use another variable to hold the opend data 

exhibitors = ['Brendan Dawes', 'Charles Joseph Minard', 'David McCandless', 'Ellie Harrison', 'Eric Fischer', 'Erica Scourti', 'Eva' , 'Franco Mattes', 'Fight for the Future' , 'Demand Progress', 'Florence Nightingale', 'Forensic Architecture', 'Future Cities Catapult', 'Heather Dewey-Hagborg', 'Horst Ademeit', 'IF', 'Ingo Günther', 'Ingrid Burrington' , 'Dan Williams', 'Interaction Research Studio', 'Goldsmiths', 'ITO World', 'Jaime Serra', 'James Bridle', 'John Snow', 'Jonathan Harris', 'Jonathan Minard', 'Julian Oliver', 'Julie Freeman', 'Kamel Makhloufi', 'Kiln', 'Laura Poitras', 'Lev Manovich', 'Moritz Stefaner', 'Lisa Jevbratt', 'Lise Autogena' , 'Josh Portway', 'mySociety', 'Nesta', 'Nicholas Felton', 'Open Knowledge', 'OpenCorporates', 'Owen Mundy', 'Paolo Cirio' , 'Alessandro Ludovico', 'Philipp Adrian', 'Rafael Lozano Hemmer', 'Ryoji Ikeda', 'Safecast', 'Salvatore Iaconesi', 'Oriana Persico', 'Stefanie Posavec', 'Giorgia Lupi', 'Tekja', 'TeleGeography', 'The Guardian', 'The Long Now Foundation', 'Thomson' , 'Craighead', 'Timo Arnall', 'Umbrellium', 'William Elford', 'Zach Blas'] 

# using a list comprehesion to strip out first names

# firstNames = [i.split()[0] for i in exhibitors]

# doesn't strip out the corner case of studio names / non-human names
# necessary to compare list before gender grouping,discard all non-humans??

firstNames = ['Brendan', 'Charles', 'David', 'Ellie', 'Eric', 'Erica', 'Eva', 'Franco', 'Fight', 'Demand', 'Florence', 'Forensic', 'Future', 'Heather', 'Horst', 'IF', 'Ingo', 'Ingrid', 'Dan', 'Interaction', 'Goldsmiths', 'ITO', 'Jaime', 'James', 'John', 'Jonathan', 'Jonathan', 'Julian', 'Julie', 'Kamel', 'Kiln', 'Laura', 'Lev', 'Moritz', 'Lisa', 'Lise', 'Josh', 'mySociety', 'Nesta', 'Nicholas', 'Open', 'OpenCorporates', 'Owen', 'Paolo', 'Alessandro', 'Philipp', 'Rafael', 'Ryoji', 'Safecast', 'Salvatore', 'Oriana', 'Stefanie', 'Giorgia', 'Tekja', 'TeleGeography', 'The', 'The', 'Thomson', 'Craighead', 'Timo', 'Umbrellium', 'William', 'Zach']

# awesome way to strip out a word from list, but needs 2b func-d
# no_word_The = [item for item in firstNames if item != 'The']

firstNamesWithout_The = ['Brendan', 'Charles', 'David', 'Ellie', 'Eric', 'Erica', 'Eva', 'Franco', 'Fight', 'Demand', 'Florence', 'Forensic', 'Future', 'Heather', 'Horst', 'IF', 'Ingo', 'Ingrid', 'Dan', 'Interaction', 'Goldsmiths', 'ITO', 'Jaime', 'James', 'John', 'Jonathan', 'Jonathan', 'Julian', 'Julie', 'Kamel', 'Kiln', 'Laura', 'Lev', 'Moritz', 'Lisa', 'Lise', 'Josh', 'mySociety', 'Nesta', 'Nicholas', 'Open', 'OpenCorporates', 'Owen', 'Paolo', 'Alessandro', 'Philipp', 'Rafael', 'Ryoji', 'Safecast', 'Salvatore', 'Oriana', 'Stefanie', 'Giorgia', 'Tekja', 'TeleGeography', 'Thomson', 'Craighead', 'Timo', 'Umbrellium', 'William', 'Zach']

# would this be better by COMPARISON against a file?
# for ex: 
# nothing_but_names = [i for i in firstNames if i is in firstNames.txt]

# compare each exhibitor first name to a list of male first names
# if it matches, append it to a new list
# calculate , return what percentage of exhibitors are male

# names = open('maleNames.txt','r')

# remember to create a set to hold large amounts of data that need to be searched often; O(n) vs O(1) 
 


