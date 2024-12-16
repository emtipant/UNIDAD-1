#Encapsulamiento de un vehículo

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__velocidad = 0

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_velocidad(self):
        return self.__velocidad

    def acelerar(self):
        self.__velocidad += 20

    def frenar(self):
        if self.__velocidad > 0:
            self.__velocidad -= 20

#Creación de objetos
coche = Vehiculo("Chevrolet", "luv dimax", 2018)

#Uso de métodos
print("Marca:", coche.get_marca())
print("Modelo:", coche.get_modelo())
print("Año:", coche.get_año())
print("Velocidad:", coche.get_velocidad())
coche.acelerar()
print("Velocidad después de acelerar:", coche.get_velocidad())
coche.frenar()
print("Velocidad después de frenar:", coche.get_velocidad())
