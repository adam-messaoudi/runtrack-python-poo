class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre  # Attribut privé pour le titre
        self.__auteur = auteur  # Attribut privé pour l'auteur
        self.__nb_pages = nb_pages  # Attribut privé pour le nombre de pages

    # Assesseur pour le titre
    def getTitre(self):
        return self.__titre

    # Mutateur pour le titre
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    # Assesseur pour l'auteur
    def getAuteur(self):
        return self.__auteur

    # Mutateur pour l'auteur
    def setAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    # Assesseur pour le nombre de pages
    def getNbPages(self):
        return self.__nb_pages

    # Mutateur pour le nombre de pages
    def setNbPages(self, nouveau_nb_pages):
        # Vérification si le nouveau nombre de pages est valide
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")

# Exemple d'utilisation
mon_livre = Livre("Harry Potter", "J.K. Rowling", 400)

# Affichage des attributs initiaux
print(f"Titre: {mon_livre.getTitre()}, Auteur: {mon_livre.getAuteur()}, Nombre de pages: {mon_livre.getNbPages()}")

# Modification des attributs
mon_livre.setTitre("Le Seigneur des Anneaux")
mon_livre.setAuteur("J.R.R. Tolkien")
mon_livre.setNbPages(600)

# Affichage des nouveaux attributs
print(f"Nouveau titre: {mon_livre.getTitre()}, Nouvel auteur: {mon_livre.getAuteur()},Nouveau nombre de pages: {mon_livre.getNbPages()}")
