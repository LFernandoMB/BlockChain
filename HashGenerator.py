from hashlib import sha256


def criptografia(block: int = 0, information: str = '', last_hash: int = 0):
    return sha256((block + information + last_hash).encode('ascii')).hexdigest()


num = 1
hash_anterior = '0'

while True:
    print('=' * 70)
    print(f'{"TREINANDO BLOCKCHAIN - L.FERNANDO":^70}')
    print('=' * 70)
    bloco = input('* Digite o número do bloco: ')
    info = input('* Digite a informação a ser criptografada: ')
    blockchain: str = criptografia(bloco, info, hash_anterior)
    hash_anterior = bloco
    print('=' * 70)
    print(f'{"BLOCO GERADO":^67} {num}')
    num += 1
    print('=' * 70)
    print(f'{blockchain:^70}')
    print('=' * 70)
    print()
    sair = input('Deseja inserir novo bloco? [S/N]: ').upper().strip()
    if sair == 'N':
        break
