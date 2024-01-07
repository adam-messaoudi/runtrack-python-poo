class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée X: {self.x}")

    def afficherY(self):
        print(f"Coordonnée Y: {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Exemple d'utilisation de la classe Point
point = Point(3, 7)
point.afficherLesPoints()
point.afficherX()
point.afficherY()

point.changerX(5)
point.changerY(9)

point.afficherLesPoints()
