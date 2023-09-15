# 4ª QUESTÃO
# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
# de crescimento.

paisA = 80000
paisB = 200000
qtd_anos = 0

while paisB > paisA:
 populacao_paisA = paisA * 0.03
 populacao_paisB = paisB * 0.015
 paisA = paisA + populacao_paisA
 paisB = paisB + populacao_paisB
 qtd_anos = qtd_anos + 1
 
print(f"O país A passará o país B em {qtd_anos} anos")
