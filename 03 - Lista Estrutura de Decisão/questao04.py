# 4ª QUESTÃO
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
 print(f"{letra} é uma vogal.")
else:
 print(f"{letra} é uma consoante.")