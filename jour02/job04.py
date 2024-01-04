<<<<<<< HEAD
# Création de la classe Personne avec des attributs nom et prenom, ainsi qu'une méthode SePresenter
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom  # Initialisation de l'attribut nom
        self.prenom = prenom  # Initialisation de l'attribut prenom
    
    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"  # Méthode pour présenter la personne

# Instanciation de plusieurs personnes avec des valeurs spécifiques et appel à la méthode SePresenter
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Alice")
print(personne1.SePresenter())
print(personne2.SePresenter())
=======
class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0  # Attribut privé credits par défaut à zéro
    
    # Mutateur pour ajouter des crédits avec validation
    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
        else:
            print("La valeur des crédits ajoutés doit être supérieure à zéro.")
    
    # Méthode pour obtenir le total de crédits de l'étudiant
    def get_credits(self):
        return self.__credits

# Instanciation de l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student("John", "Doe", 145)

# Ajout de crédits à l'étudiant John Doe et impression du total de crédits
john_doe.add_credits(20)
john_doe.add_credits(30)
john_doe.add_credits(40)

print("Total de crédits de l'étudiant John Doe est de :", john_doe.get_credits(),"points")
>>>>>>> f031f0c4267ae09390c3502473bf1039b5525d01
