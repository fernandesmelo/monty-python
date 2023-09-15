# 1ª QUESTÃO
# Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e 
# divisão.

num1 = float(input("\nInforme o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"\n{num1} + {num2} é igual a {soma}.")
print(f"{num1} - {num2} é igual a {sub}.")
print(f"{num1} x {num2} é igual a {mult}.")
print(f"{num1} / {num2} é igual a {round(div, 2)}.")
