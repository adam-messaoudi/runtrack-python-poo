class Tache:
    # Définition de la classe Tache pour représenter une tâche
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre  # Titre de la tâche
        self.description = description  # Description de la tâche
        self.statut = statut  # Statut de la tâche (par défaut, "à faire")

class ListeDeTaches:
    # Définition de la classe ListeDeTaches pour gérer une liste de tâches
    def __init__(self):
        self.taches = []  # Liste vide pour stocker les tâches

    def ajouterTache(self, tache):
        self.taches.append(tache)  # Ajoute une tâche à la liste

    def supprimerTache(self, titre):
        # Supprime une tâche de la liste en fonction de son titre
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                break

    def marquerCommeFinie(self, titre):
        # Change le statut d'une tâche à "terminée" en fonction de son titre
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                break

    def afficherListe(self):
        # Affiche toutes les tâches de la liste avec leur titre, description et statut
        for tache in self.taches:
            print(f"Titre : {tache.titre} | Description : {tache.description} | Statut : {tache.statut}")

    def filterListe(self, statut):
        # Retourne une liste des tâches ayant un certain statut ("à faire" ou "terminée")
        filtered_tasks = [tache for tache in self.taches if tache.statut == statut]
        return filtered_tasks

# Création de quelques tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser pour l'examen", "Revoir les chapitres 3 à 5")
tache3 = Tache("Appeler le plombier", "Fixer un rendez-vous pour la réparation")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de toutes les tâches
print("Liste de toutes les tâches :")
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Faire les courses")

# Afficher les tâches à faire
print("\nTâches restantes à faire :")
taches_a_faire = liste_taches.filterListe("à faire")
for tache in taches_a_faire:
    print(f"Titre : {tache.titre} | Description : {tache.description} | Statut : {tache.statut}")
