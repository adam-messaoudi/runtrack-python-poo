class Forme:
    def aire(self):
        # Méthode de la classe Forme renvoyant 0
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        # Initialisation des attributs largeur et hauteur
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        # Surchargement de la méthode aire pour calculer l'aire du rectangle
        return self.largeur * self.hauteur

# Instanciation de la classe Rectangle avec une largeur de 5 et une hauteur de 10
rectangle = Rectangle(5, 10)

# Affichage du résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle:", rectangle.aire())
