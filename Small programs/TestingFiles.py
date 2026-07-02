
class EmptyFile(Exception):
    pass

with open("text.txt", "r") as f:
    print(f.read())


