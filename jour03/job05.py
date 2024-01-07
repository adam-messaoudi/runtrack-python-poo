import random

class Personnage:
    def __init__(self, nom, vie):
        # Initialise un personnage avec un nom et des points de vie
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        # Attaque l'adversaire en infligeant des dégâts aléatoires entre 5 et 20
        degats = random.randint(5, 20)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        # Initialise le jeu avec un niveau de difficulté vide
        self.niveau = None

    def choisirNiveau(self):
        # Associe chaque niveau à un tuple représentant la vie du joueur et de l'ennemi
        niveaux = {
            1: (100, 80),
            2: (80, 100),
            3: (60, 120)
        }
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")
        self.niveau = int(input("Niveau : "))
        return niveaux.get(self.niveau, (100, 80))  # Renvoie les points de vie par défaut si le niveau est inconnu

    def lancerJeu(self):
        # Récupère les points de vie du joueur et de l'ennemi en fonction du niveau choisi
        joueur_vie, ennemi_vie = self.choisirNiveau()
        joueur = Personnage("Joueur", joueur_vie)
        ennemi = Personnage("Ennemi", ennemi_vie)

        # Déroulement du combat : attaques réciproques jusqu'à ce que l'un des deux n'ait plus de vie
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu !")
                break

        # Affiche le résultat de la partie
        if joueur.vie > 0:
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu !")

# Crée une instance de Jeu et lance la partie
jeu = Jeu()
jeu.lancerJeu()
