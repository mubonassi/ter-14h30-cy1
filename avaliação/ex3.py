base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = (base**2 + altura**2) ** 0.5
diferenca = base - altura

print("- Retangulo -")
print(f"-- Area: {area}cm")
print(f"-- Diagonal: {diagonal}cm")
print(f"-- Perimetro: {perimetro}cm")
print(f"-- Diferença: {diferenca}cm")
