class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        # Initialisation des attributs privés de la voiture
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    # Méthode pour obtenir la marque de la voiture
    def get_marque(self):
        return self.__marque

    # Méthode pour définir une nouvelle marque pour la voiture
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    # Méthode pour obtenir le modèle de la voiture
    def get_modele(self):
        return self.__modele

    # Méthode pour définir un nouveau modèle pour la voiture
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    # Méthode pour obtenir l'année de la voiture
    def get_annee(self):
        return self.__annee

    # Méthode pour définir une nouvelle année pour la voiture
    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    # Méthode pour obtenir le kilométrage de la voiture
    def get_kilometrage(self):
        return self.__kilometrage

    # Méthode pour définir un nouveau kilométrage pour la voiture
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    # Méthode pour obtenir l'état de marche de la voiture (en marche ou arrêtée)
    def get_en_marche(self):
        return "En marche" if self.__en_marche else "Arrêtée"

    # Méthode pour démarrer la voiture
    def demarrer(self):
        self.__en_marche = self.__verifier_plein()
        if self.__en_marche:
            print("La voiture démarre.")
        else:
            print("La voiture ne démarre pas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    # Méthode pour obtenir le niveau de réservoir de la voiture
    def get_reservoir(self):
        return self.__reservoir
    
    # Méthode pour définir un nouveau niveau de réservoir pour la voiture
    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée pour vérifier si le réservoir est suffisamment plein pour démarrer la voiture
    def __verifier_plein(self):
        return self.__reservoir > 5

# Création d'une nouvelle instance de la classe Voiture avec des valeurs spécifiques
ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, kilometrage=32000, reservoir=30)

# Affichage des informations initiales de la voiture
print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")

# Modifier quelques attributs de la voiture
ma_voiture.set_marque("Honda")
ma_voiture.set_modele("Civic")
ma_voiture.set_annee(2020)
ma_voiture.set_kilometrage(45000)
ma_voiture.set_reservoir(10)

# Affichage des informations de la voiture après modification
print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")

# Démarrage de la voiture
ma_voiture.demarrer()
