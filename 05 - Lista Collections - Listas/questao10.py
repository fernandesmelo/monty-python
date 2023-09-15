# 10ª QUESTÃO
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores 
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista_numeros = []
lista_letras = []
lista_total = []
cont = 0

while cont < 10:
    cont += 1
    numero = int(input("Informe um número: "))
    letra = input("Informe uma letra: ")
    lista_numeros.append(numero)
    lista_letras.append(letra)

cont = 0

while cont < 10:
    lista_total.append(lista_numeros[cont])
    lista_total.append(lista_letras[cont])
    cont += 1

print(lista_total)
