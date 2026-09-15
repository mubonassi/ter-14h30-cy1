import random
print("| PERSONALIZADOR DE DADOS |")
print("-"*60)

lados = int(input("Digite a quantidade de lados do seu dado: "))

while True:
    dado = random.randint(1,lados)
    print(f"D{lados}: {dado}")

    continuar = input("Aperte enter ou digite 'sair' para encerrar... ")
    if continuar == "sair":
        break