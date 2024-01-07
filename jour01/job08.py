import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon  # Initialisation de l'attribut rayon lors de la création d'un cercle

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon  # Méthode pour changer le rayon du cercle

    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")  # Affiche le rayon du cercle

    def circonférence(self):
        return 2 * math.pi * self.rayon  # Calcule et retourne la circonférence du cercle

    def aire(self):
        return math.pi * (self.rayon ** 2)  # Calcule et retourne l'aire du cercle

    def diametre(self):
        return 2 * self.rayon  # Calcule et retourne le diamètre du cercle

# Création des cercles avec des rayons différents
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
cercle1.afficherInfos()
print(f"Circonférence : {cercle1.circonférence()}")
print(f"Diamètre : {cercle1.diametre()}")
print(f"Aire : {cercle1.aire()}")

cercle2.afficherInfos()
print(f"Circonférence : {cercle2.circonférence()}")
print(f"Diamètre : {cercle2.diametre()}")
print(f"Aire : {cercle2.aire()}")
