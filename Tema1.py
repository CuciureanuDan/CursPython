"""
Un script care deschide un URL specificat de la tastatura si printeaza titlul paginii HTML si description meta.
"""

# importuri necesare
import requests
from bs4 import BeautifulSoup

def get_page_info(url):
    """
    Functie pentru a obtine informatii(titlu + description meta) despre o pagina web.

    Args:
        url (str): URL-ul paginii web.

    Returns:
        dict: Un dictionar continand titlul si descrierea paginii web.
        none: Afisare mesaj de eroare si codul de stare.
    """
    # realizeaza cererea HTTP
    response = requests.get(url)

    # verifica daca cererea a fost reusita
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        page_info = {
            'title': soup.title.text,   #extragem titlul presupunand ca orice pagina are tag de <title>
            'description': get_meta_description(soup)
        }

        return page_info
    else:
        print("Cererea nu a fost reusita. Cod de stare:", response.status_code)
        return None



def get_meta_description(soup):
    """
    Functie pentru a extrage description meta al unei pagini web.

    Args:
        soup (BeautifulSoup): Obiectul BeautifulSoup pentru pagina web.

    Returns:
        str: Continutul descrierii sau un mesaj de eroare daca tag-ul nu este gasit.
    """
    meta_description = soup.find('meta', attrs={'name': 'description'})
    # Verifica dacă exista meta description
    if meta_description:
        # Extrage continutul tag-ului meta
        return meta_description.get('content')
    else:
        return "Nu a fost gasit tag-ul meta description."

# e recomandat de folosit, ruleaza doar daca codul este rulat independent, nu ca modul al altui script
#if __name__ == "__main__":
   
# introducem url-ul de la tastatura
url = input("Introdu URL-ul: ")

# obtine titlul si description meta al paginii web
page_info = get_page_info(url)

# afiseaza informatiile despre pagina web
if page_info:
    print("Titlul paginii:", page_info['title'])
    print("Descrierea paginii:", page_info['description'])
