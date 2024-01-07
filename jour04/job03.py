class Forme:
    def aire(self):
        # Méthode par défaut renvoyant une aire nulle
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        # Initialisation des attributs longueur et largeur
        self.__longueur = longueur
        self.__largeur = largeur

    # Getters et setters pour longueur et largeur
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthodes pour calculer le périmètre et la surface du rectangle
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Getter et setter pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume du parallélépipède
    def volume(self):
        return self.surface() * self.__hauteur

# Instanciation d'un rectangle et d'un parallélépipède pour les tests
rectangle1 = Rectangle(2, 44)
print("Perimètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())

rectangle1.set_longueur(5)
rectangle1.set_largeur(68)
print("Perimètre du rectangle après la modif :", rectangle1.perimetre())
print("Surface du rectangle après la modif :", rectangle1.surface())

parallelepipede1 = Parallelepipede(1, 2, 3)
print("Volume du parallelepipede :", parallelepipede1.volume())
