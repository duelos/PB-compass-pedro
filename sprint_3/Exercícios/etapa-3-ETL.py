with open('/home/pedro/pb-pedro-henrique/sprint_3/Exercícios/actors.csv', 'r') as arquivo:
    resultado = []
    for linha in arquivo:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

maiorfaturamento = []
faturaator = 0
for c in resultado[1::]:
    maiorfaturamento.append(float(c[3]))
    maximo = max(maiorfaturamento)
    if float(c[3]) >= maximo:
        faturaator = c[0]

with open ('etapa_3.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior média de faturamento por filmes:')
    text.write('\nAtor/atriz com a maior média de faturamento por filme é {} com média {}.'.format(faturaator, maximo))