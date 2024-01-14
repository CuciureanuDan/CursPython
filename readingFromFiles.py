
"""
Adaugam posibilitatea de a citi link-uri dintr-un fisier de configurare de tip .ini
"""

from configparser import ConfigParser

from web_info_extractor import get_page_info

#aceasta functie a tinut de tema2
def extragere_from_ini(inifile):
    """
       Functie pentru extragere dintr-un fisier cu extensie .ini 
       Fisierul trebuie sa contina o sectiune 'website' cu chei(keys) a caror valoare(values) sa fie link-uri
       Functia va afisa numarul de link-uri din fisier, link-ul si Title & Description Meta a paginii web

       Args:
         inifile (str) : numele fisierului 

       Returns: nu returneaza nimic 
    """

    config = ConfigParser()

    #adauga un try pentru eventuale scrieri gresite de fisier
    config.read(inifile)

    keys = config.options('website')

    urls = [config.get('website', key) for key in keys]

    print("In fisierul dat sunt %d URL-uri." %(len(urls)))
    for x in urls:
        page_info = get_page_info(x)
        print("Site: "+ x + "\n"
              +"TITLE: "+ page_info['title']+"\n"
             +"DESCRIPTION META:  "+ page_info['description']+"\n")
    #print('\n'.join(urls))


if __name__ == "__main__": 

    #pentru testarea functiei
    extragere_from_ini("site_urls.ini")




