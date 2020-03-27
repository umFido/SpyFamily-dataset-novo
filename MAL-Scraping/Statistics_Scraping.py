import requests
import Stats_Scraping
from bs4 import BeautifulSoup

#url = "https://myanimelist.net/manga/119161/Spy_x_Family/stats"

#stats_page = requests.get(url)
#cod_status = str(stats_page.status_code)

#print("Status code = ", cod_status)

#Verificacao do status code
#if cod_status[0] != "2":
#    print("O codgio foi: ", cod_status)
#    exit()

#Cria árvore de analise com a pagina coletada
soup = BeautifulSoup(Stats_Scraping.stats_page.text,'html.parser')

#Classe geral = js-scrollfix-bottom
extrai_scrollfix = soup.find(class_ = "js-scrollfix-bottom")
#print(extrai_scrollfix)

extrai_div = extrai_scrollfix.find_all("div")
#print(extrai_div)

limparLista = []

for elemento in extrai_div[14:]:
    extrai_text = elemento.text.replace(",","")
    extrai_text = extrai_text.strip()
    limparLista.append(extrai_text)

#Limpa lista e mantem Score, Ranked, Popularity, Members e Favorites
limparLista.pop(1)
limparLista.pop(2)
limparLista.pop()
limparLista.pop()
limparLista.pop()

#print(limparLista)

primeiro_Registro = limparLista[0]
statistics_Score = primeiro_Registro[7:12]
#print(statistics_Score)
statistics_Users = primeiro_Registro[24:28]
#print(statistics_Users)

segundo_Registro = limparLista[1]
statistics_Rank = segundo_Registro[9:12]
#print(statistics_Rank)

terceiro_Registro = limparLista[2]
statistics_Pop = terceiro_Registro[-3:]
#print(statistics_Pop)

quarto_Registro = limparLista[3]
statistics_Memb = quarto_Registro[-5:]
#print(statistics_Memb)

quinto_Registro = limparLista[4]
statistics_Fav = quinto_Registro[-4:]
#print(statistics_Fav)

#ratingV = extrai_scrollfix.find("span", itemprop_="ratingValue")
#print(ratingV)

#ratingC = extrai_scrollfix.find("span", itemprop_="ratingCount")
#print(ratingC)