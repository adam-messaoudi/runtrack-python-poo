class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur  # Attribut privé longueur
        self._largeur = largeur    # Attribut privé largeur

    def calculerPerimetre(self):
        return 2 * (self._longueur + self._largeur)  # Méthode pour calculer le périmètre

    def calculerSurface(self):
        return self._longueur * self._largeur  # Méthode pour calculer la surface

    # Assesseurs et mutateurs pour longueur et largeur
    def getLongueur(self):
        return self._longueur

    def setLongueur(self, new_longueur):
        self._longueur = new_longueur

    def getLargeur(self):
        return self._largeur

    def setLargeur(self, new_largeur):
        self._largeur = new_largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # Appel au constructeur de la classe mère
        self._hauteur = hauteur  # Attribut hauteur supplémentaire

    def calculerVolume(self):
        return self._longueur * self._largeur * self._hauteur  # Méthode pour calculer le volume


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 10)

# Utilisation des méthodes de la classe Rectangle
print("Périmètre du rectangle:", rectangle.calculerPerimetre())
print("Surface du rectangle:", rectangle.calculerSurface())

# Utilisation des assesseurs et mutateurs pour la classe Rectangle
rectangle.setLongueur(7)
rectangle.setLargeur(12)
print("Nouvelle longueur:", rectangle.getLongueur())
print("Nouvelle largeur:", rectangle.getLargeur())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(3, 4, 5)

# Utilisation de la méthode de la classe Parallelepipede
print("Volume du parallélépipède:", parallelepipede.calculerVolume())
