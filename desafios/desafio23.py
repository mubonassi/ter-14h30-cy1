print("| CARDÁPIO RESTAURANTE |")
print("-"*60)

pratos = ["Hamburger","Frango","Sorvete"]
precos = [10.99,30.85,6.99]

print("-- CARDAPIO --")
print(pratos)
print("-"*60)

pedido = int(input("Digite o prato desejado (indice): "))

if pedido <= 2:
    print(f"{pratos[pedido]} - {precos[pedido]}")
    print("Deseja finalizar o pedido?")
    escolha = input("Digite aqui (sim/não): ")
    if escolha == "sim":
        print(f"Pedido finalizado com sucesso!")
    else:
        print(f"Pedido de {pratos[pedido]} foi cancelado!")
else:
    print("Prato não existe!")