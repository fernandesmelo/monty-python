# 8ª QUESTÃO
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a 
# idade e a altura na ordem inversa a ordem lida.

lista_idades = []
lista_alturas = []

for cont in range(1, 6):
    print(f"\nDados da {cont}ª pessoa:")
    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura em metros: "))
    lista_idades.append(idade)
    lista_alturas.append(altura)

print(f"\nIdades: {lista_idades[::-1]}")
print(f"Alturas: {lista_alturas[::-1]}")
