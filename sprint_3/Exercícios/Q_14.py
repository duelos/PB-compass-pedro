def funcao (*argumentos, **argumentos_nomeados):
    for arg in argumentos:
        print(arg)
    for x in argumentos_nomeados.values():
        print(f'{x}')

funcao (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)