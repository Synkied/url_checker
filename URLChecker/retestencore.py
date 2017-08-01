# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *








class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showChooseFile)
        
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        

    def showChooseFile(self):

        filename, ouvrir = QFileDialog.getOpenFileName(self, "Open File...", None,
                "Fichiers HTML (*.htm *.html);;Fichiers ePub (*.ePub);;Tous les fichiers (*)")
        
        File = open(filename, 'r', encoding='utf-8')
        
        with File:        
            data = File.read()
            self.textEdit.setText(data)  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
