# 6ª QUESTÃO
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o 
# número de alunos com média maior ou igual a 7.0.

lista_medias = []
lista_aprovados = []
cont_aprovados = 0

for cont in range(1, 11):
    print(f"\nNOTAS - {cont}º ALUNO:")
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    nota3 = float(input("3ª nota: "))
    nota4 = float(input("4ª nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    lista_medias.append(media)
    
    if media >= 7:
        lista_aprovados.append(media)
        cont_aprovados += 1

print(f"\nMédias dos alunos: {lista_medias}")
print(f"Quantidade de alunos com média maior ou igual a sete: {cont_aprovados}.")

