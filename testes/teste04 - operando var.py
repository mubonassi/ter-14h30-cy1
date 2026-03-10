#Operando com Variaveis
#Operando com String
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print(f"Seu nome completo é {nomeCompleto}")

#Operando com Numeros
#Para receber numeros, necessita converter/traduzir o valor
#Ex: int(valor) / float(valor)
numero1 = int(input("Digite o 1o numero: "))
numero2 = int(input("Digite o 2o numero: "))
resultado = numero1+numero2
print(f"{numero1} + {numero2} = {resultado}")