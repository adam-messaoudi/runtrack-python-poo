# Définition de la classe Carte représentant chaque carte individuelle
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # La valeur de la carte (nombre ou figure)
        self.couleur = couleur  # La couleur de la carte

import random

# Définition de la classe Jeu pour gérer le paquet de cartes
class Jeu:
    def __init__(self):
        self.paquet = []  # Initialisation d'une liste vide pour le paquet de cartes
        self.creer_paquet()  # Création du paquet de 52 cartes

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']  # Liste des couleurs
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']  # Liste des valeurs

        # Création du paquet de 52 cartes en combinant chaque couleur avec chaque valeur
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))  # Ajout de chaque carte au paquet

    def melanger(self):
        random.shuffle(self.paquet)  # Mélange aléatoire du paquet de cartes

    def donner_carte(self):
        # Distribue une carte du paquet et la retire de la liste
        if len(self.paquet) > 0:
            return self.paquet.pop()
        else:
            print("Plus de cartes dans le paquet.")  # Message si le paquet est vide

# Définition de la classe Blackjack pour gérer le jeu lui-même
class Blackjack:
    def __init__(self):
        # Initialisation d'un jeu, mélange des cartes et création des mains du joueur et du croupier
        self.jeu = Jeu()
        self.jeu.melanger()
        self.main_joueur = []  # Main du joueur
        self.main_croupier = []  # Main du croupier

    def debut_partie(self):
        # Distribue deux cartes à chaque joueur au début de la partie
        for _ in range(2):
            self.main_joueur.append(self.jeu.donner_carte())  # Ajout d'une carte à la main du joueur
            self.main_croupier.append(self.jeu.donner_carte())  # Ajout d'une carte à la main du croupier

    def tour_joueur(self):
        # Gestion du tour du joueur : il peut prendre des cartes supplémentaires ou passer
        while True:
            self.afficher_main_joueur()  # Affichage de la main du joueur
            choix = input("Voulez-vous prendre une carte ? (o/n) : ")
            if choix.lower() == 'o':
                self.main_joueur.append(self.jeu.donner_carte())  # Le joueur prend une carte
                if self.calculer_points(self.main_joueur) > 21:
                    # Vérifie si le joueur a dépassé 21 points (buste)
                    self.afficher_main_joueur()
                    print("Vous avez dépassé 21, vous avez perdu !")
                    return False
            else:
                return True  # Le joueur choisit de passer

    def tour_croupier(self):
        # Gestion du tour du croupier : il prend des cartes jusqu'à atteindre au moins 17 points
        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.donner_carte())  # Le croupier prend une carte

    def calculer_points(self, main):
        # Calcule le total de points pour une main de cartes
        points = 0
        as_present = False
        for carte in main:
            if carte.valeur.isdigit():
                points += int(carte.valeur)
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                points += 10
            else:  # 'As'
                as_present = True
                points += 11  # Ajoute 11 pour l'As (si possible)
        if as_present and points > 21:
            points -= 10  # Change l'As en 1 s'il fait dépasser 21 points
        return points

    def afficher_main_joueur(self):
        # Affiche la main actuelle du joueur et le total de points
        print("Votre main : ")
        for carte in self.main_joueur:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total des points : {self.calculer_points(self.main_joueur)}")

    def demarrer_partie(self):
        # Démarrage du jeu : distribution des cartes, tours du joueur et du croupier, affichage du résultat
        self.debut_partie()
        if self.tour_joueur():
            self.tour_croupier()
            self.afficher_main_croupier()
            self.declarer_resultat()

    def afficher_main_croupier(self):
        # Affiche la main du croupier et le total de points
        print("Main du croupier : ")
        for carte in self.main_croupier:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total des points : {self.calculer_points(self.main_croupier)}")

    def declarer_resultat(self):
        # Déclare le résultat du jeu : gagnant, perdant ou égalité
        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        if points_joueur > 21:
            print("Vous avez dépassé 21, vous avez perdu !")
        elif points_croupier > 21:
            print("Le croupier a dépassé 21, vous avez gagné !")
        elif points_joueur > points_croupier:
            print("Vous avez plus de points que le croupier, vous avez gagné !")
        elif points_croupier > points_joueur:
            print("Le croupier a plus de points, vous avez perdu !")
        else:
            print("Égalité !")

# Démarrage du jeu
jeu_blackjack = Blackjack()
jeu_blackjack.demarrer_partie()
