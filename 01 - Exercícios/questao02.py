# 2ª QUESTÃO
# Leia a idade do usuário e classifique-o em:
# ▶ Criança – 0 a 12 anos
# ▶ Adolescente – 13 a 17 anos
# ▶ Adulto – acima de 18 anos
# ▶ Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.

idade = int(input("Qual a sua idade? "))

if idade < 0:
 print("Idade inválida. Tente novamente.")
elif idade >= 0 and idade < 13:
 print("Você é uma criança.")
elif idade > 12 and idade < 18:
 print("Você é um adolescente.")
else:
 print("Você é um adulto.")