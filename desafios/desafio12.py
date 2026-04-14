print("| VERIFICADOR DE SENHA |")

senha = "abcd1234"
tentativa = input("Digite a tentativa de senha: ")

if tentativa == senha:
    print("Você acertou!")
else:
    print("Você errou!")