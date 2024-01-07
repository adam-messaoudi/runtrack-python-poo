class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une Personne et d'un Eleve
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()

# Faire dire bonjour à l'élève et aller en cours
eleve.bonjour()
eleve.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
eleve.modifierAge(15)

# Instanciation d'un professeur de 40 ans
professeur = Professeur("Mathématiques")
professeur.modifierAge(40)

# Faire dire bonjour au professeur et commencer le cours
professeur.bonjour()
professeur.enseigner()
