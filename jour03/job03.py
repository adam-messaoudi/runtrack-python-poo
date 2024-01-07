class Tache:
    def __init__(self, titre, description, statut="À faire"):
        # Initialise les attributs d'une tâche
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        # Initialise une liste vide pour les tâches
        self.taches = []

    def ajouterTache(self, tache):
        # Ajoute une nouvelle tâche à la liste
        self.taches.append(tache)

    def supprimerTache(self, titre_tache):
        # Supprime une tâche par son titre
        for tache in self.taches:
            if tache.titre == titre_tache:
                self.taches.remove(tache)
                break

    def marquerCommeFinie(self, titre_tache):
        # Marque une tâche comme terminée
        for tache in self.taches:
            if tache.titre == titre_tache:
                tache.statut = "Terminée"
                break

    def afficherListe(self):
        # Affiche la liste de toutes les tâches
        for tache in self.taches:
            print(f"Titre : {tache.titre}, Description : {tache.description}, Statut : {tache.statut}")

    def filterListe(self, statut):
        # Retourne une liste filtrée par statut
        return [tache for tache in self.taches if tache.statut == statut]

# Création d'une liste de tâches
liste_taches = ListeDeTaches()

# Création de quelques tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser Python", "Préparer pour l'examen")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste de tâches
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Faire les courses")

# Afficher les tâches restantes à faire
taches_restantes = liste_taches.filterListe("À faire")
print("Tâches restantes à faire : 5")
for tache in taches_restantes:
    print(f"{tache.titre} : {tache.description}")
