# -*-coding:utf-8 -*-

import sys
import subprocess
import re
import sys
import urllib.request
import urllib.parse
import win32com.client
from bs4 import BeautifulSoup
import os    


class extracteur(urllib.request.FancyURLopener):        #   Définir un autre UserAgent que celui défini par FancyURLopener (sous-classe)
    version = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36' # Useragent : http://whatsmyuseragent.com/


allFiles = os.listdir(os.getcwd())          #  Liste tous les fichiers du répertoire actuel

def processDir(allFiles):                   #  Dit d'analyser tous les fichiers du répertoire avec ProcessFile
    for url in allFiles:
        processFile(url)



def processFile(url):                       #  C'est ici qu'on définit comment l'url est analysé
    urllib._urlopener = extracteur()        #  Définir un autre UserAgent que celui défini par FancyURLopener
    extractor = extracteur()               #  Utiliser la sous-classe Extracteur() via une instance

    page = extractor.open(url)

    text = page.read()                      #  Lire l'intérieur de chaque page HTML
    page.close()                            #  Puis les fermer pour passer à la suivante

    soup = BeautifulSoup(text)              #  Définir un autre UserAgent que celui défini par FancyURLopener


    with open("links.html", "a", encoding='utf-8') as fichierUrl:  # Ici on écrit les url dans un fichier html, doc ou txt suivant l'extension choisie

        for tag in soup.findAll('a', href=True):                   # Trouve tous les "tag" <a> ayant pour attribut "href"

            tag['href'] = urllib.parse.urljoin(url, tag['href'])   # Créer un "dictionnaire" (liste) des tag href trouvés
                
            link = "<a href=\"{}\">{}</a><br/>".format(tag['href'], tag['href'])        # Récupérer les liens et les écrire sous forme de lien cliquables
            fichierUrl.write (link  + "\n")                                             # Ecrire les liens dans le fichier "links.html" avec un saut de ligne à chaque lien

    fichierUrl.close()



def main():                                  
    for url in sys.argv[0:]:            # Si au moins un des paramètres est rempli : exécuter le programme
        print()
        print("Extraction des liens...")
        print()
        processDir(allFiles)
        processFile(url)
        os.system("pause")