def calculo_funcionario():
   
    nome = input("Digite o nome do funcionário: ")
    horas = float(input("Digite o número de horas trabalhadas: "))
    valor_hora = float(input("Digite o valor que recebe por hora: "))

    salario = horas * valor_hora

    print(f"SALÁRIO = Reais {salario:.2f}")
