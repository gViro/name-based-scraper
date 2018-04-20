# try to scrape the artists from sommerset house Big Bang Data webpage

# xpath for artist name >> /html/body/div[5]/div/ul/li[1]/a/text()   ??? text in the final a

# code from previous scraper

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://bigbangdata.somersethouse.org.uk/artists/")
bsObj = BeautifulSoup(html.read(), "lxml")

artists = bsObj.findAll("a")
# corps = bsObj.findAll("div", {"class":"featured_text"})

names = []

for a in artists:
    names.append(a.get_text())

print(names)

# after slicing some junk out, the artist list is below

# now figure out how to get them into a dictionary

names = ['Brendan Dawes', 'Charles Joseph Minard', 'David McCandless', 'Ellie Harrison', 'Eric Fischer', 'Erica Scourti', 'Eva and Franco Mattes', 'Fight for the Future and Demand Progress', 'Florence Nightingale', 'Forensic Architecture', 'Future Cities Catapult', 'Heather Dewey-Hagborg', 'Horst Ademeit', 'IF', 'Ingo Günther', 'Ingrid Burrington and Dan Williams', 'Interaction Research Studio, Goldsmiths', 'ITO World', 'Jaime Serra', 'James Bridle', 'John Snow', 'Jonathan Harris', 'Jonathan Minard', 'Julian Oliver', 'Julie Freeman', 'Kamel Makhloufi', 'Kiln', 'Laura Poitras', 'Lev Manovich and Moritz Stefaner', 'Lisa Jevbratt', 'Lise Autogena and Josh Portway', 'mySociety', 'Nesta', 'Nicholas Felton', 'Open Knowledge', 'OpenCorporates', 'Owen Mundy', 'Paolo Cirio and Alessandro Ludovico', 'Philipp Adrian', 'Rafael Lozano Hemmer', 'Ryoji Ikeda', 'Safecast', 'Salvatore Iaconesi & Oriana Persico', 'Stefanie Posavec and  Giorgia Lupi', 'Tekja', 'TeleGeography', 'The Guardian', 'The Long Now Foundation', 'Thomson and Craighead', 'Timo Arnall', 'Umbrellium', 'William Elford', 'Zach Blas']




# use pandas to_csv (http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_csv.html)

import pandas as pd
df = pd.DataFrame(names, columns=["exhibitors"])
df.to_csv('names.csv', index=False)
