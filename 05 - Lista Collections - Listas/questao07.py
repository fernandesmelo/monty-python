# 7ª QUESTÃO
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
# multiplicação e os números.

lista_num_inteiros = []
soma = 0
mult = 1

for c in range(1, 6):
    valor = int(input(f"Informe o {c}º número inteiro: "))
    lista_num_inteiros.append(valor)
    soma += valor
    mult *= valor
    print(f"Números: {lista_num_inteiros}")

print(f"Soma: {soma}")
print(f"Multiplicação: {mult}")
