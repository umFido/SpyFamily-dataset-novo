import AniList_Stats
import AniList_Ranking
import datetime
import pandas as pd
#---------------------------------------------------------------------------------------------------#
AniList_Date = datetime.datetime.now()
AniList_Index = 0

#---------------------------------------------------------------------------------------------------#
AniList_Dict = {
    "Date": AniList_Date,
    "Current": AniList_Stats.AniList_StatusDistribution_amount[0],
    "Planning": AniList_Stats.AniList_StatusDistribution_amount[1],
    "Completed": AniList_Stats.AniList_StatusDistribution_amount[2],
    "Dropped": AniList_Stats.AniList_StatusDistribution_amount[3],
    "Paused": AniList_Stats.AniList_StatusDistribution_amount[4],

    "Average": AniList_Ranking.AniList_Rank_Avg,
    "Mean": AniList_Ranking.AniList_Rank_Mean,
    "Favourites": AniList_Ranking.AniList_Rank_Fav,
    "Popularity": AniList_Ranking.AniList_Rank_Pop,
    
    "H._AllTime": AniList_Ranking.AniList_Rank_HighAllTime,
    "Pop._AllTime": AniList_Ranking.AniList_Rank_PopularAllTime,
    "H._2019": AniList_Ranking.AniList_Rank_High2019,
    "Pop._2019": AniList_Ranking.AniList_Rank_Popular2019,

    "Score_10": AniList_Stats.AniList_ScoreDistribution_amount[0],
    "Score_30": AniList_Stats.AniList_ScoreDistribution_amount[1],
    "Score_40": AniList_Stats.AniList_ScoreDistribution_amount[2],
    "Score_50": AniList_Stats.AniList_ScoreDistribution_amount[3],
    "Score_60": AniList_Stats.AniList_ScoreDistribution_amount[4],
    "Score_70": AniList_Stats.AniList_ScoreDistribution_amount[5],
    "Score_80": AniList_Stats.AniList_ScoreDistribution_amount[6],
    "Score_90": AniList_Stats.AniList_ScoreDistribution_amount[7],
    "Score_100": AniList_Stats.AniList_ScoreDistribution_amount[8],
}
#print(AniList_Dict)


#---------------------------------------------------------------------------------------------------#
#Lendo arquivo
abreCSV = pd.read_csv(r"AniList.csv")
AniList_Index = abreCSV["Index"].size + 1

#---------------------------------------------------------------------------------------------------#
#Criar DataFrame
AniList_DF = pd.DataFrame(AniList_Dict, index=[AniList_Index],)
#print(AniList_DF)

#---------------------------------------------------------------------------------------------------#
#Exportar para o CSV
AniList_toCSV = AniList_DF.to_csv("AniList.csv", mode="a", header=False, line_terminator="\r\n")
print("CSV atualizado")

#---------------------------------------------------------------------------------------------------#