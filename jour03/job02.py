class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        # Initialisation des attributs du compte
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert  # Booléen indiquant si le découvert est autorisé

    def afficher(self):
        # Méthode pour afficher les détails du compte
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde}")
        print(f"Découvert autorisé : {self.__decouvert}")

    def afficherSolde(self):
        # Affiche le solde actuel du compte
        print(f"Le solde du compte est de : {self.__solde}")

    def versement(self, montant):
        # Méthode pour effectuer un versement sur le compte
        self.__solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde : {self.__solde}")

    def retrait(self, montant):
        # Méthode pour effectuer un retrait du compte
        if self.__decouvert or (self.__solde - montant) >= 0:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.__solde}")
        else:
            print("Opération impossible : solde insuffisant.")

    def agios(self):
        # Méthode pour appliquer des agios en cas de solde négatif
        if self.__solde < 0:
            self.__solde *= 1.05  # Appliquer des agios de 5% au solde négatif
            print("Des agios ont été appliqués.")
        else:
            print("Pas de solde négatif, pas d'agios à appliquer.")

    def virement(self, compte_destinataire, montant):
        # Méthode pour effectuer un virement vers un autre compte
        if (self.__decouvert or self.__solde >= montant) and montant > 0:
            compte_destinataire.versement(montant)
            self.retrait(montant)
            print("Virement effectué avec succès.")
        else:
            print("Opération de virement impossible.")

# Création d'un compte bancaire
compte_1 = CompteBancaire(1, "Doe", "John", 500)
compte_1.afficher()

# Opérations sur le compte bancaire
compte_1.versement(300)
compte_1.retrait(200)
compte_1.agios()
compte_1.afficherSolde()

# Création d'un compte bancaire avec découvert
compte_2 = CompteBancaire(2, "Smith", "Alice", -200, decouvert=True)
compte_2.afficher()

# Virement du compte_1 vers le compte_2 pour remettre ce dernier à zéro
compte_1.virement(compte_2, 700)
compte_2.afficherSolde()
compte_1.afficherSolde()
