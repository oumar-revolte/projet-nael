import requests
from bs4 import BeautifulSoup
import csv
import json
url = "https://plan-comptable-ohada.com/nouvelle-norme-2016/plan-comptable-syscohada.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()[:1000] ) # Print the first 1000 characters of the HTML for inspection
titre=soup.title.string
print(titre)
res=soup.find(id="toc").find_all("a")
mes_donnees=list(x.string for x in res)
#(mes_donnees)
type_part, libelle_part = mes_donnees[0].split(" : ")
print(type_part)
print(libelle_part)
type_parts=type_part.split()
type, num= type_parts
print(type)
print(num)
classe=[]
print(mes_donnees)
for x in mes_donnees:
    type_part, libelle=x.split(" : ")
    numero=type_part.split()[1]
    if type_part.split()[0]=="CLASSE":
        c_dict=dict()
        c_dict["numero"]=numero
        c_dict["libelle"]=libelle
        classe.append(c_dict)
print(classe)