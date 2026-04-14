#Estruturas de Condição -> Criam condições para que um bloco de código seja executado
#Um comando só irá acontecer se determinada condição retornar verdadeira
#Condição => Ação

#Ex: Se o número digitado pelo usuário for X acontecerá a mensagem "você digitou o número X"
numero = int(input("Digite um número para ser verificado: "))

#se (condição) então: {ação}
#senão então: {ação}

if numero == 17:
    print("Você digitou o número 17!")
else:
    print("Você NÃO digitou o número 17!")

#Comparadores
# == -> Igual a (valor == valor)
# > -> Maior que (valor > valor)
# < -> Menor que (valor < valor)
# >= -> Maior ou igual a (valor >= valor)
# <= -> Menor ou igual a (valor <= valor)
# != -> Diferente de (valor != valor)