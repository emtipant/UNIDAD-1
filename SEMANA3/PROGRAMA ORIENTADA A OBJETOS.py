#calcular el promedio semanal y manejar una lista de temperaturas

print("Promedio diario de temperatura")
class Clima:
    def __init__(self):
        self.temperaturas = []

    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_temperaturas(self):
        for i, temperatura in enumerate(self.temperaturas):
            print(f"Día {i+1}: {temperatura}°C")

#Creación de objetos
clima = Clima()

#Agregar temperaturas
clima.agregar_temperatura(23)
clima.agregar_temperatura(31)
clima.agregar_temperatura(25)
clima.agregar_temperatura(29)
clima.agregar_temperatura(28)
clima.agregar_temperatura(26)
clima.agregar_temperatura(20)

#Mostrar temperaturas
clima.mostrar_temperaturas()

#Calcular promedio semanal
promedio_semanal = clima.calcular_promedio_semanal()
print(f"Promedio semanal: {promedio_semanal}°C")
