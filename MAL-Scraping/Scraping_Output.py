import Stats_Scraping
import Statistics_Scraping
import datetime
import pandas as pd

MAL_date = datetime.datetime.now()
#---------------------Lendo Arquivos----------------------

abreSummary = pd.read_csv(r".\CSV\SF_Summary.csv")

abreScore = pd.read_csv(r".\CSV\SF_Score.csv")

abreStatistics = pd.read_csv(r".\CSV\SF_Statistics.csv")

#Pega tamanho do Index
Summary_Index = abreSummary["Index"].size + 1
Score_Index = abreScore["Index"].size + 1
Statistics_Index = abreStatistics["Index"].size + 1

#--------------------------Stats--------------------------
#Monta dicionários para dataframe
MAL_Summary = {
    "Date": MAL_date,
    "Reading": Stats_Scraping.summary_list[0],
    "Completed": Stats_Scraping.summary_list[1],
    "On_Hold": Stats_Scraping.summary_list[2],
    "Dropped": Stats_Scraping.summary_list[3],
    "Plan_To_Watch": Stats_Scraping.summary_list[4],
    "Total": Stats_Scraping.summary_list[5],
}
#print(MAL_Summary)

MAL_Score = {
    "Date": MAL_date,
    "10": Stats_Scraping.score_votes_list[0],
    "9": Stats_Scraping.score_votes_list[1],
    "8": Stats_Scraping.score_votes_list[2],
    "7": Stats_Scraping.score_votes_list[3],
    "6": Stats_Scraping.score_votes_list[4],
    "5": Stats_Scraping.score_votes_list[5],
    "4": Stats_Scraping.score_votes_list[6],
    "3": Stats_Scraping.score_votes_list[7],
    "2": Stats_Scraping.score_votes_list[8],
    "1": Stats_Scraping.score_votes_list[9]
}
#print(MAL_Score)

#MAL_Percent = {
#    "10": Stats_Scraping.score_percent_list[0],
#    "9": Stats_Scraping.score_percent_list[1],
#    "8": Stats_Scraping.score_percent_list[2],
#    "7": Stats_Scraping.score_percent_list[3],
#    "6": Stats_Scraping.score_percent_list[4],
#    "5": Stats_Scraping.score_percent_list[5],
#    "4": Stats_Scraping.score_percent_list[6],
#    "3": Stats_Scraping.score_percent_list[7],
#    "2": Stats_Scraping.score_percent_list[8],
#    "1": Stats_Scraping.score_percent_list[9]
#}
#print(MAL_Percent)

#DataFrame
df_Summary = pd.DataFrame(MAL_Summary, index = [Summary_Index])
#print(df_Summary)
df_Score = pd.DataFrame(MAL_Score, index = [Score_Index])

#df_Percent = pd.DataFrame(MAL_Percent, index = [0])

#--------------------Statistics--------------------
#Monta dicionário para dataset
MAL_Statistics = {
    "Date": MAL_date,
    "Score": Statistics_Scraping.statistics_Score,
    "Users_Scored": Statistics_Scraping.statistics_Users,
    "Rank": Statistics_Scraping.statistics_Rank,
    "Popularity": Statistics_Scraping.statistics_Pop,
    "Members": Statistics_Scraping.statistics_Memb,
    "Favorites": Statistics_Scraping.statistics_Fav
}
#print(MAL_Statistics)

#DataFrame
df_Statistics = pd.DataFrame(MAL_Statistics, index = [Statistics_Index])

#-----------------Exportando CSV-------------------
summary_export_csv = df_Summary.to_csv(r'.\CSV\SF_Summary.csv', mode="a", header=False, line_terminator= "\r\n")
score_export_csv = df_Score.to_csv(r'.\CSV\SF_Score.csv', mode="a", header=False, line_terminator= "\r\n")
statistics_export_csv = df_Statistics.to_csv(r'.\CSV\SF_Statistics.csv', mode="a", header=False, line_terminator= "\r\n")

print("CSVs foram criados")