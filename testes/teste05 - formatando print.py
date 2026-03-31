#Formatação e Manipulação de String/Print
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

resultado = numero1/numero2

print(f"{numero1}/{numero2} = {resultado} <---- Sem formatação")

#Funções do Print

#Limitando as casas decimais do float NO PRINT
# :.0f
#Obs: Necessita ser usado no 'f' do print
print(f"{numero1}/{numero2} = {resultado:.2f} <---- Com formatação")

#Manipulação de texto/string
palavra = input("Digite uma palavra aleatória: ")
frase = input("Digite uma frase aleatória: ")

#Função upper() -> Deixa tudo maiusculo
print(palavra.upper())

#Função lower() -> Deixa tudo minusculo
print(palavra.lower())

#Função capitalize() -> Deixa a primeira letra da string maiuscula
print(frase.capitalize())

#Função title() -> Deixa a primeira letra de cada palavra da string maiuscula
print(frase.title())