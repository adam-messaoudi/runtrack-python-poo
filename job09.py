# Création de la classe Produit avec des méthodes pour manipuler et afficher les informations sur le produit
class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom  # Initialisation de l'attribut nom du produit
        self.prixHT = prixHT  # Initialisation de l'attribut prixHT du produit
        self.TVA = TVA  # Initialisation de l'attribut TVA du produit
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)  # Méthode pour calculer le prix TTC
    
    def afficher(self):
        print(f"Nom du produit : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}%")  # Méthode pour afficher les informations du produit
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom  # Méthode pour modifier le nom du produit
    
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix  # Méthode pour modifier le prix du produit
    
    def getNom(self):
        return self.nom  # Méthode pour obtenir le nom du produit
    
    def getPrixHT(self):
        return self.prixHT  # Méthode pour obtenir le prix HT du produit
    
    def getTVA(self):
        return self.TVA  # Méthode pour obtenir la TVA du produit

# Utilisation de la classe Produit pour créer des produits, les modifier et afficher leurs informations
produit1 = Produit("Livre", 10, 5)
produit2 = Produit("Montre", 50, 10)

print("Prix TTC du produit 1 :", produit1.CalculerPrixTTC())
print("Prix TTC du produit 2 :", produit2.CalculerPrixTTC())

produit1.modifierNom("Roman")
produit1.modifierPrix(12)
produit2.modifierNom("Bracelet")
produit2.modifierPrix(60)

print("Nouveau prix du produit 1 :", produit1.getPrixHT())
print("Nouveau nom du produit 1 :", produit1.getNom())
print("Nouveau prix du produit 2 :", produit2.getPrixHT())
print("Nouveau nom du produit 2 :", produit2.getNom())
