with open('/home/pedro/pb-pedro-henrique/sprint_3/Exercícios/actors.csv', 'r') as arquivo:
    resultado = []
    for linha in arquivo:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])
valores = []

for c in resultado[1::]:
    valores.append(c[5])

total_gross = sum(float(value) for value in valores)
media_gross = total_gross / len(valores)

with open ('etapa_2.txt', 'w', encoding='utf-8') as text:
    text.write('apresente a media de receita de bilheteria bruta dos principais filmes, considerando todos os autores: \n')
    text.write(f'A média de receita bruta dos principais filmes é: {media_gross:.2f}')