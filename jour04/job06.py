class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        # Affiche les informations générales du véhicule
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")

    def demarrer(self):
        # Message générique pour démarrer le véhicule
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        # Affiche les informations de la voiture et son nombre de portes
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        # Message spécifique pour démarrer une voiture
        print("La voiture démarre!")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        # Affiche les informations de la moto et son nombre de roues
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        # Message spécifique pour démarrer une moto
        print("La moto démarre!")


# Instanciation et appel des méthodes
ma_voiture = Voiture("Toyota", "Corolla", 2023, 25000)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

print("\n")  # Saut de ligne ajouté

ma_moto = Moto("Yamaha", "YZF-R6", 2022, 12000)
ma_moto.informationsVehicule()
ma_moto.demarrer()
