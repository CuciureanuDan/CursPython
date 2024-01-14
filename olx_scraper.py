"""
  Extragem din fisierul cu extensia .ini link-ul site-ului olx , numele produsului cautat 
"""

from configparser import ConfigParser
import requests
from bs4 import BeautifulSoup


def extragereNr(x):
    """
    Dintr-un sir de caractere extrage doar numerele
    
    Args:
        x (str) : un sir de caractere

    Return:
        int: Numerele extrase din sir
        -1: Daca nu exista numere

    """
    sir=''.join(c for c in x if c.isdigit())
    return int(sir) if sir else -1


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


produse=[]

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')

    divs = soup.find_all('div', class_='css-u2ayx9')
    #aceste divuri trebuie sortate in functie de pret , dar pretul trebuie extras numai cu cifre
    # o sa facem o lista cu dictionare care sa contina titlul si pretul , iar dupa o sa fie usor si de sortat 
    
    for div in divs:
        elem={}
        title = div.find('h6')
        price = div.find('p')
        elem['titlu'] = title.get_text()
        elem['pret'] = extragereNr(price.get_text())
        produse.append(elem)
else:
    print("Cererea nu a fost reusita. Cod de stare:", response.status_code)

    #facem sortarea si afisarea produselor in consola
if produse: 
    produse.sort(key=lambda x: x['pret'])
    for aux in produse:
        # print("Titlu: "+aux['titlu']+"\n"
        #       +"Pret: "+str(aux['pret'])+" lei" )
        print(f"Titlu:  {aux['titlu']} \n Pret: {aux['pret']} lei \n")




