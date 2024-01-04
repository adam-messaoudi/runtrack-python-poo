class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
            self.__level = self.__studentEval()
        else:
            print("La valeur des crédits ajoutés doit être supérieure à zéro.")
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Moyen"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print(f"Nom de l'étudiant : {self.__nom}")
        print(f"Prénom de l'étudiant : {self.__prenom}")
        print(f"id de l'étudiant : {self.__numero_etudiant}")
        print(f"Niveau de l'étudiant : {self.__level}")
    
    # Getter pour récupérer le nombre de crédits
    def get_credits(self):
        return self.__credits

john_doe = Student("John", "Doe", 145)
john_doe.add_credits(10)
john_doe.add_credits(30)
john_doe.add_credits(40)

# Affichage du total de crédits et des informations de l'étudiant
print("Total de crédits de l'étudiant John Doe :", john_doe.get_credits())
john_doe.studentInfo()
