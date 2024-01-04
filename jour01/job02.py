<<<<<<< HEAD
# Définition de la classe Operation
class Operation:
    def __init__(self, nombre1=10, nombre2=6):
        self.nombre1 = nombre1  # Initialisation de l'attribut nombre1
        self.nombre2 = nombre2  # Initialisation de l'attribut nombre2

# Instanciation de la classe et impression de l'objet
operation_instance = Operation()

# Impression des attributs nombre1 et nombre2 de l'instance de la classe Operation
print("Le nombre est",operation_instance.nombre1)
print("Le nombre est",operation_instance.nombre2)
=======
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre  # Attribut privé titre
        self.__auteur = auteur  # Attribut privé auteur
        self.__nb_pages = nb_pages  # Attribut privé nb_pages
    
    # Assesseurs pour obtenir les valeurs des attributs
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def getNbPages(self):
        return self.__nb_pages
    
    # Mutateurs pour modifier les valeurs des attributs, avec validation pour nb_pages
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def setAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def setNbPages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Nombre de pages invalide. Veuillez saisir un nombre entier positif.")

# Utilisation de la classe Livre et des mutateurs pour modifier et afficher les attributs
mon_livre = Livre("Harry Potter", "J.K. Rowling", 300)
mon_livre.setNbPages(400)
print("Titre :", mon_livre.getTitre())
print("Auteur :", mon_livre.getAuteur())
print("Nombre de pages :", mon_livre.getNbPages())
>>>>>>> f031f0c4267ae09390c3502473bf1039b5525d01
