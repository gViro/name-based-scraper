# using pandas to make a csv file from a list
# use pandas to_csv (http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_csv.html)

# import pandas as pd  

names = ['Brendan Dawes', 'Charles Joseph Minard', 'David McCandless', 'Ellie Harrison', 'Eric Fischer', 'Erica Scourti', 'Eva and Franco Mattes', 'Fight for the Future and Demand Progress', 'Florence Nightingale', 'Forensic Architecture', 'Future Cities Catapult', 'Heather Dewey-Hagborg', 'Horst Ademeit', 'IF', 'Ingo Günther', 'Ingrid Burrington and Dan Williams', 'Interaction Research Studio, Goldsmiths', 'ITO World', 'Jaime Serra', 'James Bridle', 'John Snow', 'Jonathan Harris', 'Jonathan Minard', 'Julian Oliver', 'Julie Freeman', 'Kamel Makhloufi', 'Kiln', 'Laura Poitras', 'Lev Manovich and Moritz Stefaner', 'Lisa Jevbratt', 'Lise Autogena and Josh Portway', 'mySociety', 'Nesta', 'Nicholas Felton', 'Open Knowledge', 'OpenCorporates', 'Owen Mundy', 'Paolo Cirio and Alessandro Ludovico', 'Philipp Adrian', 'Rafael Lozano Hemmer', 'Ryoji Ikeda', 'Safecast', 'Salvatore Iaconesi & Oriana Persico', 'Stefanie Posavec and  Giorgia Lupi', 'Tekja', 'TeleGeography', 'The Guardian', 'The Long Now Foundation', 'Thomson and Craighead', 'Timo Arnall', 'Umbrellium', 'William Elford', 'Zach Blas']

# using pandas
# df = pd.DataFrame(names, columns=["exhibitors"])
# df.to_csv('names.csv', index=False)



# to create a txt file,new line per list item, and without the comma
theFile = open('exhibitors.txt', 'w')

# this is not working. Too idiomatic???
# for n in names:
#     print>>theFile, n 

# this is working great, UTF-8 and all
for n in names:
    theFile.write("%s\n" % n)


