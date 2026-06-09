print("| LISTA DE PRODUTOS |")
print("-"*40)

produtos = ["Xbox","PSX","Suco de Laranja","Antonio","Cadeira","Cadeira 2"]

print("Escolha um dos produtos: ")
print(produtos)

escolha = int(input("Digite o indice do produto: "))

print(f"Você escolheu o produto: {produtos[escolha]}")