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
