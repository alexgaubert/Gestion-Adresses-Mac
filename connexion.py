import sqlite3

def connecter(self):
    self.connexion = sqlite3.connect('gestion_adresse_mac.db')
    self.requete = self.connexion.cursor()

def deconnecter(self):
    self.connexion.commit()
    self.db.close()

