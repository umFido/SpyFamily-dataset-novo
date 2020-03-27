import requests

# Here we define our query as a multi-line string
query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    averageScore
    meanScore
    favourites
    popularity
    rankings {
      id
      rank
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 108556
}

#--------------------------------------------------------------------------------------------------#

#Definir variaveis
url = 'https://graphql.anilist.co'

#API POST com Retorno
response = requests.post(url, json={'query': query, 'variables': variables})
print("Ranking - Status code =", response.status_code)

AniList_Rank_json = response.json()
#print(AniList_Rank_json)

AniList_Rank_Avg = AniList_Rank_json["data"]["Media"]["averageScore"]
AniList_Rank_Mean = AniList_Rank_json["data"]["Media"]["meanScore"]
AniList_Rank_Fav = AniList_Rank_json["data"]["Media"]["favourites"]
AniList_Rank_Pop = AniList_Rank_json["data"]["Media"]["popularity"]
#print(AniList_Rank_Avg)

AniList_Rank_HighAllTime = AniList_Rank_json["data"]["Media"]["rankings"][0]["rank"]
AniList_Rank_PopularAllTime = AniList_Rank_json["data"]["Media"]["rankings"][1]["rank"]
AniList_Rank_High2019 = AniList_Rank_json["data"]["Media"]["rankings"][2]["rank"]
AniList_Rank_Popular2019 = AniList_Rank_json["data"]["Media"]["rankings"][3]["rank"]