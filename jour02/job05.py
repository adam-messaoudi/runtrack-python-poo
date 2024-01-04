class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False  # Attribut privé en_marche initialisé à False
    
    # Assesseurs pour obtenir les valeurs des attributs
    def getMarque(self):
        return self.__marque
    
    def getModele(self):
        return self.__modele
    
    def getAnnee(self):
        return self.__annee
    
    def getKilometrage(self):
        return self.__kilometrage
    
    def getEnMarche(self):
        return self.__en_marche
    
    # Mutateurs pour modifier les valeurs des attributs
    def setMarque(self, nouvelle_marque):
        self.__marque = nouvelle_marque
    
    def setModele(self, nouveau_modele):
        self.__modele = nouveau_modele
    
    def setAnnee(self, nouvelle_annee):
        self.__annee = nouvelle_annee
    
    def setKilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Le réservoir est trop bas pour démarrer la voiture.")
    
    def arreter(self):
        self.__en_marche = False
    
    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir
    
    # Autres méthodes ici

# Utilisation de la classe Voiture et de ses méthodes pour gérer le démarrage et l'arrêt
ma_voiture = Voiture("Toyota", "Corolla", 2020, 20000)
ma_voiture.demarrer()
print("En marche :", ma_voiture.getEnMarche())
ma_voiture.arreter()
print("En marche après arrêt :", ma_voiture.getEnMarche())
