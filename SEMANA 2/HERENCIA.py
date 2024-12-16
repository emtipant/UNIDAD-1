#Herencia de una clase "Persona"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}")

class Profesor(Persona):
    def __init__(self, docente, edad, asignatura):
        super().__init__(docente, edad)
        self.asignatura = asignatura

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")

#Creación de objetos
estudiante = Estudiante("ERIKA", 20, "Ingeniería en tecnologias de la imformacion")
profesor = Profesor("María", 35, "sistemas")

#Uso de métodos
estudiante.mostrar_info()
profesor.mostrar_info()
