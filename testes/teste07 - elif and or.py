#Estrutura de Condição ENCADEADA e COMPOSTA
numero = int(input("Digite um número: "))

#IF Composto (AND e OR) -> Trabalhando com múltiplas condições
#OR (ou) -> Uma das condições necessitam ser verdadeiras
if numero == 6 or numero == 9:
    print("Você digitou O NÚMERO EXTRA MÁGICO!!!!!111111")
else:
    print("Pena, não digitou um dos números mágicos")

#AND (e) -> TODAS as condições necessitam ser verdadeiras
if numero > 0 and numero < 10:
    print("Você digitou um número maior que zero e menor que dez")
else:
    print("Você não digitou um número maior que zero e menor que dez")

#IF Encadeado -> Trabalhando com múltiplas perguntas
#elif -> Uma condição/pergunta caso a anterior tenha sido negativa
if numero == 5:
    print("Você abriu o 5, os portais do inferno");
elif numero == 7:
    print("Você abriu o 7, você tropeçou na lava do vulcão");
elif numero == 0:
    print("Você abriu o 0, foi pro submundo");
else:
    print("Você tá seguro");