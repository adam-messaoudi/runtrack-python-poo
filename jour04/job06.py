class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        # Méthode pour afficher les informations générales du véhicule
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")
    
        

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        # Méthode pour afficher les informations spécifiques à la voiture en plus des infos générales
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


# Instanciation d'un objet Voiture et appel de la méthode informationsVehicule
voiture = Voiture("Toyota", "Corolla", 2023, 25000)
voiture.informationsVehicule()


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        # Méthode pour afficher les informations spécifiques à la moto en plus des infos générales
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")


# Instanciation d'un objet Moto et appel de la méthode informationsVehicule
moto = Moto("Honda", "CBR500R", 2022, 8000)
moto.informationsVehicule()


class Vehicule:
    def demarrer(self):
        # Méthode générique pour démarrer un véhicule
        print("Attention, je roule")


class Voiture(Vehicule):
    def demarrer(self):
        # Surcharge de la méthode demarrer pour la classe Voiture
        print("La voiture démarre avec un vrombissement !")


class Moto(Vehicule):
    def demarrer(self):
        # Surcharge de la méthode demarrer pour la classe Moto
        print("La moto démarre avec un vrombissement !")


# Instanciation d'un objet Voiture et Moto et démarrage
voiture = Voiture()
moto = Moto()

voiture.demarrer()
moto.demarrer()
