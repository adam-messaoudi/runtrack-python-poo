<<<<<<< HEAD
# Définition de la classe Point avec des méthodes pour afficher, modifier et consulter les coordonnées
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # Initialisation de l'attribut x
        self.y = y  # Initialisation de l'attribut y
    
    def afficherLesPoints(self):
        print(f"Coordonnées : ({self.x}, {self.y})")  # Affichage des coordonnées
    
    def afficherX(self):
        print(f"Coordonnée X : {self.x}")  # Affichage de la coordonnée x
    
    def afficherY(self):
        print(f"Coordonnée Y : {self.y}")  # Affichage de la coordonnée y
    
    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur  # Méthode pour changer la valeur de x
    
    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur  # Méthode pour changer la valeur de y

# Utilisation de la classe Point et de ses méthodes pour manipuler les coordonnées
point_instance = Point(2, 3)
point_instance.afficherLesPoints()
point_instance.changerX(5)
point_instance.changerY(7)
point_instance.afficherX()
point_instance.afficherY()
=======
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque  # Attribut privé pour la marque de la voiture
        self.__modele = modele  # Attribut privé pour le modèle de la voiture
        self.__annee = annee    # Attribut privé pour l'année de la voiture
        self.__kilometrage = kilometrage  # Attribut privé pour le kilométrage de la voiture
        self.__en_marche = False  # Attribut privé pour indiquer si la voiture est en marche (par défaut à False)
        self.__reservoir = 50     # Attribut privé pour le réservoir initialisé à 50
        
    # Assesseurs (getters) pour récupérer les valeurs des attributs
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    # Mutateurs (setters) pour modifier les valeurs des attributs
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque
    
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele
    
    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee
    
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage
    
    def set_en_marche(self, etat):
        self.__en_marche = etat
    
    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:  # Vérifie si le réservoir est supérieur à 5
            self.__en_marche = True      # Met la voiture en marche
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide, la voiture ne peut pas démarrer.")
    
    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")
    
    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir
    
    # Assesseur pour le réservoir (pas de mutateur, car on n'a pas besoin de le modifier directement depuis l'extérieur)
    def get_reservoir(self):
        return self.__reservoir

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Peugeot", "208", 2019, 30000)

# Démarrer la voiture
ma_voiture.demarrer()

# Afficher le kilométrage de la voiture
print("Kilométrage actuel de la voiture :", ma_voiture.get_kilometrage())

# Arrêter la voiture
ma_voiture.arreter()
>>>>>>> f031f0c4267ae09390c3502473bf1039b5525d01
