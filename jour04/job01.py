class Personne:
    def __init__(self, age=14):
        self.age = age  # Initialise l'attribut âge avec la valeur par défaut de 14 ans

    def afficherAge(self):
        print(f"L'âge de la personne est de {self.age} ans.")  # Affiche l'âge de la personne

    def bonjour(self):
        print("Hello")  # Affiche "Hello" lorsque la méthode est appelée

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age  # Permet de modifier l'âge de la personne


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")  # Affiche "Je vais en cours" lorsque la méthode est appelée

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")  # Affiche l'âge de l'élève


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee  # Initialise l'attribut matière enseignée

    def enseigner(self):
        print("Le cours va commencer")  # Affiche "Le cours va commencer" lorsque la méthode est appelée


# Instanciation d'une Personne et d'un Eleve
personne = Personne()  # Crée une instance de la classe Personne avec l'âge par défaut
eleve = Eleve()  # Crée une instance de la classe Eleve avec l'âge par défaut

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()
