print("| CALCULADORA COMPLETA (V1) |")

operadores = ["+","-","/","*","//","**","%"]

num1 = float(input("Digite o Número 1: "))
num2 = float(input("Digite o Número 2: "))
op = input("Digite o operador: ")

if op in operadores:
    
    if num2 == 0 and op in ["/","//","%"]:
        print("ERRO! Não se pode dividir por zero!")
        resultado = "ERRO!"
    elif op == "+":
        resultado = num1+num2
    elif op == "-":
        resultado = num1-num2
    elif op == "/":
        resultado = num1/num2
    elif op == "//":
        resultado = num1//num2
    elif op == "%":
        resultado = num1%num2
    elif op == "*":
        resultado = num1*num2
    elif op == "**":
        resultado = num1**num2

    print(f"{num1} {op} {num2} = {resultado}")
else:
    print("Operador inexistente! O cálculo não será executado")