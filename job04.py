class Joueur:
    # Classe représentant un joueur
    def __init__(self, nom, numero, position):
        self.nom = nom  # Nom du joueur
        self.numero = numero  # Numéro du joueur
        self.position = position  # Position du joueur sur le terrain
        self.buts_marques = 0  # Initialisation du nombre de buts marqués
        self.passes_decisives = 0  # Initialisation du nombre de passes décisives
        self.cartons_jaunes = 0  # Initialisation du nombre de cartons jaunes reçus
        self.cartons_rouges = 0  # Initialisation du nombre de cartons rouges reçus

    # Méthode pour incrémenter le nombre de buts marqués
    def marquerUnBut(self):
        self.buts_marques += 1

    # Méthode pour incrémenter le nombre de passes décisives
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    # Méthode pour incrémenter le nombre de cartons jaunes reçus
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    # Méthode pour incrémenter le nombre de cartons rouges reçus
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    # Méthode pour afficher les statistiques du joueur
    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} - Buts marqués: {self.buts_marques} | Passes décisives: {self.passes_decisives} | Cartons jaunes: {self.cartons_jaunes} | Cartons rouges: {self.cartons_rouges}")


class Equipe:
    # Classe représentant une équipe
    def __init__(self, nom):
        self.nom = nom  # Nom de l'équipe
        self.liste_joueurs = []  # Liste vide pour stocker les joueurs de l'équipe

    # Méthode pour ajouter un joueur à l'équipe
    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    # Méthode pour afficher les statistiques de tous les joueurs de l'équipe
    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    # Méthode pour mettre à jour les statistiques d'un joueur en fonction de l'action (but, passe, carton...)
    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 11, "Attaquant")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Juventus")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)

# Affichage des statistiques avant le match
print("Statistiques avant le match :")
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

# Simulation du match
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Neymar", "passe")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "carton_rouge")

# Affichage des statistiques après le match
print("\nStatistiques après le match :")
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
