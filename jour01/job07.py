# Création de la classe Personnage pour représenter un personnage de jeu avec des méthodes pour se déplacer et obtenir la position
class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x  # Initialisation de l'attribut x représentant la position en abscisse
        self.y = y  # Initialisation de l'attribut y représentant la position en ordonnée
    
    def gauche(self):
        self.x -= 1  # Méthode pour déplacer le personnage vers la gauche
    
    def droite(self):
        self.x += 1  # Méthode pour déplacer le personnage vers la droite
    
    def bas(self):
        self.y -= 3  # Méthode pour déplacer le personnage vers le bas
    
    def haut(self):
        self.y += 5 # Méthode pour déplacer le personnage vers le haut
    
    def position(self):
        return (self.x, self.y)  # Méthode pour obtenir la position actuelle du personnage

# Utilisation de la classe Personnage pour déplacer le personnage et obtenir sa position
personnage_instance = Personnage()
personnage_instance.droite()
personnage_instance.haut()
print("Position du personnage :", personnage_instance.position())
