#Polimorfismo con funciones

def saludar(persona):
    print(persona.saludar())

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"BEEP BEEP, soy {self.nombre}"

#Creación de objetos
persona = Persona("BENDER")
robot = Robot("DOBLADOR-D2")

#Uso de la función
saludar(persona)
saludar(robot)
