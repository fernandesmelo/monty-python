# 3ª QUESTÃO
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_notas = []
soma = 0

for i in range(4):
    nota = float(input(f"Informe a {i + 1}ª nota: "))
    lista_notas.append(nota)
    soma += nota

media = soma / 4

print(f"As notas foram: {lista_notas}")
print(f"A média das notas é: {round(media, 2)}")
