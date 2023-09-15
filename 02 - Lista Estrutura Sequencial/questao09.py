# 9ª QUESTÃO
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
# C = 5 * ((F-32) / 9).

graus_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))

graus_celsius = 5 * ((graus_fahrenheit - 32) / 9)

print(f"Graus Celsius: {round(graus_celsius, 2)}ºC")
