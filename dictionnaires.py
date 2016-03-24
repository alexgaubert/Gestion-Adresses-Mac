def init(self):
    self.dic_cbB_nom = {}
    self.dic_tw_app = {}
    self.dic_tw_adr = {}
    self.dic_tw_nom = {}
    
    self.nb_nom_bd = int(str(self.requete.execute(self.r_nb_prop).fetchone())[1:-2])
    self.nb_app = int(str(self.requete.execute(self.r_nb_adr).fetchone())[1:-2])
    
    
    
    for i in range(1, self.nb_nom_bd + 1):
        if str(self.requete.execute(self.r_dic_cbB_nom, (i, )).fetchone())[2:-3] != '':
            self.dic_cbB_nom[i] = str(self.requete.execute(self.r_dic_cbB_nom, (i, )).fetchone())[2:-3]
    print(self.dic_cbB_nom)
    
    for i in range(1, self.nb_app + 1):
        self.dic_tw_app[i] = str(self.requete.execute(self.r_dic_tw_app, (i, )).fetchone())[2:-3]
        self.dic_tw_adr[i] = str(self.requete.execute(self.r_dic_tw_adr, (i, )).fetchone())[2:-3]
        self.dic_tw_nom[i] = str(self.requete.execute(self.r_dic_tw_nom, (i, )).fetchone())[2:-3]

def fermeture(self):
    for i in range(self.nb_nom_bd +1, self.nb_nom_bd + self.nb_nom_ajout + 1):
        self.requete.execute("insert into proprietaire(nom) values(?)", (self.dic_cbB_nom[i], ))
    
    self.connexion.commit()
