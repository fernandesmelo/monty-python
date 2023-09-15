# 1ª QUESTÃO
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.

nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("Valor inválido. Digite novamente.")
    nota = float(input("Digite uma nota: "))

print(f"A nota é {nota}.")
