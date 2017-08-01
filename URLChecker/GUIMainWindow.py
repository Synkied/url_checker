# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import re
import urllib.request
import urllib.parse
import win32com.client
from bs4 import BeautifulSoup
import os
from GUIOpenFile import * 
from GUIQt import*   


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






class MainWindow(QMainWindow):
    
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.form_widget = formWidget(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.form_widget)
        self.setCentralWidget(_widget)

        self.initUI()
        
        	
    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('URLChecker permet d\'extraire et traiter les URL de différents fichiers.')    
        
        #General definition of the window
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('URLChecker')
        self.setWindowIcon(QIcon('img/urlchecker_icon.png'))    
        self.show()
        #General definition of the window

        #Behavior of the options in the MenuBar
        openFile = QAction(QIcon('img/openFile.png'), '&Contrôler un fichier...', self)        
        openFile.setShortcut('Ctrl+N')
        openFile.triggered.connect(choseFileWindow)

        launchAction = QAction(QIcon('img/play.png'),'&Reprendre', self)        
        launchAction.setShortcut('Ctrl+G')
        launchAction.setStatusTip('Reprendre')
        launchAction.triggered.connect(processFile)

        pauseAction = QAction(QIcon('img/pause.png'),'&Pause', self)        
        pauseAction.setShortcut('Ctrl+G')
        pauseAction.setStatusTip('Pause')
        pauseAction.triggered.connect(processFile)

        stopAction = QAction(QIcon('img/stop.png'),'&Stop d\'urgence', self)        
        stopAction.setShortcut('Ctrl+G')
        stopAction.setStatusTip('Stop d\'urgence')
        stopAction.triggered.connect(processFile)

        exitAction = QAction(QIcon('img/sortie.png'),'&Quitter', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quitter l\'application')
        exitAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon('img/edit.png'), '&Préférences...', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Accéder aux préférences du logiciel')
        editAction.triggered.connect(qApp.quit)
        #Behavior of the options in the MenuBar
        
        menubar = self.menuBar()
        #Create + instance menuBar

        #Add MenuBar buttons
        shortcutMenuBar = menubar.addMenu('&Fichier')
        shortcutMenuBar.addAction(openFile)
        shortcutMenuBar.addAction(exitAction)
        
        editMenu = menubar.addMenu('&Options')
        editMenu.addAction(editAction)
        #Add MenuBar buttons

        #Add ToolBar buttons
        self.toolbar = self.addToolBar('')
        self.toolbar.addAction(openFile)

        self.toolbar.addSeparator()

        self.toolbar.addAction(launchAction)
        self.toolbar.addAction(pauseAction)
        self.toolbar.addAction(stopAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(exitAction)
        self.toolbar.setIconSize(QSize(14,14))
        #Add ToolBar buttons

        self.statusBar()
        #Create StatusBar
        
        self.statusBar().showMessage('Prêt pour l\'utilisation')
        #Default text on the StatusBar of the application


        
        
    def showChooseFile(self):

        filename = QFileDialog.getOpenFileName(self, "Open File...", None,
                "Fichiers HTML (*.htm *.html);;Fichiers ePub (*.ePub);;Tous les fichiers (*)")
        
        File = open(filename, 'r', encoding='utf-8')
        
        with File:        
            data = File.read()
            self.textEdit.setText(data)


    def closeEvent(self, event):
        """Quit event by clicking on the X in the top right corner of the window"""
        
        reply = QMessageBox.question(self, 'Quitter ?',
            "Êtes-vous sûr de vouloir quitter ?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
        	event.accept()
        else:
        	event.ignore()
            	

    def center(self):
        """Centering the windows of the app"""
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class formWidget(QWidget):
    """Widget dans la fenêtre centrale"""

    def __init__(self, parent):
        super(formWidget, self).__init__(parent)
        self.controls()

    def controls(self):
        btnOpenWin = QPushButton("Choisir un fichier...")

        btnOpenWin.clicked.connect(choseFileWindow)


        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)

        self.hbox.addWidget(btnOpenWin)

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()








