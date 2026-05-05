print("| TREVISTA DE'MPREGO |")

print("Resposta as perguntas com 'sim' ou 'não'!")
print("Você veio para a entrevista?")
resposta = input("Digite aqui: ")

if resposta == "sim":
    print("Showleza, podemos continuar")
    print("Você trouxe o currículo?")
    resposta = input("Digite aqui: ")
    if resposta == "sim":
        print("Beleshow, agora podemos iniciar")
        print("Mas pera ai, você tem experiência na area de limpeza de sofás?")
        resposta = input("Digite aqui: ")
        if resposta == "sim":
            print("Agora sim, vamos iniciar de verdade")
        else:
            print("Precisa limpar mais sofás para trabalhar aqui")
    else:
        print("VAI LÁ PEGAR O CURRICULO CARAMBA!!!!!!!")
else:
    print("Por que veio aqui, então?")