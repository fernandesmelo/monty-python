# 9ª QUESTÃO
# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = input("Informe um número: ")
num2 = input("Informe outro número: ")
num3 = input("Agora informe mais outro número: ")

if num1 > num2 and num1 > num3 and num2 > num3:
 print(f"Números informados em ordem decrescente: {num1}, {num2}, {num3}")
elif num1 > num2 and num1 > num3 and num2 < num3 :
 print(f"Números informados em ordem decrescente: {num1}, {num3}, {num2}")
elif num1 < num2 and num1 > num3 and num2 > num3:
 print(f"Números informados em ordem decrescente: {num2}, {num1}, {num3}")
elif num1 > num2 and num1 < num3 and num2 < num3:
 print(f"Números informados em ordem decrescente: {num3}, {num1}, {num2}")
elif num1 < num2 and num1 < num3 and num2 > num3:
 print(f"Números informados em ordem decrescente: {num2}, {num3}, {num1}")
else:
 print(f"Números informados em ordem decrescente: {num3}, {num2}, {num1}")
