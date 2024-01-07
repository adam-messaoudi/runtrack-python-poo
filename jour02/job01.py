class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé pour la longueur
        self.__largeur = largeur  # Attribut privé pour la largeur

    # Assesseur pour la longueur
    def getLongueur(self):
        return self.__longueur

    # Mutateur pour la longueur
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # Assesseur pour la largeur
    def getLargeur(self):
        return self.__largeur

    # Mutateur pour la largeur
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Création d'un rectangle avec longueur 10 et largeur 5
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print(f"Longueur: {mon_rectangle.getLongueur()}, Largeur: {mon_rectangle.getLargeur()}")

# Modification de la longueur et de la largeur
mon_rectangle.setLongueur(15)
mon_rectangle.setLargeur(8)

# Vérification des modifications
print(f"Nouvelle longueur: {mon_rectangle.getLongueur()}, Nouvelle largeur: {mon_rectangle.getLargeur()}")
