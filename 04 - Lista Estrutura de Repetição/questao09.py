# 9ª QUESTÃO
# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for cont in range(1, 51):
    if cont % 2 == 1:
        print(cont, end=" - ")

print()
