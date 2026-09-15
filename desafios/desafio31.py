print("| CONTADOR DE CARACTERES |")
print("-"*60)

digitado = input("Digite uma palavra/frase para ser contado: ")
caracteres = 0
separados = ""

for letra in digitado:
    if letra != " ":
        caracteres += 1
        separados += letra + " "

print(f"Caracteres: {separados}")
print(f"Número de Caracteres: {caracteres}")