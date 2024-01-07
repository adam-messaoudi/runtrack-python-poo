class Forme:
    def aire(self):
        return 0  # Méthode aire renvoyant 0 par défaut pour toute forme


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur  # Surcharge de la méthode aire pour le rectangle


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 10)

# Calcul et affichage de l'aire du rectangle à l'aide de la méthode aire surchargée
print("Aire du rectangle:", rectangle.aire())
