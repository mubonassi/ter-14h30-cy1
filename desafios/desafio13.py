print("| POSTO DE PYTHONLINA! |")

tanque = float(input("Digite o quanto está sobrando no tanque: "))
combustivel = float(input("Digite o quanto deseja encher no tanque: "))

if combustivel <= tanque:
    sobrou = tanque - combustivel
    print("Você encheu o tanque com sucesso!")
    if sobrou > 0:
        print(f"Sobrou no seu tanque: {sobrou}L")
else:
    passou = combustivel - tanque
    print("Você ultrapassou o limite do tanque! Tente novamente!")
    print(f"Passado do tanque: {passou}L")