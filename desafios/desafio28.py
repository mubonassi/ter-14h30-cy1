print("| PARES E IMPARES |")
print("-"*60)

valor = int(input("Digite o número em sequência que será exibidos os pares e impares: "))

print("| PARES |")
pares = ""
for i in range(2,valor+1,2):
    pares = pares + f"{i} "
print(pares)

impares = ""
print("| IMPARES |")
for i in range(1,valor+1,2):
    impares += f"{i} "
print(impares)