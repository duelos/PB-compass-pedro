def funcao(string):
    numeros = string.split(",")  
    soma = 0
    for num in numeros:
        soma += int(num)  
    return soma

soma = funcao("1,3,4,6,10,76")
print(soma) 