class Operation:
    def __init__(self, nombre1=5, nombre2=20):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {result}")

# Instanciation de la classe Operation avec les valeurs par défaut
operation_instance = Operation()

# Appel de la méthode addition pour effectuer l'addition et afficher le résultat
operation_instance.addition()
