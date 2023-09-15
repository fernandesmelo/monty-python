# 3ª QUESTÃO
# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por
# litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta
# forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da 
# distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS USADOS =
# DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida 
# e a quantidade de litros utilizada na viagem.

tempo = float(input("Quantas horas de viagem? "))
vel = float(input("Qual foi a velocidade média do carro durante a viagem em km/h? "))

distancia = tempo * vel
litros_usados = distancia / 12

print(f"\nVelocidade média = {round(vel, 2)} km/h")
print(f"Tempo gasto na viagem = {tempo} horas")
print(f"Distância percorrida = {round(distancia, 2)} km")
print(f"Quantidade de litros utilizada na viagem = {round(litros_usados, 2)} litros")