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
