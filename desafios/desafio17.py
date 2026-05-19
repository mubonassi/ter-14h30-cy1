print("| SISTEMA DE PONTUAÇÃO |")
print("-"*30)

pontos = int(input("Digite aqui sua pontuação total: "))

#método 1
#if pontos >= 0 and pontos <= 199:
#    print("Rank: Iniciante")

#método 2
if pontos >= 1000:
    print("Rank: Lendário")
elif pontos >= 700:
    print("Rank: Mestre")
elif pontos >= 500:
    print("Rank: Campeão")
elif pontos >= 200:
    print("Rank: Veterano")
elif pontos >= 0:
    print("Rank: Iniciante")
else:
    print("RANK INVÁLIDO!")