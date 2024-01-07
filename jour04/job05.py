class Forme:
    def aire(self):
        return 0  # Méthode aire renvoyant 0 par défaut pour toute forme


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur  # Surcharge de la méthode aire pour le rectangle


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14159 * self.radius ** 2  # Surcharge de la méthode aire pour le cercle


# Instanciation d'un rectangle et d'un cercle
rectangle = Rectangle(5, 10)
cercle = Cercle(4)

# Calcul et affichage de l'aire du rectangle et du cercle
print("Aire du rectangle:", rectangle.aire())
print("Aire du cercle:", cercle.aire())
