import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTranslator
from main import *


passwdApp = QApplication(sys.argv)

translator = QTranslator()
translator.load("Billal")
passwdApp.installTranslator(translator)

win = Main()
win.show()

rc = passwdApp.exec_()
sys.exit(rc)

