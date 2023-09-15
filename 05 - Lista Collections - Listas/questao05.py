# 5ª QUESTÃO
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
# números IMPARES no vetor impar. Imprima os três vetores.

pares = []
impares = []
lista_numeros = []

for c in range(1, 21):
    num = int(input(f"Informe o {c}º número: "))
    lista_numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista completa: {lista_numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
