def maiores_que_media(conteudo:dict)->list:

    media = sum(conteudo.values()) / len(conteudo)
    
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    
    produtos_acima_media.sort(key=lambda x: x[1])
    
    return produtos_acima_media

