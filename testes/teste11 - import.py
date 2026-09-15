#Import - Permite importar funções internas da biblioteca de códigos do Python

#import biblioteca -> puxa as funções especificas
#random -> biblioteca de funções que geram valores aleatórios
import random as rdm

valor = rdm.randint(1,100)
print(f"Valor gerado: {valor}")

lista = ["a","b","c","d","e"]
item = rdm.choice(lista)
print(f"Item gerado: {item}")