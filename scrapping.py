from bs4 import BeautifulSoup
import requests



url = "https://www.paroles.net/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

