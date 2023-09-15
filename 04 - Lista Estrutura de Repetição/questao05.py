# 5ª QUESTÃO
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a 
# entrada e permita repetir a operação.

populacaoA = int(input("Qual a população do país A? "))
taxa_crescimentoA = float(input("Qual a taxa de crescimento anual do país A em percentual? "))
populacaoB = int(input("Qual a população do país B? "))
taxa_crescimentoB = float(input("Qual a taxa de crescimento anual do país B em percentual? "))
anos = 0

if populacaoA > populacaoB:
    while populacaoA > populacaoB:
        crescimentoA = populacaoA * (taxa_crescimentoA / 100)
        crescimentoB = populacaoB * (taxa_crescimentoB / 100)
        populacaoA += crescimentoA
        populacaoB += crescimentoB
        anos += 1
    print(f"Levará {anos} anos para a população do país B ultrapassar a do país A.")
elif populacaoB > populacaoA:
    while populacaoB > populacaoA:
        crescimentoA = populacaoA * (taxa_crescimentoA / 100)
        crescimentoB = populacaoB * (taxa_crescimentoB / 100)
        populacaoA += crescimentoA
        populacaoB += crescimentoB
        anos += 1
    print(f"Levará {anos} anos para a população do país A ultrapassar a do país B.")
else:
    print("As populações dos dois países são iguais.")
