import csv, random
import pandas as pd
from sklearn.model_selection import train_test_split


lyrics = pd.read_csv('/home/fitec/Téléchargements/lyrics_final.csv', sep=';', names = ["Identifiant","Artiste", "Titre", "Lien", "Paroles"])
df = pd.DataFrame(lyrics)
lyrics["Artiste"].value_counts() # nombre d'entrées pour chaque chanteur

""" sss = StratifiedShuffleSplit(n_splits=10, test_size=0.1, random_state = 0)# 
strat_test_set = []
for ech_index in sss.split(lyrics, lyrics["Artiste"]):
    strat_test_set.append(ech_index) """



ech1, ech2 = train_test_split(lyrics, stratify=lyrics['Artiste'], test_size=500)
#ech2.to_csv("ech_a_labeliser.csv", sep=";", index=False, header=True)



choix=[0,1,2,3]
liste=[]
for i in range(500):
	liste.append(random.sample(choix,4))
	
dispatch=pd.DataFrame(liste, columns=["Hannankhan", "Yacine","Fatou","Youssef"])

dispatch.reset_index(drop=True, inplace=True)
ech2.reset_index(drop=True, inplace=True)

a_labeliser= pd.concat([ech2, dispatch], axis=1)
a_labeliser.to_csv("/home/fitec/Téléchargements/ech_a_labeliser.csv", sep=";",header=True)
