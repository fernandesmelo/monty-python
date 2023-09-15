# 8ª QUESTÃO
# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for cont in range(1, 6):
    num = int(input("Informe um número: "))
    soma = soma + num

print(f"A soma dos números é igual a {soma}.")
