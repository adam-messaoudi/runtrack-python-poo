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

    # Autres méthodes ici

# Instanciation d'un étudiant, ajout de crédits et impression du total de crédits
etudiant = Student("John", "Doe", 145)
etudiant.add_credits(20)
etudiant.add_credits(30)
etudiant.add_credits(40)
print("Total de crédits de l'étudiant :", etudiant.get_credits())

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
    
    # Méthode privée pour évaluer le niveau de l'étudiant
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        level = self.__studentEval()
        print(f"Informations de l'étudiant : {self.__nom} {self.__prenom} ({self.__numero_etudiant}) - Niveau : {level}")

# Instanciation d'un étudiant, ajout de crédits et impression des informations de l'étudiant
etudiant = Student("John", "Doe", 145)
etudiant.add_credits(20)
etudiant.add_credits(30)
etudiant.add_credits(40)
etudiant.studentInfo()
