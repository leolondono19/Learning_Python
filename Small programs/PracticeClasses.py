class Estudiante():
    def __init__(self, nombre: str, edad: int, grado: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def __str__(self) -> str:
        return f"El estudiante {self.nombre} que tiene {self.edad} años y esta en {self.grado} grado esta estudiando"
    
    def estudiar(self) -> None:
        print(f"El estudiante {self.nombre} esta estudiando")
    
    @staticmethod
    def sumar(number1: int, number2: int) -> int:
        resultado = number1 + number2
        return resultado

    
resultado = Estudiante.sumar(12, 17)
print(resultado)

estudiante1 = Estudiante("Leonee", 22, "5to")
print(estudiante1)


""" 
print("Ingrese los datos del estudiante")
nombre: str = input("Ingrese el nombre del estudiante: \n")
edad: int = int(input("Ingrese la edad del estudiante: \n"))
grado: str = input("Ingrese el grado del estudiante: \n")

estudiante1 = Estudiante(nombre, edad, grado)

dato = input("Hay algo que quieras decirle al estudiante? \n")
if dato == "estudiar":
    print(estudiante1)
else:
    print("GRACIAS POR LA INFORMACION")
    """  