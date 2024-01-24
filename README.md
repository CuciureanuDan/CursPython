# Proiectul Web Scraper

Acest proiect contine mai multe scripturi Python pentru extragerea informatiilor de pe internet, configurate si personalizate in functie de diferite scenarii.
Mai jos sunt detaliile si instructiunile pentru fiecare script.

## Prerequisites
To install these requirements, run the following commands:
Pentru a instala pachetele necesare , ruleaza urmatoarele comenzi: 
```bash
# Upgrade pip to the latest version
python -m pip install -U pip

# Install the required packages
pip install -r requirements.txt
```

# Configurare

1. web_info_extractor.py - Deschide un URL specificat la tastatura si afiseaza titlul si descrierea meta doar cand codul este rulat independent.
```python
python web_info_extractor.py 
```

2. readingFromFiles.py - Permite specificarea URL-ului într-un fisier de configurare de tip .ini numit site_urls.ini.
```python
python readingFromFiles.py 
```

3. olx_scraper.py - Afiseaza la consola titlul si preturile de pe olx.ro pentru cuvintele cheie 'iphone 15 pro', ordonate crescator dupa pret. Informatiile sunt citite din fisierul .ini.
```python
# doar pentru o simpla afisare a preturilor crescator
python olx_scraper.py 

# si pentru adaugarea timpului necesar fiecarui request catre site-ul din .ini
python olx_scraper.py -log
```

4. mailer.py - Modul pentru trimiterea de e-mail-uri, accesat din olx_scraper.py

5. Proiectul utilizează un fisier de configurare de tip .ini pentru a gestiona diferite setari. Fisierul relevant este 'site_urls.ini'.

6. EmailData.ini - Creati un fisier EmailData.ini cu urmatorul continut pentru configurarea datelor de e-mail:

```ini
[credentials]
email = adresa.email@example.com
password = parolaEmail
```
**Nota**: Asigurati-va ca acest fisier este protejat si nu este distribuit public.
