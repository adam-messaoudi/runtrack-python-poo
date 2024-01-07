class Forme:
    def aire(self):
        # Méthode par défaut renvoyant une aire nulle
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        # Initialisation des attributs largeur et hauteur
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        # Surchargement de la méthode aire pour le rectangle
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        # Initialisation de l'attribut rayon (radius)
        self.radius = radius

    def aire(self):
        # Surchargement de la méthode aire pour le cercle
        return 3.14 * self.radius ** 2  # Utilisation de la formule π*r^2 pour calculer l'aire

# Création d'une instance de Rectangle et de Cercle pour les tests
rectangle = Rectangle(5, 10)
cercle = Cercle(7)

# Affichage des aires calculées pour chaque forme
print("Aire du rectangle :", rectangle.aire())
print("Aire du cercle :", cercle.aire())
