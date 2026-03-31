print("> AUMENTO DE 10%")
print("-"*30)

valor = float(input("Digite um valor: "))

#Método 1 - Utilizando uma segunda variável
acrescimo = valor + (valor/10) #1
acrescimo = valor * 1.10 #2 -> Melhor forma

print(f"O acréscimo de 10% do valor {valor} deu {acrescimo}")

#Método 2 - Alterando/Atualizando a Variável
valor = valor * 1.10