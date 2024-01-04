class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"
    
    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat, statut_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": statut_plat}
    
    # Méthode pour annuler une commande
    def annuler_commande(self):
        self.__statut_commande = "annulée"
    
    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total
    
    # Méthode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande {self.__numero_commande} - Statut : {self.__statut_commande}")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} - Prix : {details['prix']} - Statut : {details['statut']}")
        print(f"Total à payer : {total}")
    
    # Méthode pour calculer la TVA
    def calculer_TVA(self):
        total = self.__calculer_total()
        tva = total * 0.2  # Supposons une TVA de 20%
        return tva

# Utilisation de la classe Commande pour créer et manipuler une commande
ma_commande = Commande("123")
ma_commande.ajouter_plat("Pizza", 10, "en préparation")
ma_commande.ajouter_plat("Salade", 5, "prête")
ma_commande.afficher_commande()
print("TVA :", ma_commande.calculer_TVA())
ma_commande.annuler_commande()
ma_commande.afficher_commande()
