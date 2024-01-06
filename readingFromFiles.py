
"""
Adaugam posibilitatea de a citi link-uri dintr-un fisier de configurare de tip .ini
"""

from configparser import ConfigParser

from web_info_extractor import get_page_info



config = ConfigParser()

config.read("site_urls.ini")

keys = config.options('website')

urls = [config.get('website', key) for key in keys]

print("In fisierul dat sunt %d URL-uri." %(len(urls)))
for x in urls:
    page_info = get_page_info(x)
    print("Site: "+ x + "\n"
          +"TITLE: "+ page_info['title']+"\n"
          +"DESCRIPTION META:  "+ page_info['description']+"\n")

#print('\n'.join(urls))

