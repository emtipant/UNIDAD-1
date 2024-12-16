# Abstracción de un vehículo

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__velocidad = 0

    def acelerar(self):
        self.__velocidad += 20

    def frenar(self):
        if self.__velocidad > 0:
            self.__velocidad -= 20

    def get_velocidad(self):
        return self.__velocidad

#Creación de objetos
coche = Vehiculo("Ford", "Focus", 2018)

#Uso de métodos
coche.acelerar()
print("Velocidad:", coche.get_velocidad())
coche.frenar()
print("Velocidad:", coche.get_velocidad())
