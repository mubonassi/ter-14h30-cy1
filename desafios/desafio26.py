print("|SISTEMA DE TABUADA|")
print("-"*60)

tabuada = int(input("Digite o valor que queira realizar a tabuada: "))
print("-"*60)

for i in range(1,11):
    res = tabuada * i
    print(f"{tabuada} x {i} = {res}")