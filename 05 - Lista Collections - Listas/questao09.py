# 9ª QUESTÃO
# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do 
# vetor.

lista_A = []
soma = 0

for c in range(1, 11):
    num = int(input("Informe um número inteiro: "))
    quadrado = num ** 2
    soma += quadrado
    lista_A.append(quadrado)
    print(f"Quadrado: {quadrado}")

print(f"A soma dos quadrados dos elementos do vetor é igual a {soma}.")
