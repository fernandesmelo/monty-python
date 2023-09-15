# 10ª QUESTÃO
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. F = (C * 1,8) + 32.

graus_celsius = float(input("Informe a temperatura em graus Celsius: "))

graus_fahrenheit = (graus_celsius * 1.8) + 32

print(f"Graus Fahrenheit: {round(graus_fahrenheit,2)}ºF")