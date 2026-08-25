print("| SOMANDO OS NÚMEROS |")
print("-"*50)

valor = int(input("Digite o valor para ser calculado em sequência: "))

resultado = 0
conta = ""
for numero in range(1,valor+1):
    resultado += numero
    conta += f"{numero}"
    if numero < valor:
        conta += " + "

print(f"{conta} = {resultado}")

#1+2+3+4+5 = 15