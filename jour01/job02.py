class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe Operation avec les valeurs par défaut
operation_instance = Operation()

# Impression des valeurs des attributs "nombre1" et "nombre2" de l'objet
print(f"La Valeur de nombre1 est {operation_instance.nombre1}")
print(f"La Valeur de nombre2 est {operation_instance.nombre2}")
