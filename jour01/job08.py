import math

# Création de la classe Cercle avec des méthodes pour manipuler et obtenir des informations sur le cercle
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon  # Initialisation de l'attribut rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon  # Méthode pour changer le rayon du cercle
    
    def afficherInfos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")  # Affichage des informations sur le cercle
    
    def circonference(self):
        return 2 * math.pi * self.rayon  # Méthode pour calculer la circonférence
    
    def aire(self):
        return math.pi * self.rayon ** 2  # Méthode pour calculer l'aire du cercle
    
    def diametre(self):
        return 2 * self.rayon  # Méthode pour calculer le diamètre

# Utilisation de la classe Cercle pour créer des cercles et obtenir des informations à leur sujet
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print("Circonférence du cercle 1 :", cercle1.circonference())
print("Diamètre du cercle 1 :", cercle1.diametre())
print("Aire du cercle 1 :", cercle1.aire())

cercle2.afficherInfos()
print("Circonférence du cercle 2 :", cercle2.circonference())
print("Diamètre du cercle 2 :", cercle2.diametre())
print("Aire du cercle 2 :", cercle2.aire())
