print("| EXIBINDO CARDAPIO |")
print("-"*60)

cardapio = ["Arroz","Feijão","Macarrão","Hercules","Mostarda","Comida","Helmans Ketchup"]

print("--- CARDAPIO ---")
for prato in cardapio:
    print(f">> {prato}")
print("-"*60)

escolha = input("Digite o prato que deseja comprar: ")
if escolha in cardapio:
    print(f"Aproveite o {escolha}!")
else:
    print("Não existe esse prato")