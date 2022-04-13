from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cyberpuerta.mx/Audio-y-Video/Audio-y-MP3/Audifonos/1/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.find_all('div', {'class': 'emproduct clear listitemline emsmoothhover2'})

filename = "Audifonos.csv"
f = open(filename, "w")

headers = "Marca\n"

f.write(headers)


for container in containers:
    marca_container = container.findAll("div", {"class": "badges-left"})
    marca = marca_container[0].img["alt"].title()
    f.write(marca + "\n")