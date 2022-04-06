from bs4 import BeautifulSoup
import requests
import pandas as pd

url= "https://www.cyberpuerta.mx/Audio-y-Video/Audio-y-MP3/Audifonos/1/"
page= requests.get(url)
soup= BeautifulSoup(page.content, 'html.parser')

#Contenedores
#title= soup.find_all('div', class_= 'emproduct_right')
containers= soup.find_all('div', {'class':'emproduct clear listitemline emsmoothhover2'})
print(containers[0])
#gitdemo