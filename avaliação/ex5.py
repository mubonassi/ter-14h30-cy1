dinheiro = float(input("Digite o quanto de R$ você tem: "))
qtd_litros = float(input("Digite a quantidade de L enchidos: "))
valor_litro = float(input("Digite o valor em R$ do litro: "))

total = valor_litro * qtd_litros

print(f"Valor Total: {total}")

if dinheiro >= total:
    print("Foi pago com sucesso!")
else:
    print("Dinheiro insuficiente!")