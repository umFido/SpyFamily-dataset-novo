import spyFamilyStats
import spyFamilyLog
import pandas as pd

#----------------------------------------------------------------------------------------#

#Criação de data frame e inclusão de linha no arquivo
mal_Data = {
    "Date":[spyFamilyStats.spyFamily_Date],
    "Members":[spyFamilyStats.spyFamily_Members[0]],
    "Score":[spyFamilyStats.spyFamily_Score[0]],
    "Chapters":[spyFamilyStats.spyFamily_Chapters[0]],
    "Volumes":[spyFamilyStats.spyFamily_Volumes[0]],
    "Reading":[spyFamilyStats.spyFamily_Reading],
    "Completed":[spyFamilyStats.spyFamily_Completed],
    "OnHold":[spyFamilyStats.spyFamily_OnHold],
    "Dropped":[spyFamilyStats.spyFamily_Droppped],
    "PlanToRead":[spyFamilyStats.spyFamily_Plan],
    "Total":[spyFamilyStats.spyFamily_Total]
}

#----------------------------------------------------------------------------------------#

#Ler arquivo CSV
abre_CSV = pd.read_csv(r"SF_MAL_Dataset.csv")
#print(lendoCSV)

# Acha a quantidade de registros na coluna Index
# e adiciona 1 ao indice que vai entrar na planilha 
SF_DataFrame_index = abre_CSV["Index"].size + 1

#---------------------------------------------------------------------#

#Exportando as informações para o CSV
SF_dataFrame = pd.DataFrame(mal_Data, index=[SF_DataFrame_index])
#print(SF_dataFrame)
SF_export_csv = SF_dataFrame.to_csv(r"SF_MAL_Dataset.csv", mode="a", header=False, line_terminator= "\r\n")
print("CSV atualizado com sucesso")