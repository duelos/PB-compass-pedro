arquivo = spark.read.text("README.md").rdd

palavras = arquivo.flatMap(lambda linha: linha[0].lower().split())

palavras = palavras.filter(lambda palavra: palavra.isalpha())

contagem_palavras = palavras.map(lambda palavra: (palavra, 1)).reduceByKey(lambda a, b: a + b)

resultados = contagem_palavras.collect()

for palavra, contagem in resultados:
    print(f"{palavra}: {contagem}")

