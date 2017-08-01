
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip, QApplication, QMessageBox, QDesktopWidget,
 QMainWindow, QAction, qApp, QTextEdit, QFileDialog, QPushButton, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QFont, QIcon)
import subprocess  

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.form_widget)
        self.setCentralWidget(_widget)

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        self.label = QLabel("Name for backdrop")
        self.txted = QLineEdit()
        self.lbled = QLabel("Select a readNode")
        self.cmbox = QComboBox()
        

    def __layout(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.h2Box = QHBoxLayout()

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.txted)

        self.h2Box.addWidget(self.lbled)
        self.h2Box.addWidget(self.cmbox)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h2Box)
        self.setLayout(self.vbox)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 