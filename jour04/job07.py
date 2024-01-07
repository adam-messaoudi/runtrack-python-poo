import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['As', 'Deux', 'Trois', 'Quatre', 'Cinq', 'Six', 'Sept', 'Huit', 'Neuf', 'Dix', 'Valet', 'Dame', 'Roi']

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def distribuer_cartes(self, nombre_cartes):
        return random.sample(self.paquet, nombre_cartes)

    def calculer_points(self, main):
        points = 0
        as_present = False

        for carte in main:
            if carte.valeur == 'As':
                as_present = True
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                points += 10
            else:
                points += 1  # Compte de l'As comme 1, pour le moment, car la valeur de l'As n'est pas décidée

        if as_present:
            if points + 10 <= 21:
                points += 10

        return points

# Déroulement d'une partie de Blackjack
jeu_blackjack = Jeu()

# Distribution des cartes pour le joueur et le croupier
main_joueur = jeu_blackjack.distribuer_cartes(2)
main_croupier = jeu_blackjack.distribuer_cartes(2)

# Affichage des cartes du joueur et du croupier
print("Cartes du joueur:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

print("\nCartes du croupier:")
for carte in main_croupier:
    print(f"{carte.valeur} de {carte.couleur}")

# Calcul des points du joueur et du croupier
points_joueur = jeu_blackjack.calculer_points(main_joueur)
points_croupier = jeu_blackjack.calculer_points(main_croupier)

# Affichage des points du joueur et du croupier
print(f"\nTotal des points du joueur: {points_joueur}")
print(f"Total des points du croupier: {points_croupier}")
