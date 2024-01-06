# """
# Extragem din fisierul cu extensia .ini link-ul site-ului olx , numele produsului cautat 
# """

from configparser import ConfigParser
import requests
from bs4 import BeautifulSoup

config = ConfigParser()

config.read('site_urls.ini')

link = config['olx']['url']
produs = config['olx']['produs']

url = link + produs

response = requests.get(url)

  # divurile ce contin titlul si pretul sunt de forma urmatoare 
#<div class="css-u2ayx9">
#<h6 class="css-16v5mdi er34gjf0">iPhone 15 ProMax, 512 gb, blue, sigilat</h6>
#<p data-testid="ad-price" class="css-10b0gli er34gjf0">7 300 lei</p>  # pe langa lei poate sa contina si alte caractere
#</div>




if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')



else:
    print("Cererea nu a fost reusita. Cod de stare:", response.status_code)




