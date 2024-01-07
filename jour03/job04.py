class Joueur:
    def __init__(self, nom, numero, position):
        # Initialise les attributs du joueur
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        # Méthode pour enregistrer un but marqué par le joueur
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        # Méthode pour enregistrer une passe décisive effectuée par le joueur
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        # Méthode pour enregistrer un carton jaune reçu par le joueur
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        # Méthode pour enregistrer un carton rouge reçu par le joueur
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        # Méthode pour afficher les statistiques du joueur
        print(f"Statistiques de {self.nom} (Numéro {self.numero}) - Position : {self.position}")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes reçus : {self.cartons_jaunes}")
        print(f"Cartons rouges reçus : {self.cartons_rouges}")
        print("-----------------------")


class Equipe:
    def __init__(self, nom):
        # Initialise le nom de l'équipe et une liste vide de joueurs
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        # Méthode pour ajouter un joueur à l'équipe
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        # Méthode pour afficher les statistiques de tous les joueurs de l'équipe
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()
        print("-----------------------")

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        # Méthode pour mettre à jour les statistiques d'un joueur en fonction de l'action
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                break


# Création des joueurs
joueur1 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur2 = Joueur("Lionel Messi", 10, "Milieu Offensif")
joueur3 = Joueur("Neymar Jr.", 11, "Ailier")

# Création des équipes
equipe1 = Equipe("Real Madrid")
equipe2 = Equipe("Paris Saint-Germain")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques initiales des joueurs
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation du match en mettant à jour les statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", "but")
equipe2.mettreAJourStatistiquesJoueur("Lionel Messi", "passe")
equipe2.mettreAJourStatistiquesJoueur("Neymar Jr.", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Neymar Jr.", "rouge")

# Affichage des statistiques mises à jour après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
