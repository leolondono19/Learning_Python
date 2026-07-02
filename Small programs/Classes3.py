from typing import Protocol

class Archivo:
    def leer(self) -> None:
        print("Leyendo archivo")


class BaseDatos:
    def leer(self) -> None:
        print("Leyendo base de datos")

class Perro:
    def ladrar(self) -> None:
        print("waf")

class Leible(Protocol):
    def leer(self):
        pass

def procesar(objeto: Leible):
    objeto.leer()

archivo: Archivo = Archivo()
bas: BaseDatos = BaseDatos()
perro1: Perro = Perro()
procesar(archivo)
procesar(bas)
procesar(perro1)
