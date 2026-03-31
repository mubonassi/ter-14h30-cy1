print("> Calculo dos Produtos!")
print("-"*30)

produto1 = float(input("Digite o valor do 1º produto: "))
produto2 = float(input("Digite o valor do 2º produto: "))
produto3 = float(input("Digite o valor do 3º produto: "))

valorTotal = produto1 + produto2 + produto3

valorDebito = valorTotal
valorVista = valorTotal * (1 - 0.051)
valorCredito = valorTotal * 1.0375

print(f"Valor Total: R${valorTotal}")
print(">> Formas de Pagamento <<")
print(f"À Vista (dinheiro): R${valorVista}")
print(f"Crédito: R${valorCredito}")
print(f"Débito: R${valorDebito}")