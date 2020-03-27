import requests

# Here we define our query as a multi-line string
query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: MANGA) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    stats {
      scoreDistribution {
        score
        amount
      }
      statusDistribution {
        status
        amount
      }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 108556
}

#------------------------------------------------------------------------------------------------#

#Variaveis
url = 'https://graphql.anilist.co'
AniList_StatusDistribution_amount = []
AniList_ScoreDistribution_amount = []

#API POST com Retorno
response = requests.post(url, json={'query': query, 'variables': variables})

print("Status - Status code =", response.status_code)
#print(response.json())

#------------------------------------------------------------------------------------------------#

AniList_stats_json = response.json()
#print(AniList_stats_json)

AniList_stats_ScoreDistribution = AniList_stats_json["data"]["Media"]["stats"]["scoreDistribution"]
AniList_stats_StatusDistribution = AniList_stats_json["data"]["Media"]["stats"]["statusDistribution"]

for score_index in AniList_stats_ScoreDistribution:
    #print("Printing Score")
    qnt_Score = score_index["amount"]
    AniList_ScoreDistribution_amount.append(qnt_Score)

for status_index in AniList_stats_StatusDistribution:
    #print("Printing Status")
    qnt_Status = status_index["amount"]
    AniList_StatusDistribution_amount.append(qnt_Status)
    
#Score 10, 30, 40, 50, 60, 70, 80, 90, 100
#print(AniList_ScoreDistribution_amount)
#CURRENT, PLANNING, COMPLETED, DROPPED, PAUSED
#print(AniList_StatusDistribution_amount)