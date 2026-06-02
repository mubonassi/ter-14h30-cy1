hrs_trabalhadas = int(input("Digite as horas trabalhadas: "))
tarefas_realizadas = int(input("Digite a qtd de tarefas realizadas: "))

if hrs_trabalhadas >= 5 or tarefas_realizadas >= 4:
    print("Você fez o necessário para finalizar o dia!")
else:
    print("Você não fez o necessário para finalizar o dia!")