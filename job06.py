# Création de la classe Animal avec des attributs âge et prenom, ainsi que des méthodes pour vieillir et nommer
class Animal:
    def __init__(self):
        self.age = 0  # Initialisation de l'attribut âge
        self.prenom = ""  # Initialisation de l'attribut prenom
    
    def vieillir(self):
        self.age += 1  # Méthode pour augmenter l'âge de l'animal
    
    def nommer(self, nom):
        self.prenom = nom  # Méthode pour donner un nom à l'animal

# Utilisation de la classe Animal et de ses méthodes pour gérer l'âge et le nom de l'animal
animal_instance = Animal()
print("Âge initial de l'animal :", animal_instance.age)
animal_instance.vieillir()
print("Âge après vieillissement :", animal_instance.age)
animal_instance.nommer("Rex")
print("Nom de l'animal :", animal_instance.prenom)
