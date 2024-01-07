class Rectangle:
    def __init__(self, longueur, largeur):
        # Initialisation des attributs privés longueur et largeur
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs pour la longueur et la largeur
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs pour la longueur et la largeur
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    # Méthode pour calculer le périmètre du rectangle
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface du rectangle
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        # Appel du constructeur de la classe parent Rectangle
        super().__init__(longueur, largeur)
        # Initialisation de l'attribut privé hauteur
        self.__hauteur = hauteur

    # Assesseur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour la hauteur
    def set_hauteur(self, nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur

    # Méthode pour calculer le volume du parallélépipède
    def volume(self):
        return self.__hauteur * self.surface()


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 10)
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(3, 4, 6)
print("Volume du parallélépipède:", parallelepipede.volume())
