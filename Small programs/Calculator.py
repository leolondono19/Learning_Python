import os
from typing import Any

def show_menu() -> None:
    print("\n----Menu----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def clean_display() -> None:
    os.system("cls")

def pause_display() -> None:
    os.system("pause")

def add(number1: float, number2: float) -> float:
    result = number1 + number2
    return result

def substract(number1: float, number2: float) -> float:
    result = number1 - number2
    return result

def multiplication(number1: float, number2: float) -> float:
    result = number1 * number2
    return result

def division(number1: float, number2: float) -> float:
    result = number1 / number2
    return result

def option_menu(option: str) -> None:
    result: float = 0.0
    number: float = 0.0
    exit: str = "0"
    counter: int = 0
    clean_display()
    while exit.replace(".", "", 1).isdigit():
        exit = input("Please enter a number: ")
        if exit.replace(".", "", 1).isdigit():
            number = float(exit)
        else:
            break

        if option == "1":
            result = add(result, number)

        elif option == "2":
            if counter == 0:
                result = abs(substract(result, number))
            else:
                result = substract(result, number)

        elif option == "3":
            if counter == 0:
                result = multiplication(1, number)
            else:
                result = multiplication(result, number)

        elif option == "4":
            if counter == 0:
                result = division(number, 1)
            else:
                result = division(result, number)
        
        if result.is_integer():
            print(int(result))
        else:
            print(result)
        counter += 1


while True:
    clean_display()
    show_menu()
    option: str = input("Welcome to my Calculator, choose an option: ")
    if option == "5":
        break
    option_menu(option)
