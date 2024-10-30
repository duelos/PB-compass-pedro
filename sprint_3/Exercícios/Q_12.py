def my_map(list, f):
    lista = []
    for n in list:
        resultado = f(n)
        lista.append(resultado)
    print(lista)
def potencia (n):
    return n**2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_map(lista,potencia)
