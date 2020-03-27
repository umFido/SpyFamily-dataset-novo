import requests
import json
import datetime

#-------------------------------------------------------------------#

#Variables
#Empty list to get votes
spyFamily_Qnt_Votos = []
#Data
spyFamily_Date = datetime.datetime.now()
#Stats URL and Search
spyFamily_Stats_URL = "https://api.jikan.moe/v3/manga/119161/stats"
spyFamily_Search_URL = "https://api.jikan.moe/v3/search/manga?q=Spy_x_Family"

#-------------------------------------------------------------------#

#GET Request stats
spyFamily_Data = requests.get(spyFamily_Stats_URL)
print("Stats Status code =",spyFamily_Data.status_code)
#GET Request search
spyFamily_Data_Search = requests.get(spyFamily_Search_URL)
print("Search Status code =",spyFamily_Data_Search.status_code)

#Request Headers
spyFamily_Data_Header = json.dumps(dict(spyFamily_Data.headers))
#print(spyFamily_Data_Header)

spyFamily_Data_Search_Header = json.dumps(dict(spyFamily_Data_Search.headers))
#print(spyFamily_Data_Search_Header.text)

#--------------------------------------------------------------------#

#Reader Stats
spyFamily_Stats = spyFamily_Data.json()
#print(spyFamily_Stats)
spyFamily_Reading = spyFamily_Stats["reading"]
spyFamily_Completed = spyFamily_Stats["completed"]
spyFamily_OnHold = spyFamily_Stats["on_hold"]
spyFamily_Droppped = spyFamily_Stats["dropped"]
spyFamily_Plan = spyFamily_Stats["plan_to_read"]
spyFamily_Total = spyFamily_Stats["total"]

#print(spyFamily_Reading)
#print(spyFamily_Completed)

#Reader Status
spyFamily_Scores = spyFamily_Data.json()["scores"]
#print(spyFamily_Scores)

#Loops dict searching for votes
for indice_spyFamily_Scores in spyFamily_Scores:
    votos = spyFamily_Scores[indice_spyFamily_Scores]["votes"]
#    print(votos)
    spyFamily_Qnt_Votos.append(votos)

#Sum votes to get a total
spyFamily_Qnt_Votos_Total = sum(spyFamily_Qnt_Votos)

#-----------------------------------------------------------------------#

#Search Stats
spyFamily_Search = spyFamily_Data_Search.json()
#print(spyFamily_Search)

for indice_spyFamily_Search in spyFamily_Search["results"]:
    spyFamily_malId = indice_spyFamily_Search.get("mal_id")
#    print(spyFamily_malId)
    if spyFamily_malId == 119161:
        spyFamily_Members = indice_spyFamily_Search.get("members"),
        spyFamily_Score = indice_spyFamily_Search.get("score"),
        spyFamily_Chapters = indice_spyFamily_Search.get("chapters"),
        spyFamily_Volumes = indice_spyFamily_Search.get("volumes"),
        break

#---------------
