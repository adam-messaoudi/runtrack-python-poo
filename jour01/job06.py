<<<<<<< HEAD
# Création de la classe Animal avec des attributs âge et prenom, ainsi que des méthodes pour vieillir et nommer
class Animal:
    def __init__(self):
        self.age = 0  # Initialisation de l'attribut âge
        self.prenom = ""  # Initialisation de l'attribut prenom
    
    def vieillir(self):
        self.age += 1  # Méthode pour augmenter l'âge de l'animal
    
    def nommer(self, nom):
        self.prenom = nom  # Méthode pour donner un nom à l'animal

# Utilisation de la classe Animal et de ses méthodes pour gérer l'âge et le nom de l'animal
animal_instance = Animal()
print("Âge initial de l'animal :", animal_instance.age)
animal_instance.vieillir()
print("Âge après vieillissement :", animal_instance.age)
animal_instance.nommer("Rex")
print("Nom de l'animal :", animal_instance.prenom)
=======
class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats commandés
        self.__statut_commande = "En cours"  # Statut initial de la commande
    
    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix, statut="Non livré"):
        self.__plats_commandes[nom_plat] = {"prix": prix, "statut": statut}
    
    # Méthode pour annuler une commande
    def annuler_commande(self):
        self.__plats_commandes.clear()  # Vide la liste des plats pour annuler la commande
        self.__statut_commande = "Annulée"  # Met à jour le statut de la commande
    
    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total
    
    # Méthode pour afficher une commande avec son total à payer
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande numéro {self.__numero_commande}:")
        for plat, details in self.__plats_commandes.items():
            print(f"- Plat : {plat}, Prix : {details['prix']}, Statut : {details['statut']}")
        print(f"Total à payer : {total} €")
    
    # Méthode pour calculer la TVA
    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva

# Exemple d'utilisation de la classe Commande
ma_commande = Commande("123")
ma_commande.ajouter_plat("Pizza", 12.5)
ma_commande.ajouter_plat("Salade", 8.0)
ma_commande.ajouter_plat("Boisson", 3.0)

ma_commande.afficher_commande()

tva = ma_commande.calculer_tva(20)
print(f"TVA à payer : {tva} €")

ma_commande.annuler_commande()
ma_commande.afficher_commande()
>>>>>>> f031f0c4267ae09390c3502473bf1039b5525d01
