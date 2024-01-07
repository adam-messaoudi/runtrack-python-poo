class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes avec des valeurs de construction
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Alice")
personne3 = Personne("Johnson", "Emma")

# Appel à la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())

