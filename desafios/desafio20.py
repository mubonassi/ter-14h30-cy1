print("| CONFIRMANDO PRESENÇA EM SALA DE AULA |")
print("-"*40)

alunos = ["Clara","Nico","Antonio","Henrique","Murilo","Mauri","Patricia","Bob","Caiu"]
print(f"Lista de Alunos: {alunos}")

escolha = int(input("Digite o indice do aluno para confirmar a presença: "))
alunos[escolha] = alunos[escolha] + " - CONFIRMADO"

print(f"Lista atualizada: {alunos}")