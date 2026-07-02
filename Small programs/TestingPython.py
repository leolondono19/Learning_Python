from typing import Any

numero1 = 12
numero2 = 34

resultado = numero1 + numero2

print(f"El resultado es {resultado}")

for x in range(1, 16):
    print(x)

coleccion: list[Any] = ["Leonee", 2, 3]

for i in coleccion:
    print(i)

diccionario = {"Leonee":22, "Maria":12, "Juan":18, "Jimmy":20}
for i in diccionario:
    print(f"Elementos: {diccionario[i]}")

for clave, valor in diccionario.items():
    print(f"{clave} tiene {valor}")


dictionary = {"1" : {1 : 2}}
print (dictionary.values())


