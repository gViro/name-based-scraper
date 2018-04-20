# try to scrape the awwwards jurors webpage

# xpath for first juror name >> /html/body/div[2]/section/div/div/div/div/ul/li[1]/figure/a/div/ul/li[1]/h3

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.awwwards.com/jury/")
bsObj = BeautifulSoup(html.read(), "lxml")

jurors = bsObj.findAll("h3")
# corps = bsObj.findAll("div", {"class":"featured_text"})

jurors = []

for j in jurors:
    jurors.append(j.get_text())

print(jurors)

# after slicing some junk out, the artist list is below

# now figure out how to get them into a dictionary






# use pandas to_csv (http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_csv.html)

# import pandas as pd
# df = pd.DataFrame(names, columns=["exhibitors"])
# df.to_csv('names.csv', index=False)
