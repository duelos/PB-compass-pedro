class Aviao:
    cor = "Azul"  

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

    def __str__(self):
        return (f'O avião de modelo "{self.modelo}" possui uma velocidade máxima de '
                f'"{self.velocidade_maxima}", capacidade para "{self.capacidade}" '
                f'passageiros e é da cor "{self.cor}".')

avioes = [
    Aviao("BOIENG456", "1500 km/h", 400),
    Aviao("Embraer Praetor 600", "863 km/h", 14),
    Aviao("Antonov An-2", "258 km/h", 12)
]

for aviao in avioes:
    print(aviao)
