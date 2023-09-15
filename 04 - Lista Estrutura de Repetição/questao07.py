# 7ª QUESTÃO
# Faça um programa que leia 5 números e informe o maior número.

maior = None  

for cont in range(1, 6):
    num = int(input("Informe um número: "))
    if maior is None or num > maior:
        maior = num

print(f"O maior número foi {maior}.")
