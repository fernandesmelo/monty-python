# 6ª QUESTÃO
# Faça um Programa que leia três números e mostre o maior deles.

num1 = input("Informe um número: ")
num2 = input("Informe outro número: ")
num3 = input("Agora informe mais outro número: ")

if num1 > num2 and num1 > num3:
 print(f"{num1} é o maior número entre os três números informados.")
elif num2 > num1 and num2 > num3:
 print(f"{num2} é o maior número entre os três números informados.")
else:
 print(f"{num3} é o maior número entre os três números informados.")