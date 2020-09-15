#Import de Requests et urlopen permettant de récuperer le contenu d'une page html
from urllib.request import Request, urlopen
import requests
#Import de BeautifulSoup permettant de parser une page html
from bs4 import BeautifulSoup

#
import time
import csv 

#Fonction qui permet de récuperer les paroles d'une chanson à partir de son url sur le site paroles.net
def get_paroles(lien):
    req = Request(lien, headers={'User-agent':'Opera/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
    response = urlopen(req).read()
    soup=BeautifulSoup(response,"html.parser")
    br=soup.findAll("br")
    return " ".join([b.next for b in br if b.next!="\n"]).replace("\n","")

    
#Liste des chanteurs dont on souhaite récupérer les chansons : à completer
liste_artistes=[]

#Liste qui contiendra les données scrappées. Un élément de la liste sera ainsi : {'chanteur':'nomChanteur', 'titre':'titreChanson', 'lien':'lienChanson', 'paroles':'parolesChanson}
liste_finale = []
chiffres=["1","2","3","4","5","6","7","8","9"]

#On répète les action ci-dessous autant de fois qu'il y a de chanteurs dans la liste liste_artistes:
for el in liste_artistes:
    #Construction de l'url qui mène a la liste des chansons d'un chanteur 
    url = "https://www.paroles.net/" + el
    #sur paroles.net, la liste des chansons pour un artiste est paginée. On récupère le nombre de page par artiste dans la variable nb.
    t1=requests.get(url+"-1000")
    time.sleep(20)
    t2 = t1.url[-1]
    if t2 in chiffres:
        nb = int(t1.url[-1])
    else:
        nb = 1
    #Une fois
    for n in range(1,nb+1):
        try:
            url2=url + "-" + str(n)
            req = Request(url2, headers={'User-agent':'Opera/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            time.sleep(90)
            response = urlopen(req).read()
            soup=BeautifulSoup(response,"html.parser")
            liste_chansons=soup.findAll("a", {"itemprop": "url"})
            for chanson in liste_chansons:
                dico = {}
                dico['chanteur'] = el
                dico['titre'] = chanson.text
                dico['lien'] = chanson['href']
                dico['paroles'] = get_paroles(dico['lien'])
                time.sleep(90)
                liste_finale.append(dico)
        except Exception as e:
            pass


keys = liste_finale[0].keys()
with open('chansons1.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(liste_finale)
