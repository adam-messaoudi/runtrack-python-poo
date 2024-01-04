# Définition de la classe Operation
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1  # Initialisation de l'attribut nombre1
        self.nombre2 = nombre2  # Initialisation de l'attribut nombre2

# Instanciation de la classe et impression de l'objet
operation_instance = Operation()

# Impression des attributs nombre1 et nombre2 de l'instance de la classe Operation
print(operation_instance.nombre1)
print(operation_instance.nombre2)
