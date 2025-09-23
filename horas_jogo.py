def hora_do_jogo():
    hora_inicial = int(input("Digite a hora inicial (0-23): "))
    hora_final = int(input("Digte a hora final (0-23): "))

    if hora_final > hora_inicial:
        duracao = hora_final - hora_inicial
    elif hora_final <  hora_inicial:
        duracao = (24 - hora_inicial) + hora_final
    else:
        duracao = 24
    print(f"O JOGO DUROU {duracao} HORA(S)")            