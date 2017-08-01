# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUIMainWindow import *


class choseFileWindow(QWidget):
    
    def __init__(self):
        super(choseFileWindow, self).__init__()
        
        self.initUIWidget()
        
    def initUIWidget(self):      

        self.btnOpenFile = QPushButton('Choisir un fichier...', self)
        self.btnOpenFile.move(272, 50)
        self.btnOpenFile.clicked.connect(self.showChooseFile)
        
        titleEdit = QLineEdit(self)
        titleEdit.move(20,22)
        titleEdit.setFixedWidth(350)

        
        self.setFixedSize(400, 400)
        self.center()
        self.setWindowTitle('Choisir un fichier à traiter')
        

        self.btnLaunch = QPushButton('Lancer l\'extracteur', self)
        self.btnLaunch.resize(self.btnLaunch.sizeHint())
        self.btnLaunch.move(190, 350)
        self.btnLaunch.clicked.connect(lambda:self.run(''))
        self.btnLaunch.hide()
        #Bouton qui bug nécessaire à l'ouverture de la fenêtre à partir de la fenêtre principale...

        self.btnLaunch = QPushButton('Lancer l\'extracteur', self)
        self.btnLaunch.resize(self.btnLaunch.sizeHint())
        self.btnLaunch.move(190, 350)
        self.btnLaunch.clicked.connect(processFile)

        self.btnCancel = QPushButton('Annuler', self)
        self.btnCancel.resize(self.btnCancel.sizeHint())
        self.btnCancel.move(295, 350)
        self.btnCancel.clicked.connect(self.cancelEvent)       
 
        self.show()
        #Show the Window and everything included
        

    def showChooseFile(self):

        filename = QFileDialog.getOpenFileName(self, "Open File...", None,
                "Fichiers HTML (*.htm *.html);;Fichiers ePub (*.ePub);;Tous les fichiers (*)")
        
        File = open(filename, 'r', encoding='utf-8')
        
        with File:        
            data = File.read()
            self.textEdit.setText(data) 

    def center(self):
        """Centering the windows of the app"""
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):
               
        if e.key() == Qt.Key_Escape:
            self.close()

    def cancelEvent(self):
        self.deleteLater()          
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cFW = choseFileWindow()
    sys.exit(app.exec_())
