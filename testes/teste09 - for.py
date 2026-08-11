#Estruturas de Repetição
#São estruturas/controle de código que permite que um bloco de comandos possa ser repetido

#Repetição Contada (Quantidade Definida)

#FOR - Determina quandas X vezes o código será executado
#range(x) - Determina um intervalo de números(int) que o código será repetido
#i - variável que irá guardar o indice da contagem

#[0,1,2,3,4]
for i in range(5):
    print("Teste")
print("-- Fim da Repetição --")

#Utilizando a variável da repetição no contexto do código
for i in range(5):
    print(f"{i}")
print("-- Fim da Repetição --")

#Determinando em qual indice(numero) irá começar a repetição
#[1,2,3,4,5]
for i in range(1,6):
    print(f"{i}")
print("-- Fim da Repetição --")

#Determinando o intervalo/pulo entre cada índice
#[5,10,15,20,25]
for i in range(5,26,5):
    print(f"{i}")
print("-- Fim da Repetição --")