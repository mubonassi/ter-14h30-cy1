#Coleção/Lista de Valores - Array
#É um tipo de variavel que guarda uma lista de valores

#Cria e exibe uma lista (ARRAY)
lista = ["abc",123,1.6,True,2+2]
print(lista)

#Exibindo um item especifico da lista
print(lista[0])
print(f"Item #4: {lista[3]}")

#Alterando valor da lista
lista[2] = "mudou valor"
print(lista)

valor1 = "abc"
valor2 = "bca"

#Verificando um item da lista
#in - not in
if valor1 in lista:
    print(f"{valor1} está na lista!")

if valor2 not in lista:
    print(f"{valor2} NÃO está na lista")