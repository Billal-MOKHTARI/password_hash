from getpass import getpass
import hashlib
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from mot_de_passe import *

class Main(Ui_PasswordApp, QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.action_Quitter.triggered.connect(self.quitter)
        self.pushButtonPassword.clicked.connect(self.generer)


    def quitter(self):
        boite_de_dialogue = QMessageBox.question(self, "Confirmation", "Voulez-vous quitter l'application ?",
                                                 QMessageBox.Yes, QMessageBox.No)
        if boite_de_dialogue == 16384 :
            self.close()

    def generer(self):
        mot_de_passe = self.lineEditPassword.text().encode()
        type_chiffrement = self.comboBoxChiffrement.currentText()

        if type_chiffrement == "sha1" :
            msg_chiffre = hashlib.sha1(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)
        elif type_chiffrement == "sha224" :
            msg_chiffre = hashlib.sha224(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)
        elif type_chiffrement == "sha256" :
            msg_chiffre = hashlib.sha256(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)
        elif type_chiffrement == "sha512" :
            msg_chiffre = hashlib.sha512(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)
        elif type_chiffrement == "sha384" :
            msg_chiffre = hashlib.sha384(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)
        else :
            msg_chiffre = hashlib.md5(mot_de_passe).hexdigest()
            self.labelPassword.setText(msg_chiffre)