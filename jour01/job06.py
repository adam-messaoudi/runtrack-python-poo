class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"Âge de l'animal : {self.age} ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"Nom de l'animal : {self.prenom}")

# Instanciation de la classe Animal
animal = Animal()

# Affichage de l'âge initial de l'animal
animal.afficherAge()

# Faire vieillir l'animal et afficher son âge mis à jour
animal.vieillir()
animal.afficherAge()

# Nommer l'animal et afficher son nom
animal.nommer("Rex")
