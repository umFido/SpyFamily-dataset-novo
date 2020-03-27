import spyFamilyStats
import os

#---------------------------------------------------------------------------------------------------#
#Variable
date = spyFamilyStats.spyFamily_Date

header_request = "Request Header:"
json_request = "Request JSON:"


#Stats Header & Json
SF_D_Code = "Status code: " + str(spyFamilyStats.spyFamily_Data.status_code)
SF_D_H = spyFamilyStats.spyFamily_Data_Header
SF_D_Json = str(spyFamilyStats.spyFamily_Stats)
#Search Header & Json
SF_S_Code = "Status code: " + str(spyFamilyStats.spyFamily_Data_Search.status_code)
SF_S_H = spyFamilyStats.spyFamily_Data_Search_Header
SF_S_Json = str(spyFamilyStats.spyFamily_Search)

quebraLinha = "\n"

#Original dir
startDir = os.getcwd()

#---------------------------------------------------------------------------------------------------#
#Mudar o diretório dos Logs
#print(os.getcwd())
os.chdir("Log")
#print(os.getcwd())

#---------------------------------------------------------------------------------------------------#
#Cria arquivo
with open(date.strftime("%Y%m%d-%H%M%S")+".txt","w+", encoding="utf-8") as SF_Log:
    SF_buffer = ["Stats Request", SF_D_Code, header_request, SF_D_H, json_request, SF_D_Json,
                quebraLinha, 
                "Search Request", SF_S_Code, header_request, SF_S_H, json_request, SF_S_Json]
    SF_Log.writelines("%s\n" % line for line in SF_buffer)

#---------------------------------------------------------------------------------------------------#
#Volta para o diretório dos programas
os.chdir(startDir)
print("Log criado com sucesso")