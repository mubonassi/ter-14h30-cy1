print("| FESTA DO TRABALHO |")

funcionarios = ["Nico","Antonio","Henrique","Clara","Murilo","Matheus","Tunico","Fernando","Mauri","Pat","Felipe","Luciana","Arcade da Sala","Xbox","T-Rex","Leo","Bob","Andrew"]
banidos = ["Nico","Xbox","Fernando","Henrique","Bob"]

nome = input("Digite o seu nome: ").capitalize()

if nome in funcionarios:
    if nome not in banidos:
        print(f"Seja bem vindo, {nome}!")
    else:
        print(f"Saia daqui, {nome}, você esqueceu o que você fez naquela noite do dia 23 de maio, de 2024, às 20h33, na sala de funcionários, com o faxineiro e uma cabra chinesa?")
else:
    print(f"{nome} você não é funcionário.")