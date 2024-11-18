import hashlib

print('Digite seu texto("sair" para finalizar):')
while True:
    msg = input('Texto: ')
    if msg.lower() == "sair":
        print("FINALIZANDO")
        break
    hash = hashlib.sha1(msg.encode()).hexdigest()
    print(f'Hash string: {hash}')