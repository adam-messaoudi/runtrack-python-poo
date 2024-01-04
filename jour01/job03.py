# Ajout d'une méthode addition à la classe Operation pour effectuer une addition
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        result = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", result)

# Utilisation de la méthode addition pour effectuer une opération
operation_instance = Operation(5, 3)
operation_instance.addition()
