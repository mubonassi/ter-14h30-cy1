print("| ADIVINHAR SENHA MULTIPLAYER |")

senha = int(input("Digite a senha: "))
tentativa = int(input("Digite a tentativa: "))

if tentativa == senha:
    print("TU ACERTASTES!!!!!!!!!!!1111")
else:
    print("TU ERRASTESSSSSSSSXXXX!!!!!!!!111")
    if tentativa > senha:
        print("Você tentou um numero MIÓ!")
    else:
        print("Você tentou um número MINÓ!")