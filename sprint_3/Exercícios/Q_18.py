speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
lista = []
for x in speed.values():
    lista.append(x)
print(list(set(lista)))
