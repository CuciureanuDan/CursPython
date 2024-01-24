"""
  Extragem din fisierul cu extensia .ini link-ul site-ului olx , numele produsului cautat 

  Am adaugat posibilitatea folosirii parametrului -log pentru afisarea timpului necesar fiecarui request

  Am adaugat posibilitatea trimiterii unui email daca in 'site_urls.ini' exista un pret si un email al destinatarului si daca exista vreun produs sub acel pret 
"""

from configparser import ConfigParser
import requests
import argparse
from bs4 import BeautifulSoup
from mailer import send_email


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


def time_decorator(func):
    def modificare(*pargs, **kargs):
        result = func(*pargs, **kargs)
        if args.log:
            print(f"Timpul necesar pentru request: {result.elapsed.total_seconds()} secunde\n\n")
        return result
    return modificare


parser = argparse.ArgumentParser()
parser.add_argument("-log", help="Introduce timpul necesar fiecarui request",action="store_true")
args = parser.parse_args()



config = ConfigParser()

config.read('site_urls.ini')

link = config['olx']['url']
produs = config['olx']['produs']
url = link + produs


check_send_email = False

#verificam daca exista date posibile pentru trimiterea email-ului

if 'email' in config and 'dest' in config['email'] and config['email']['dest']:
        if 'limite de pret' in config and 'pret' in config['limite de pret'] and config['limite de pret']['pret']:
            check_send_email = True
            dest = config['email']['dest']
            lim = extragereNr( config['limite de pret']['pret'] )


@time_decorator
def cerere(url):
    return requests.get(url , timeout=2)

response = cerere(url)

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


if check_send_email:

    #verifica daca exista vreun produs e sub limita ceruta de pret
    #Daca produsul nu are pret afisat, el va primi valoarea '-1' , am facut si o verificare pentru asta
    #As putea elimina si problema in care daca sunt accesorii de vanzare facand any() asa: any(produs['pret'] <= lim and produs['pret'] > 1000 for produs in produse)
    #Dar daca modific asa as strica verificarea pentru alte produse 

    if any(produs['pret'] <= lim and produs['pret'] > 1000 for produs in produse):
        send_email(dest,produs,lim)
    else:
        print(f"\n Nu exista produse cu pretul sub {lim} lei.")
    
    
    #produsele_cautate = [produs for produs in produse if produs['pret'] < lim] #pentru viitoare implementari, sa si afisam numele si pretul. Poate si un link?
