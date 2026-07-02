from typing import Any

"""
count = 0
for x in range(3):
    for y in range(3):
        print(f"[{x},{y}]", end=" ")
        count += 1
    print()
"""

"""
iterator = 0
while iterator<10:
    print(iterator)
    iterator+=1

    lista: Any = ["Leonee", 12, True]
tupla: Any = ("Leonee", 12, True)
print(tupla[0])
tupla[0] = "Jimmy"
print(tupla[0])
"""
a = 13
def addition(number1:int, number2:int) -> int:
    global a
    a = 10
    result = number1 + number2
    return result

result = addition(a, 14)
print(result)
print(a)


name = "Leonee"
def print_text(text:str):
    global name
    name = "Jimmy"
    print(text)

print_text(name)




