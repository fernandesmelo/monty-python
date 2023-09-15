# 8ª QUESTÃO
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão 
# é sempre pelo mais barato.

produto1 = input("Informe o valor do 1º produro: R$")
produto2 = input("Informe o valor do 2º produto: R$")
produto3 = input("Agora informe o valor do 3º produto: R$")

if produto1 < produto2 and produto1 < produto3:
 print(f"O produto que você deve comprar é o de R${produto1}. Pois é o mais barato.")
elif produto2 < produto1 and produto2 < produto3:
 print(f"O produto que você deve comprar é o de R${produto2}. Pois é o mais barato.")
else:
 print(f"O produto que você deve comprar é o de R${produto3}. Pois é o mais barato.")