# 7ª QUESTÃO
# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Agora digite mais um número: "))

maior = num1
menor = num1

if num2 > maior:
 maior = num2
if num3 > num2:
 maior = num3
if num2 < menor:
 menor = num2
if num3 < menor:
 menor = num3

print(f"O maior número é {maior} e o menor número é {menor}.")