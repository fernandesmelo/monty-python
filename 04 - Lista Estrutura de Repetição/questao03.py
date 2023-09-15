# 3ª QUESTÃO
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = ""
idade = -1
salario = -1
sexo = ""
estado_civil = ""

while len(nome) <= 3:
    nome = input("Informe seu nome: ")
    if len(nome) <= 3:
        print("O nome precisa ter mais de 3 caracteres. Tente novamente.")

while idade < 0 or idade > 150:
    idade = int(input("Informe sua idade: "))
    if idade < 0 or idade > 150:
        print("Idade precisa estar entre 0 e 150 anos. Tente novamente.")

while salario < 0:
    salario = float(input("Informe seu salário: R$"))
    if salario < 0:
        print("O salário precisa ser maior que R$0. Tente novamente.")

while sexo != "f" and sexo != "m":
    sexo = input("Informe seu sexo. [M] Masculino ou [F] Feminino? ")
    if sexo != "m" and sexo != "f":
        print("Sexo inválido. Tente novamente.")

while estado_civil not in ["s", "c", "v", "d"]:
    estado_civil = input("Informe seu estado civil - [C] Casado(a), [S] Solteiro(a), [V] Viúvo(a) ou [D] Divorciado(a): ")
    if estado_civil not in ["s", "c", "v", "d"]:
        print("Opção inválida. Tente novamente.")

# Corrigir atribuições
if sexo == "m":
    sexo = "Masculino"
elif sexo == "f":
    sexo = "Feminino"

if estado_civil == "s":
    estado_civil = "Solteiro(a)"
elif estado_civil == 'c':
    estado_civil = "Casado(a)"
elif estado_civil == "v":
    estado_civil = "Viúvo(a)"
elif estado_civil == "d":
    estado_civil = "Divorciado(a)"

print(f'''\nNome: {nome}
Idade: {idade} anos
Salário: R${salario}
Sexo: {sexo}
Estado Civil: {estado_civil}''')
