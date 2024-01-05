class CompteBancaire:
    # Initialisation de la classe avec ses attributs
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte  # Attribut privé : numéro de compte
        self.__nom = nom  # Attribut privé : nom du titulaire
        self.__prenom = prenom  # Attribut privé : prénom du titulaire
        self.__solde = solde  # Attribut privé : solde du compte
        self.__decouvert = decouvert  # Attribut privé : autorisation de découvert

    # Méthode pour afficher les détails du compte
    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Titulaire : {self.__prenom} {self.__nom}")
        print(f"Solde : {self.__solde}")

    # Méthode pour afficher uniquement le solde du compte
    def afficherSolde(self):
        print(f"Solde du compte : {self.__solde}")

    # Méthode pour effectuer un versement
    def versement(self, montant):
        self.__solde += montant

    # Méthode pour effectuer un retrait
    def retrait(self, montant):
        # Vérifie si le solde est suffisant ou si le découvert est autorisé
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.__solde}")
        else:
            print("Solde insuffisant. Opération impossible.")

    # Méthode pour appliquer des agios si le solde est négatif
    def agios(self, taux_agios):
        if self.__solde < 0:
            self.__solde *= (1 + taux_agios / 100)

    # Méthode pour effectuer un virement vers un autre compte
    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            print(f"Virement de {montant} effectué vers {compte_destinataire.__numero_compte}")
        else:
            print("Solde insuffisant pour effectuer le virement.")

# Création d'un compte avec des valeurs au choix
compte1 = CompteBancaire("12345", "Doe", "John", 500, decouvert=True)
compte1.afficher()

# Création d'un deuxième compte en découvert
compte2 = CompteBancaire("54321", "Smith", "Alice", -200, decouvert=True)
compte2.afficher()

# Faire un versement du premier compte vers le deuxième pour le remettre à zéro
compte1.virement(compte2, 500)
compte1.afficher()
compte2.afficher()
