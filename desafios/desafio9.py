print("> CONTA BANCÁRIA!")
print("-"*30)
valorConta = float(input("Digite o valor que possui na conta: R$"))
porcentagemAumento = float(input("Digite a porcentagem de aumento: %"))

valorConta = valorConta * (porcentagemAumento/100 + 1)

print(f"Valor final da conta: R${valorConta}")