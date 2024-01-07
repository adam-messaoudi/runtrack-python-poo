class Personne:
    def __init__(self, age=14):  # Initialise avec l'âge par défaut à 14
        self.age = age  # Attribut age

    def afficherAge(self):  # Méthode pour afficher l'âge
        print(f"J'ai {self.age} ans")

    def bonjour(self):  # Méthode pour dire bonjour
        print("Hello")

    def modifierAge(self, new_age):  # Méthode pour modifier l'âge
        self.age = new_age


class Eleve(Personne):  # Classe Eleve héritant de Personne
    def allerEnCours(self):  # Méthode pour indiquer aller en cours
        print("Je vais en cours")

    def afficherAge(self):  # Méthode pour afficher l'âge de l'élève
        print(f"J'ai {self.age} ans")


class Professeur(Personne):  # Classe Professeur héritant de Personne
    def __init__(self, matiereEnseignee):  # Initialisation avec la matière enseignée
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):  # Méthode pour indiquer que le cours va commencer
        print("Le cours va commencer")


# Instanciation d'une Personne et d'un Eleve
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()
