# Définition de la classe Point avec des méthodes pour afficher, modifier et consulter les coordonnées
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # Initialisation de l'attribut x
        self.y = y  # Initialisation de l'attribut y
    
    def afficherLesPoints(self):
        print(f"Coordonnées : ({self.x}, {self.y})")  # Affichage des coordonnées
    
    def afficherX(self):
        print(f"Coordonnée X : {self.x}")  # Affichage de la coordonnée x
    
    def afficherY(self):
        print(f"Coordonnée Y : {self.y}")  # Affichage de la coordonnée y
    
    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur  # Méthode pour changer la valeur de x
    
    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur  # Méthode pour changer la valeur de y

# Utilisation de la classe Point et de ses méthodes pour manipuler les coordonnées
point_instance = Point(2, 3)
point_instance.afficherLesPoints()
point_instance.changerX(5)
point_instance.changerY(7)
point_instance.afficherX()
point_instance.afficherY()
