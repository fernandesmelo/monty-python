# 2ª QUESTÃO
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma 
# mensagem de erro e voltando a pedir as informações.

usuario = input("Usuário: ")
senha = input("Senha: ")

while usuario == senha:
    print("Senha inválida. Tente novamente outra senha.")
    senha = input("Senha: ")

print(f"Olá, {usuario}. Seja bem-vindo(a)!")

