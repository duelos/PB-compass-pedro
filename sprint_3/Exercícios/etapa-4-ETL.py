with open('/home/pedro/pb-pedro-henrique/sprint_3/Exercícios/actors.csv', 'r') as arquivo:
    resultado = []
    for linha in arquivo:
        palavras = linha.rsplit(',', 5)
        resultado.append(palavras[:])

frequencia = []
numfrequencia = 0
nomefreq = 0
for c in resultado[1::]:
    frequencia.append(c[4])
    nomefreq = max(frequencia, key=frequencia.count)
    if c[4] == nomefreq:
        numfrequencia += 1

with open ('etapa_4.txt', 'w', encoding='utf-8') as text:
    text.write('O nome dos filmes mais frequentes e sua respectiva frequencia:')
    text.write('\nO nome do filme mais frequente é {} e sua frequência é {}.'.format(nomefreq, numfrequencia))