class Student:
    def __init__(self, nom, prenom, num_etudiant):
        # Initialisation des attributs privés
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0  # Crédits initiaux par défaut à zéro
        self.__level = self.__studentEval()  # Initialisation du niveau de l'étudiant

    # Méthode pour ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:  # Vérification que le nombre de crédits est valide
            self.__credits += credits  # Ajout des crédits
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

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
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant: {self.__num_etudiant}")
        print(f"Niveau: {self.__level}")

# Instanciation de l'étudiant John Doe avec le numéro 145
etudiant = Student("John", "Doe", 145)

# Ajout de crédits à trois reprises
etudiant.add_credits(20)
etudiant.add_credits(30)
etudiant.add_credits(40)

# Affichage des informations de l'étudiant
etudiant.studentInfo()
