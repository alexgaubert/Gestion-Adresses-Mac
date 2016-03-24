# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from Ui_fenetre import Ui_Form
import connexion
import requetes
import dictionnaires
import fonctions

class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        
        connexion.connecter(self)
        requetes.init(self)
        dictionnaires.init(self)
        
        self.ligne = 0
        
        for nom in self.dic_cbB_nom.values():
            if nom != '':
                self.cbB_proprietaire.addItem(nom)
        
        for i in range(1, self.nb_app + 1):
            if self.dic_tw_app[i] != '':
                self.ligne += 1
                self.tW_bd.setRowCount(self.ligne)
                self.tW_bd.setItem(self.ligne - 1, 0, QTableWidgetItem(self.dic_tw_app[i]))
                self.tW_bd.setItem(self.ligne - 1, 1, QTableWidgetItem(self.dic_tw_adr[i]))
                self.tW_bd.setItem(self.ligne - 1, 2, QTableWidgetItem(self.dic_tw_nom[i]))
    
    @pyqtSlot(str)
    def on_lE_proprietaire_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        if self.lE_proprietaire.text() != '':
            self.pB_activer_ajouter.setEnabled(True)
        else:
            self.pB_activer_ajouter.setEnabled(False)
    
    @pyqtSlot()
    def on_pB_activer_ajouter_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.pB_activer_ajouter.text() == '+' and self.pB_supprimer_annuler.text() == '-':
            
            self.cbB_proprietaire.hide()
            self.pB_activer_ajouter.setEnabled(False)
            self.pB_supprimer_annuler.setText('x')
            
        elif self.pB_activer_ajouter.text() == '+' and self.pB_supprimer_annuler.text() == 'x':
            
            if not self.lE_proprietaire.text() in self.dic_cbB_nom.values():
                self.cbB_proprietaire.addItem(self.lE_proprietaire.text())
                self.dic_cbB_nom[fonctions.getMax(self) + 1] = self.lE_proprietaire.text()
            
            self.lE_proprietaire.setText('')
            self.cbB_proprietaire.show()
            self.pB_activer_ajouter.setEnabled(True)
            self.pB_supprimer_annuler.setText('-')
            
        elif self.pB_activer_ajouter.text() == '-' and self.pB_supprimer_annuler.text() == 'x':
            
            for cle in self.dic_cbB_nom:
                if self.dic_cbB_nom[cle] == self.cbB_proprietaire.currentText():
                    self.cbB_proprietaire.removeItem(self.cbB_proprietaire.currentIndex())
                    del self.dic_cbB_nom[cle]
                    break
            
            self.cbB_proprietaire.setEnabled(True)
            self.pB_activer_ajouter.setText('+')
            self.pB_supprimer_annuler.setText('-')
    
    @pyqtSlot()
    def on_pB_supprimer_annuler_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.pB_activer_ajouter.text() == '+' and self.pB_supprimer_annuler.text() == '-':
            
            self.cbB_proprietaire.setEnabled(False)
            self.pB_activer_ajouter.setText('-')
            self.pB_supprimer_annuler.setText('x')
            
        elif self.pB_activer_ajouter.text() == '-' and self.pB_supprimer_annuler.text() == 'x':
            
            self.cbB_proprietaire.setEnabled(True)
            self.pB_activer_ajouter.setText('+')
            self.pB_supprimer_annuler.setText('-')
            
        elif self.pB_activer_ajouter.text() == '+' and self.pB_supprimer_annuler.text() == 'x':
            
            self.lE_proprietaire.setText('')
            self.cbB_proprietaire.show()
            self.pB_activer_ajouter.setEnabled(True)
            self.pB_supprimer_annuler.setText('-')
    
    @pyqtSlot(int, int)
    def on_tW_bd_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.ligne_courante = row
        self.pB_supprimer_annuler.setEnabled(True)
    
    @pyqtSlot()
    def on_pB_ajouter_clicked(self):
        """
        Slot documentation goes here.
        """
        
        appareil = self.lE_appareil.text()
        adresse = self.lE_adresse.text()
        proprietaire = self.cbB_proprietaire.currentText()
        
        self.table = self.tW_bd
        self.table.setRowCount(self.ligne + 1)
        self.table.setItem(self.ligne, 0, QTableWidgetItem(appareil))
        self.table.setItem(self.ligne, 1, QTableWidgetItem(adresse))
        self.table.setItem(self.ligne, 2, QTableWidgetItem(proprietaire))
        
        id = int(str(self.requete.execute(self.r_recherche_prop, (proprietaire, )).fetchone())[1:-2])
        
        self.requete.execute(self.r_ajout_app, (appareil, adresse, id))
        
        self.ligne += 1
    
    @pyqtSlot()
    def on_pB_supprimer_clicked(self):
        """
        Slot documentation goes here.
        """
        self.table = self.tW_bd
        appareil = self.table.item(self.ligne_courante, 1).text()
        self.table.removeRow(self.ligne_courante)
        
        id = int(str(self.requete.execute(self.r_recherche_app, (appareil, )).fetchone())[1:-2])
        
        self.requete.execute(self.r_supp_app, (id, ))
        
        self.ligne -= 1
    
    def closeEvent(self, event):
        
        if fonctions.getMax(self) >= int(str(self.requete.execute(self.r_nb_prop).fetchone())[1:-2]):
            max = fonctions.getMax(self)
        else:
            max = int(str(self.requete.execute(self.r_nb_prop).fetchone())[1:-2])
        
        for i in range(1, max + 1):
            if str(self.requete.execute(self.r_dic_cbB_nom, (i, )).fetchone())[2:-3] != '' and i not in self.dic_cbB_nom:
                self.requete.execute(self.r_supp_prop, (i, ))
            elif str(self.requete.execute(self.r_dic_cbB_nom, (i, )).fetchone())[2:-3] == '' and i in self.dic_cbB_nom:
                self.requete.execute(self.ra_dic_tw_nom, (self.dic_cbB_nom.get(i), ))
            else:
                self.requete.execute(self.r_modif_prop, (self.dic_cbB_nom.get(i), i))
            
        
        self.connexion.commit()
        

#        dictionnaires.fermeture(self)

































