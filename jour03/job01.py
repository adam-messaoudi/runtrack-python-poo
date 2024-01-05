# Définition de la classe Ville avec un nom et un nombre d'habitants
class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom  # Attribut privé : nom de la ville
        self.nombre_habitants = nombre_habitants  # Attribut privé : nombre d'habitants

# Définition de la classe Personne avec nom, âge et une référence à une instance de Ville
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom  # Attribut privé : nom de la personne
        self.age = age  # Attribut privé : âge de la personne
        self.ville = ville  # Attribut privé : référence à une instance de Ville

    # Méthode pour augmenter le nombre d'habitants de la ville de la personne de 1
    def ajouterPopulation(self):
        self.ville.nombre_habitants += 1

# Création de l'objet Ville Paris avec 1 000 000 habitants
ville_paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à Paris : {ville_paris.nombre_habitants} habitants")  # Affichage du nombre d'habitants à Paris

# Création de l'objet Ville Marseille avec 861 635 habitants
ville_marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants à Marseille : {ville_marseille.nombre_habitants} habitants")  # Affichage du nombre d'habitants à Marseille

# Création des personnes et ajout à leur ville respective
john = Personne("John", 45, ville_paris)
john.ajouterPopulation()  # Appel de la méthode pour ajouter John à la population de Paris

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouterPopulation()  # Appel de la méthode pour ajouter Myrtille à la population de Paris

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouterPopulation()  # Appel de la méthode pour ajouter Chloé à la population de Marseille

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Mise à jour de la population à Paris : {ville_paris.nombre_habitants} habitants")
print(f"Mise à jour de la population à Marseille : {ville_marseille.nombre_habitants} habitants")
