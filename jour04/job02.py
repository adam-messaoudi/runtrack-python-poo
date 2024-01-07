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
    def __init__(self, matiereEnseignee, age=40):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee  # Initialise l'attribut matière enseignée

    def enseigner(self):
        print("Le cours va commencer")  # Affiche "Le cours va commencer" lorsque la méthode est appelée


# Instanciation d'une Personne et d'un Eleve
personne = Personne()  # Crée une instance de la classe Personne avec l'âge par défaut
eleve = Eleve()  # Crée une instance de la classe Eleve avec l'âge par défaut

# Utilisation des méthodes pour l'élève et le professeur
eleve.bonjour()  # Affiche "Hello" pour l'élève
eleve.allerEnCours()  # Affiche "Je vais en cours" pour l'élève
eleve.modifierAge(15)  # Modifie l'âge de l'élève à 15 ans

professeur = Professeur("Mathématiques", age=40)  # Crée une instance de la classe Professeur avec l'âge à 40 ans
professeur.bonjour()  # Affiche "Hello" pour le professeur
professeur.enseigner()  # Affiche "Le cours va commencer" pour le professeur
