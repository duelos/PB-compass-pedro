primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
for indice,nome in enumerate(primeirosNomes):
    print(f'{indice} - {nome} {sobreNomes[indice]} está com {idades[indice]} anos')