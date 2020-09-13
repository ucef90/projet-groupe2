#Import de Requests et urlopen permettant de récuperer le contenu d'une page html
from urllib.request import Request, urlopen
import requests
#Import de BeautifulSoup permettant de parser une page html
from bs4 import BeautifulSoup

#
import time

#Fonction qui permet de récuperer les paroles d'une chanson à partir de son url sur le site paroles.net
def get_paroles(lien):
    req = Request(lien, headers={'User-agent':'Firefox/5.0'})
    response = urlopen(req).read()
    soup=BeautifulSoup(response,"html.parser")
    br=soup.findAll("br")
    return " ".join([b.next for b in br if b.next!="\n"]).replace("\n","")

    
#Liste des chanteurs dont on souhaite récupérer les chansons : à completer
liste_artistes=['kery-james',	'Rim-K',	'damso',	'youssoupha',	'Soprano',	'Orelsan',	'H-MAGNUM',	'dosseh',	'Scylla',	'booba',	'Rohff',	'Kaaris',	'nick-conrad',	'NTM',	'Doc-Gyneco',	'Lunatic',	'VII',	'ninho',	'nekfeu',	'georgio',	'vald',	'sultan',	'kaaris',	'bigflo-oli',	'hayce-lemsi',	'pnl',	'lacrim',	'mister-you',	'jul',	'sch',	'guizmo',	'sexion-d-assaut',	'ntm',	'oxmo-puccino',	'iam',	'sniper',	'sinik',	'mac-tyer',	'sefyu']

#Liste qui contiendra les données scrappées. Un élément de la liste sera ainsi : {'chanteur':'nomChanteur', 'titre':'titreChanson', 'lien':'lienChanson', 'paroles':'parolesChanson}
liste_finale = []

#On répète les action ci-dessous autant de fois qu'il y a de chanteurs dans la liste liste_artistes:
for el in liste_artistes:
    #Construction de l'url qui mène a la liste des chansons d'un chanteur 
    url = "https://www.paroles.net/" + el
    #sur paroles.net, la liste des chansons pour un artiste est paginée. On récupère le nombre de page par artiste dans la variable nb.
    nb = int(requests.get(url+"-1000").url[-1])
    #Une fois 
    for n in range(1,nb+1):
        try:
            url2=url + "-" + str(n)
            req = Request(url2, headers={'User-agent':'Firefox/5.0'})
            response = urlopen(req).read()
            soup=BeautifulSoup(response,"html.parser")
            liste_chansons=soup.findAll("a", {"itemprop": "url"})
            for chanson in liste_chansons:
                dico = {}
                dico['chanteur'] = el
                dico['titre'] = chanson.text
                dico['lien'] = chanson['href']
                dico['paroles'] = get_paroles(dico['lien'])
                liste_finale.append(dico)
                time.sleep(15)
        except e:
            print(e)


