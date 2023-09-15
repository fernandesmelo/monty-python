# 4ª QUESTÃO
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_letras = []
cont = 0

for c in range(1, 11):
    letra = input("Informe uma letra: ")
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        lista_letras.append(letra)
        cont += 1

print(f"Foram encontradas {cont} consoantes, que são: {lista_letras}.")
