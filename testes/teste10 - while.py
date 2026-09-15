#While - Repetição Condicionada
#Repete enquanto a condição for verdadeira
#Isso mistura repetição com condição (if)

#Enquanto o número for igual a 0, o bloco irá se repetir
numero = 0
while numero == 0:
    numero = int(input("Digite um número: "))

#While True -> Repetição INDEFINIDA -> Loop infinito
#break -> palavra chave que encerra uma repetição
while True:
    palavra = input("Escreva 'sair': ")
    if palavra == "sair":
        break