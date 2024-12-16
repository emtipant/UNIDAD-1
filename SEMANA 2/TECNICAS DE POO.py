#Definición de una clase llamada "Persona"
class Persona:
    # Atributos de la clase
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    # Método de la clase para mostrar información
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Dirección: {self.direccion}")

    # Método de la clase para cambiar la dirección
    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

#Definición de una subclase llamada "Empleado"
class Empleado(Persona):
    # Atributos adicionales de la subclase
    def __init__(self, nombre, edad, direccion, cargo, salario):
        super().__init__(nombre, edad, direccion)
        self.cargo = cargo
        self.salario = salario

    # Método adicional de la subclase para mostrar información laboral
    def mostrar_info_laboral(self):
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")

#Creación de objetos
persona = Persona("Juan", 30, "Calle 123")
empleado = Empleado("Pedro", 35, "Avenida 456", "Gerente", 50000)

#Uso de métodos
persona.mostrar_info()
empleado.mostrar_info()
empleado.mostrar_info_laboral()

#Cambio de dirección
persona.cambiar_direccion("Calle 789")
empleado.cambiar_direccion("Avenida 901")

#Uso de métodos después del cambio de dirección
persona.mostrar_info()
empleado.mostrar_info()
