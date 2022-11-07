pip install requests

import http.client

conn = http.client.HTTPSConnection("livescore6.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "62a02ca5ccmsha68a5acf6c698d9p1ffc12jsnbe2b9a765139",
    'X-RapidAPI-Host': "livescore6.p.rapidapi.com"
    }

conn.request("GET", "/matches/v2/list-live?Category=soccer&Timezone=-7", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"soccer","Timezone":"-7"}

headers = {
	"X-RapidAPI-Key": "62a02ca5ccmsha68a5acf6c698d9p1ffc12jsnbe2b9a765139",
	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)