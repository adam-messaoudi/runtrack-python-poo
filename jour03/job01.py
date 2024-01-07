class Ville:
    def __init__(self, nom, nb_habitants):
        # Initialise les attributs de la ville
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self.__nb_habitants  # Méthode pour obtenir le nombre d'habitants


class Personne:
    def __init__(self, nom, age, ville):
        # Initialise les attributs de la personne
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        # Méthode pour augmenter de 1 le nombre d'habitants de la ville de la personne
        nb_habitants = self.__ville.get_nb_habitants()
        nb_habitants += 1
        self.__ville._Ville__nb_habitants = nb_habitants  # Modifie le nombre d'habitants (mauvaise pratique en général)

# Création de l'objet Ville "Paris" avec 1 000 000 d'habitants
paris = Ville("Paris", 1000000)

# Affichage du nombre d'habitants de la ville de Paris
print(f"Nombre d'habitants à Paris : {paris.get_nb_habitants()} habitants")

# Création de l'objet Ville "Marseille" avec 861 635 d'habitants
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants de la ville de Marseille
print(f"Nombre d'habitants à Marseille : {marseille.get_nb_habitants()} habitants")

# Création des objets Personne avec leur ville respective
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de personnes et affichage du nombre d'habitants après l'arrivée de ces personnes
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants à Paris et à Marseille après l'arrivée de ces personnes
print(f"Mise à jour du Nombre d'habitants à Paris : {paris.get_nb_habitants()} habitants")
print(f"Mise à jour du Nombre d'habitants à Marseille : {marseille.get_nb_habitants()} habitants")
