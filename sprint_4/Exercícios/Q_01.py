# Resolucao Questao 1

with open('number.txt', 'r') as file:
    numbers = list(map(int, file.readlines())) 

pares = list(filter(lambda x: x % 2 == 0, numbers))

maiores_pares = sorted(pares, reverse=True)[:5]

soma_maiores_pares = sum(maiores_pares)

print(maiores_pares)
print(soma_maiores_pares)

