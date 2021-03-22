from bs4 import BeautifulSoup
import pandas
import requests

TEAM_NAME = '.keeda_football_table_team_name'

res = requests.get('https://www.sportskeeda.com/go/la-liga/standings')

soup = BeautifulSoup(res.text, 'html.parser')

teamName = []

xTag = soup.findAll("td", {"class": "team-name-points-table"})


for x in xTag:
    tempVar = x.text
    tempVar = tempVar.replace('\n','')
    teamName.append(tempVar)

points = []
xTag1 = soup.findAll("td", {"class": "overall-points"})

for x in xTag1:
    temp1Var = x.text
    points.append(temp1Var)
points.append(" ")

dataframe = pandas.DataFrame({ "Team Name": teamName,"Points": points})
print(dataframe)
