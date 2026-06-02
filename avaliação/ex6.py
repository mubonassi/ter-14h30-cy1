minutos = int(input("Digite quantos minutos se passaram: "))
horas = minutos/60
dias = horas/24

print(f"Minutos: {minutos} | Horas: {horas} | Dias: {dias}")

if dias > 1:
    print(f"Se passaram {dias} dias!")
elif dias == 1:
    print("Se passou 1 dia")
else:
    print("Não se passou 1 dia inteiro!")