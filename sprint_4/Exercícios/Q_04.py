def calcular_valor_maximo(operadores,operandos) -> float:

    resultados = map(lambda op: op[1][0] + op[1][1] if op[0] == '+' else
                                  op[1][0] - op[1][1] if op[0] == '-' else
                                  op[1][0] * op[1][1] if op[0] == '*' else
                                  op[1][0] / op[1][1] if op[0] == '/' else
                                  op[1][0] % op[1][1], zip(operadores, operandos))
    
    return max(resultados)

