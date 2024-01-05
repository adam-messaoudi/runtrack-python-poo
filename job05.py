import random  # Importation du module random pour générer des nombres aléatoires

class Personnage:
    # Définition de la classe Personnage
    def __init__(self, nom, vie):
        # Initialisation d'un personnage avec un nom et une quantité de vie
        self.nom = nom  # Nom du personnage
        self.vie = vie  # Quantité de vie du personnage

    def attaquer(self, adversaire):
        # Méthode pour faire attaquer un personnage adverse
        degats = random.randint(5, 20)  # Génération de dégâts aléatoires entre 5 et 20
        adversaire.vie -= degats  # Réduction de la vie de l'adversaire selon les dégâts
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    # Définition de la classe Jeu
    def __init__(self):
        # Initialisation du jeu avec un niveau par défaut
        self.niveau = 1

    def choisirNiveau(self):
        # Méthode pour permettre au joueur de choisir le niveau de difficulté
        self.niveau = int(input("Choisissez un niveau de difficulté (1 facile, 2 moyen, 3 difficile): "))

    def lancerJeu(self):
        # Méthode pour lancer le jeu avec le niveau choisi
        niveaux_vie = {1: 100, 2: 150, 3: 200}  # Dictionnaire contenant les vies pour chaque niveau

        vie_joueur = niveaux_vie[self.niveau]  # Récupération de la vie du joueur pour le niveau choisi
        vie_ennemi = niveaux_vie[self.niveau]  # Récupération de la vie de l'ennemi pour le niveau choisi

        joueur = Personnage("Joueur", vie_joueur)  # Création d'un personnage pour le joueur
        ennemi = Personnage("Ennemi", vie_ennemi)  # Création d'un personnage pour l'ennemi

        while joueur.vie > 0 and ennemi.vie > 0:
            # Boucle de combat : tant que les deux personnages sont vivants
            joueur.attaquer(ennemi)  # Le joueur attaque l'ennemi
            if ennemi.vie > 0:
                ennemi.attaquer(joueur)  # Si l'ennemi est encore vivant, il attaque le joueur

        if joueur.vie <= 0:
            print("Vous avez perdu!")  # Affichage du message si le joueur perd
        else:
            print("Félicitations! Vous avez vaincu l'ennemi!")  # Affichage du message si le joueur gagne

# Début du jeu
jeu = Jeu()  # Création d'une instance de la classe Jeu
jeu.choisirNiveau()  # Le joueur choisit le niveau de difficulté
jeu.lancerJeu()  # Le jeu est lancé avec le niveau choisi
