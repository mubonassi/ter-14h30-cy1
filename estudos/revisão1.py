#Revisão
#Comandos Básicos

#Print
print("Isso é um texto de teste")
#Variável
palavra = "Ornitorrinco"
#Exibindo variável no print
print(f"Palavra escolhida foi {palavra}")
#Calculando na variável
num1 = 345
num2 = 876
res = num1 * num2
print(f"{num1}*{num2} = {res}")
#Input
algo = input("Digite alguma coisa: ")
print(f"Você digitou {algo}")

#Estruturas de Condição
resposta = True
if resposta == True:
    print("A resposta foi verdadeira")
else:
    print("A resposta foi falsa")
 
nome = "Paulo"
if nome == "Fernando":
    print("Seu nome é fernando")
else:
    print("Seu nome não é fernando")

valor = -10
if valor > 0:
    print("O valor é positivo")
elif valor == 0:
    print("O valor é neutro")
else:
    print("O valor é negativo")