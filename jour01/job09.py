class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom  # Initialisation de l'attribut nom
        self.prixHT = prixHT  # Initialisation de l'attribut prixHT
        self.TVA = TVA  # Initialisation de l'attribut TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)  # Calcul du prix TTC en fonction de la TVA

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}"  # Affichage des informations du produit

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom  # Méthode pour modifier le nom du produit

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix  # Méthode pour modifier le prix HT du produit

    def obtenirNom(self):
        return self.nom  # Méthode pour obtenir le nom du produit

    def obtenirPrixHT(self):
        return self.prixHT  # Méthode pour obtenir le prix HT du produit

    def obtenirTVA(self):
        return self.TVA  # Méthode pour obtenir la TVA du produit
# Création de quelques produits
produit1 = Produit("Livre", 15, 0.2)
produit2 = Produit("Ordinateur", 1200, 0.25)
produit3 = Produit("Montre", 100, 0.15)

# Calcul des prix TTC des produits
prix_ttc_produit1 = produit1.CalculerPrixTTC()
prix_ttc_produit2 = produit2.CalculerPrixTTC()
prix_ttc_produit3 = produit3.CalculerPrixTTC()

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouveau Livre")
produit2.modifierPrixHT(1300)

# Affichage des nouveaux prix des produits
nouveau_prix_ttc_produit1 = produit1.CalculerPrixTTC()
nouveau_prix_ttc_produit2 = produit2.CalculerPrixTTC()
nouveau_prix_ttc_produit3 = produit3.CalculerPrixTTC()

print(f"Nouveau prix TTC produit 1: {nouveau_prix_ttc_produit1}")
print(f"Nouveau prix TTC produit 2: {nouveau_prix_ttc_produit2}")
print(f"Nouveau prix TTC produit 3: {nouveau_prix_ttc_produit3}")
