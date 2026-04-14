print("| BAR DO ZÉ |")
print("-"*30)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"Você poderá entrar, {nome}! Seja bem vindo!")
else:
    print(f"SAIA DAQUI, {nome}!")