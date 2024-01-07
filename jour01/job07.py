class Personnage:

    # Initialise la classe avec les coordonnées x et y du personnage
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # déplace le personnage d'une unité vers la gauche
    def gauche(self):
        self.x -= 1

    # déplace le personnage d'une unité vers la droite 
    def droite(self):
        self.x += 6

    # déplace le personnage d'une unité vers le haut
    def haut(self):
        self.y -= 1
    # déplace le personnage d'une unité vers le bas
    def bas(self):
        self.y += 2

    # renvoie les coordonnées actuelles du personnage
    def position(self):
        return (self.x, self.y)
    
# Crée une instance de la classe Personnage avec les coordonnées initiales (0, 0)
personnage = Personnage(0, 0)

personnage.droite() # On va a droite pour modifier la valeur de x
print(personnage.position())

personnage.haut() # On fait pareil pour modifier la valeur de y
print(personnage.position())

personnage.gauche() # Puis on retourne a 0 horizontalement en allant a gauche
print(personnage.position())

personnage.bas() # Et on retourne a 0 verticalement en allant en bas
print(personnage.position())