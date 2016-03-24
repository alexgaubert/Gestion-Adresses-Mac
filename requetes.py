def init(self):
    self.r_nb_adr = 'select max(id) from appareil;'
    self.r_nb_prop = 'select max(id) from proprietaire;'
    
    self.r_dic_cbB_nom = 'select nom from proprietaire where id=?;'
    
    self.r_dic_tw_app = 'select nom from appareil where id=?;'
    self.r_dic_tw_adr = 'select adresse from appareil where id=?;'
    self.r_dic_tw_nom = 'select p.nom from proprietaire as p inner join appareil as a on a.idProprietaire = p.id where a.id=?;'
    
    self.ra_dic_tw_nom = 'insert into proprietaire(nom) values(?);'
    self.r_supp_prop = 'delete from proprietaire where id=?;'
    self.r_modif_prop = 'update proprietaire set nom=? where id=?;'

    self.r_ajout_app = 'insert into appareil(nom,adresse,idProprietaire) values(?,?,?);'
    
    self.r_recherche_prop = 'select id from proprietaire where nom=?;'
    
    self.r_supp_app = 'delete from appareil where id=?'
    
    self.r_recherche_app = 'select id from appareil where adresse=?'
