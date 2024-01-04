class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé longueur
        self.__largeur = largeur  # Attribut privé largeur
    
    # Assesseurs (getters) pour obtenir les valeurs des attributs
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    # Mutateurs (setters) pour modifier les valeurs des attributs
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur
    
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Création d'un rectangle et modification de ses valeurs avec les mutateurs
mon_rectangle = Rectangle(10, 5)
mon_rectangle.setLongueur(17)
mon_rectangle.setLargeur(8)

# Vérification des modifications en imprimant les valeurs du rectangle
print("Longueur :", mon_rectangle.getLongueur())
print("Largeur :", mon_rectangle.getLargeur())
