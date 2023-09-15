# 8ª QUESTÃO
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
# total do seu salário no referido mês.

valor_hora = float(input("Informe quanto você ganha por hora trabalahada: R$"))
qtd_horas = int(input("Agora informe quantas horas você trabalhou no mês: "))

total_salario = valor_hora * qtd_horas

print(f"Seu salário do mês é: R${total_salario}")