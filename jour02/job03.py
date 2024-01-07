class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Initialisation des attributs du livre
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  # Initialisation de l'attribut disponible à True par défaut

    # Assesseurs et mutateurs pour le titre du livre
    def getTitre(self):
        return self.__titre

    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    # Assesseurs et mutateurs pour l'auteur du livre
    def getAuteur(self):
        return self.__auteur

    def setAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    # Assesseurs et mutateurs pour le nombre de pages du livre
    def getNbPages(self):
        return self.__nb_pages

    def setNbPages(self, nouveau_nb_pages):
        # Vérification que le nombre de pages est un nombre entier positif
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.__disponible:  # Vérification si le livre est disponible
            self.__disponible = False  # Rendre le livre indisponible (disponible = False)
            print("Livre emprunté avec succès!")
        else:
            print("Le livre n'est pas disponible pour emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.__disponible:  # Vérification si le livre n'est pas disponible
            self.__disponible = True  # Rendre le livre disponible (disponible = True)
            print("Livre rendu avec succès!")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
mon_livre = Livre("Harry Potter", "J.K. Rowling", 400)

print(mon_livre.verification())  # Vérifier si le livre est disponible (doit afficher True)

mon_livre.emprunter()  # Emprunter le livre
print(mon_livre.verification())  # Vérifier à nouveau (doit afficher False)

mon_livre.rendre()  # Rendre le livre
print(mon_livre.verification())  # Vérifier à nouveau (doit afficher True)
