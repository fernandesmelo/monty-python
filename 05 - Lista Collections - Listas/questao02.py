# 2ª QUESTÃO
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
# inversa.

lista_num_reais = []

for cont in range(10):
    num = float(input(f"Informe o {cont + 1}º número real: "))
    lista_num_reais.append(num)

print(lista_num_reais[::-1])
