import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/manga/119161/Spy_x_Family/stats"
stats_page = requests.get(url)
cod_status = str(stats_page.status_code)

print("Status code = ", cod_status)

#Verificacao do status code
if cod_status[0] != "2":
    print("O codgio foi: ", cod_status)
    exit()

#Cria árvore de analise com a pagina coletada
soup = BeautifulSoup(stats_page.text,'html.parser')

#Classe geral: class = js-scrollfix-bottom-rel
#Classe dos stats: class = spaceit_pad

scrollfix_class = soup.find(class_="js-scrollfix-bottom-rel")

scrollfix_class_list = soup.find_all("div", class_="spaceit_pad")

#print()
#print("Stats")

MAL_list = []

#Formatando lista para extrair apenas os valores
for elemento in scrollfix_class_list:
    texto = elemento.text.replace(",","", 2)
    texto = texto.replace("(","")
    texto = texto.replace(")","")
    texto = texto.replace("%","")
    texto = texto.replace(":","")
    texto = texto.replace(u"\xa0",u"")
    texto = texto.replace(" votes","")
    texto = texto.replace(" to Read","")
    if texto.find("English") != -1 or texto.find("Japanese") != -1:
        continue
    MAL_list.append(texto)
#    print(texto)

#print("Set")
#print(MAL_list)

#print()

#Cria lista com itens do summary - Reading, Completed, On-Hold, Dropped, Plan, Total
#print("Summary")
summary_list = []

for elemento in MAL_list[0:6]:
    separa = elemento.split()
    summary_list.append(separa[1])

#print(summary_list)

#print()

#Cria lista com itens do score votes - valores vão do 10 ao 0
#print("Score")
#print("Votes")
score_votes_list = []

for elemento in MAL_list[6:]:
    separa = elemento.split()
    score_votes_list.append(separa[1])

#print(score_votes_list)

#print("")
#Cria lista com itens do score percent - valores vão do 10 ao 0
#print("Percent")
score_percent_list = []

for elemento in MAL_list[6:]:
    separa = elemento.split()
    score_percent_list.append(separa[0])

#print(score_percent_list)