# 1ª QUESTÃO
# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista_num_inteiros = []

for cont in range(5):
    num = int(input(f"Informe o {cont + 1}º número inteiro: "))
    lista_num_inteiros.append(num)

print(lista_num_inteiros)
