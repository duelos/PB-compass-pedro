import random
import csv
import names
import time
import os

nums =  [random.randrange(250) for x in range(250)]
nums.reverse
print(nums)

animais = ['Leão', 'Elefante', 'Golfinho','Canguru', 'Cavalo', 'Jacaré', 'Lobo', 'Panda', 'Gato', 'Tartaruga', 'Camaleão', 'Falcão', 'Urso', 'Tamanduá', 'Arraia', 'Lontra', 'Porco-espinho', 'Flamingo', 'Coala', 'Rena']
animais.sort
for x in animais:
    print(x)

arquivo_csv = "animais.csv"

with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for animal in animais:
        writer.writerow([animal])

random.seed(40)

nomes_unicos = 3000

nomes_aleatorios = 10000000

aux = []

for i in range(0, nomes_unicos):
    aux.append(names.get_full_name())
print(f"Gerando {nomes_aleatorios} nomes aleatorios")

dados = []

for i in range(0, nomes_aleatorios):
    dados.append(random.choice(aux))

with open('nomes_aleatorios.txt', 'w') as arquivo:
    for nome in dados:
        arquivo.write(nome + '\n')