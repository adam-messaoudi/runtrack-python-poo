class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  # Attribut privé disponible par défaut à True
    
    # Assesseurs pour obtenir les valeurs des attributs
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def getNbPages(self):
        return self.__nb_pages
    
    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible
    
    # Méthode pour emprunter le livre (rendre indisponible)
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print("Le livre est déjà emprunté.")
    
    # Méthode pour rendre le livre (le rendre disponible)
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
        else:
            print("Le livre est déjà disponible.")

# Utilisation de la classe Livre et de ses méthodes pour gérer la disponibilité
mon_livre = Livre("Python for Beginners", "John Doe", 200)
print("Disponibilité avant emprunt :", mon_livre.verification())
mon_livre.emprunter()
print("Disponibilité après emprunt :", mon_livre.verification())
mon_livre.rendre()
print("Disponibilité après rendu :", mon_livre.verification())
