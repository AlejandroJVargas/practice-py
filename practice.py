# import random

# my_list = [10, 20, 30, 40, 50]
# my_list.append(60)
# my_list.extend([70, 80, 90])
# my_list.insert(2, 25)
# print(my_list)

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriz[0][1])

# try:
#     print(matriz[3][0])
# except IndexError:
#     print("Indice fuera del rango")


# def throwing_dices():
#     dice = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice + dice2
#     return dice, dice2, total


# while True:
#     dice_one, dice_two, total_dices = throwing_dices()
#     print(f"\nYou got in the first {dice_one} and in the second dice {dice_two}")
#     print(f"In total you got {total_dices}")
#     start_again = input("Do you want to play again? (yes/no): ").strip().lower()

#     if start_again != "yes":
#         print("\nYou stop playing the game!")
#         break

colores = ["rojo", "azul", "verde"]

for color in colores:
    print(color)

for i in range(len(colores)):
    print(f"Indice: {i} Colores: {colores[i]}")

for i, color in enumerate(colores):
    print(f"Indice {i}: Colores: {color}")

numeros = [1, 2, 3]
for i in range(len(numeros)):
    numeros[i] *= 2

print(numeros)

numeros1 = [1, 2, 3, 4]
dobles = [num * 2 for num in numeros1]
print(dobles)

edades = [12, 46, 8, 16, 18, 23, 27, 28]
mayores = [edad for edad in edades if edad > 18]
print(mayores)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

suma = 0
for fila in matriz:
    for valor in fila:
        suma += valor
print(suma)

usuarios = ["Alejandro", "Jose", "Carlos"]
for usuario in usuarios:
    print(f"Hola usuarios {usuario}")
