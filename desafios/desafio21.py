print("| SORVETERIA |")

sabores = ["Chocolate","Flocos","Napolitano","Morango","Abacaxi"]
coberturas = ["MMs","Chocolate Branco","Fini","Açai","Eeeeeeeeee","Banana"]

print("-- Sabores --")
print(sabores)
print("-- Coberturas --")
print(coberturas)
print("-- Escolha o sabor do sorvete --")
sabor = input("Digite aqui o nome do sabor: ")

if sabor in sabores:
    cobertura = input("Digite aqui o nome da cobertura: ")
    if cobertura in coberturas:
        print(f"Pedido completo: Sorvete de {sabor} com cobertura de {cobertura}")
    else:
        print("Cobertura inválida! Sorvete ficará sem cobertura!")
        print(f"Pedido completo: Sorvete de {sabor}")
else:
    print("Ficou sem sorvete")