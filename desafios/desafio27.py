print("| PERSONALIZANDO A REPETIÇÃO |")

inicio = int(input("Digite o Nº inicial: "))
fim = int(input("Digite o Nº final: "))
pulo = int(input("Digite o intervalo entre cada: "))

for i in range(inicio,fim+1,pulo):
    print(i)