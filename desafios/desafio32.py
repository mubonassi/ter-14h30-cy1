import random

print("| Senha Numérica |")
print("-"*60)

senha = random.randint(1,100)
erros = 0
tentativa = 0

print("Adivinha a Senha Abaixo (0 para desistir)")
while tentativa != senha:
    tentativa = int(input("Digite a tentativa de senha (1 a 100): "))

    if tentativa == 0:
        print("VOCÊ DESISTIU, SEU RUIM!")
        print(f"A senha era: {senha}")
        break
    elif tentativa != senha:
        print("ERROU! Tente novamente!")
        erros += 1
        if tentativa > senha:
            print("Você chutou a mais!")
        else:
            print("Você chutou a menos!")
    else:
        print("VOCÊ ACERTOU!")
        print(f"E errou {erros} vezes")