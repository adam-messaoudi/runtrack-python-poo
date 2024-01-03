# Définition de la classe Operation
class Operation:
    # Le constructeur de la classe, appelé lors de l'instanciation
    def __init__(self, nombre1=0, nombre2=0):
        # Initialisation des attributs nombre1 et nombre2 avec des valeurs par défaut
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe et impression de l'objet en console
# Un objet op est créé en utilisant le constructeur par défaut (sans paramètres)
op = Operation()

# Impression des valeurs des attributs de l'objet op en console
# Ceci affiche les valeurs par défaut de nombre1 et nombre2, qui sont 0 dans ce cas
print(op.nombre1, op.nombre2)
