
animal= "  peRRito contenTO  "

print(animal.upper())
print(animal.lower())
print(animal.capitalize()) #mayuscula a la primera
print(animal.title()) #mayuscula a cada letra principal de la palabra, el resto en minuscula
print(animal.strip()) #borra los espacios laterales

print(animal.strip().capitalize())

print(animal.lstrip())
print(animal.rstrip())

print(animal.find("Rito"))

print(animal.replace("Rito", "RatZo"))

print("Rit" in animal)

print("Rit" not in animal)
