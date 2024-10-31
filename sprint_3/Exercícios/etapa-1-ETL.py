with open('/home/pedro/pb-pedro-henrique/sprint_3/Exercícios/actors.csv','r') as arquivo:
    resultado = []
    for linha in arquivo:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

qntfilmes = []
for c in resultado[1::]:
    qntfilmes.append(c[2])
    maior = max(qntfilmes)
    if c[2] == maior:
        ator = c[0]
print(f'Nome do Ator: {ator}, Quantidade de filmes: {maior}')

with open ('./etapa_1.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade:')
    text.write('\nAtor com mais filmes: {}, quantidade filmes: {}.'.format(ator, maior))
    text.close() 
