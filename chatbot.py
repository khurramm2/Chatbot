import pandas as pd
#pip install requests   - you might need to install this before using the API

import requests

url = "https://api-football-beta.p.rapidapi.com/players/topscorers"

querystring = {"season":"2022","league":"39"}

headers = {
	"X-RapidAPI-Key": "62a02ca5ccmsha68a5acf6c698d9p1ffc12jsnbe2b9a765139",
	"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print (type(response.json()))
print(response.json())
df = response.json()


playerid = 0
goals = df['response'][playerid]['statistics'][0]['goals']['total']
shot = df['response'][playerid]['statistics'][0]['shots']['total']
passing = df['response'][playerid]['statistics'][0]['passes']['total']

playercode = {'E. Haaland':0, 'H. Kane':1, 'A. Mitrović':2, 'I. Toney':3, 'L. Trossard':4, 'M. Almirón':5, 'P. Foden':6, 'Roberto Firmino':7}


def askplayer(name):
    askq = input(
        "I know a lot about football, if you want I can tell you about some of the top scorers in the premiere league. So what do you say, Yes or No? ")
    if askq == 'yes' or askq == 'Yes':
        print(
            "Here are the names of some of the top scorers I know, Choose any of those names and I'll tell you all about them")
        print("E. Haaland, H. Kane, A. Mitrović, I. Toney, L. Trossard, M. Almirón, P. Foden, Roberto Firmino")
        # playerchoose = input("So what's your choice ")
        while True:
            playerchoose = input("So what's your choice ")
            if playerchoose in playercode.keys():
                playerid = (playercode[playerchoose])
                # print(playerid)
                print(
                    "Ah yes... " + playerchoose + " I know all about him. Did you know in this season he has scored a total of "
                    + str(goals) + " goals and he's attempted a grande total of " + str(shot) + " shots")
                break




            else:
                print("That's not one of the names I gave you... Try again.")


askplayer("name")





