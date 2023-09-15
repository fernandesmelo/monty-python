# 7ª QUESTÃO
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

cumprimento = int(input("Informe o cumprimento do quadrado: "))
largura = int(input("Agora informe a largura do quadrado: "))

area_quadrado = cumprimento * largura
dobro_area = area_quadrado + area_quadrado

print(f"O dobro da área do quadrado é: {dobro_area}")