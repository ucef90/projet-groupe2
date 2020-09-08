from bs4 import BeautifulSoup
import requests



url = "https://www.paroles.net/"

r = requests.get(url)
print(dir(r))
soup = BeautifulSoup(r)
print(soup)
