# -*-coding:utf-8 -*-

import re
import sys
import urllib.request
import urllib.parse
import win32com.client
from bs4 import BeautifulSoup
import os

class Extracteur(urllib.request.FancyURLopener):  
    version = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36' # Useragent : http://whatsmyuseragent.com/




def process(url):                       #  C'est ici qu'on définit comment l'url est analysé
    urllib._urlopener = Extracteur()
    extracteur = Extracteur()

    page = extracteur.open(url)

    text = page.read()
    page.close()

    bs = BeautifulSoup(text)




    with open("links.html", "a") as fichierUrl:  # Ici on écrit les url dans un fichier html, doc ou txt suivant l'extension choisie

        for tag in bs.findAll('a', href=True):
            tag['href'] = urllib.parse.urljoin(url, tag['href'])
            print(tag['href'])

            link = "<a href=\"{}\">{}</a><br/>".format(tag['href'], tag['href'])
            
            fichierUrl.write (link  + "\n")

    fichierUrl.close()



def rename():                                   # NON UTILISE POUR LE MOMENT

    folder = 'C:/Users/synkx_000/Documents/Créations/Python/Urlextractor'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.rtf', '.doc')
        output = os.rename(infilename, newname)


def convertHTML(htmlFile):

    MSWord = win32com.client.Dispatch('Word.Application')

    docfile = MSWord.Documents.Add('C:/Users/synkx_000/Documents/Créations/Python/Urlextractor/test.doc')
    docfile.SaveAs('C:/Users/synkx_000/Documents/Créations/Python/Urlextractor/test.html', FileFormat=8)
    docfile.Close()

    MSWord.Quit()


def main():                             #  Ici, 
    if len(sys.argv) == 1:
        print("Extracteur de liens v0.3")
        print("Usage: %s URL [URL]..." % sys.argv[0])
        os.system("pause")

    for htmlFile in sys.argv[1:]:            # Sinon, si au moins un des paramètres est rempli
        convertHTML(htmlFile)
        print()
        print("=" * 70)
        print("Extracteur de liens v0.3".upper().center(70))
        print("=" * 70)
        print()
        print("Document converti en HTML ! ")
        print()               


    for url in sys.argv[1:]:            # Sinon, si au moins un des paramètres est rempli
        print()
        print("Voici les liens présents au sein de cette page : ")
        print()
        process(url)
# main()

if __name__ == "__main__":
    main()


# COPYRIGHT QUENTIN LATHIERE 2014-2015 (ou pas)