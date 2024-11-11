import csv

def processar_notas(arquivo_csv):
    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file)
        
        estudantes = []
        
        for linha in reader:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            
            tres_maiores_notas = sorted(notas, reverse=True)[:3]
            
            media = round(sum(tres_maiores_notas) / 3, 2)
            
            estudantes.append({'nome': nome, 'notas': tres_maiores_notas, 'media': media})
        
        estudantes = sorted(estudantes, key=lambda x: x['nome'])
        
        for estudante in estudantes:
            try:
                if estudante['media'] == int(estudante['media']):
                    print(f"Nome: {estudante['nome']} Notas: {estudante['notas']} Média: {estudante['media']:.1f}")
                else:
                    print(f"Nome: {estudante['nome']} Notas: {estudante['notas']} Média: {estudante['media']:.2f}")
            except Exception as e:
                print(f"Erro ao formatar a média: {e}")

processar_notas('estudantes.csv')

