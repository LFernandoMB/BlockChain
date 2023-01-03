from cripto import criptografia

if __name__ == '__main__':
    num = 1
    hash_anterior = '0'

    while True:
        print('=' * 70)
        print(f'{"TREINANDO BLOCKCHAIN - L.FERNANDO":^70}')
        print('=' * 70)
        info = input('* Digite a informação a ser criptografada: ')
        with open('Blockchain.txt', 'r+') as file:
            bloco = str(len(file.readlines()) + 1)
        blockchain: str = criptografia(bloco, info, hash_anterior)
        hash_anterior = bloco
        print('=' * 70)
        print(f'{"BLOCO GERADO":^67} {num}')
        num += 1
        print('=' * 70)
        print(f'{blockchain:^70}')
        print('=' * 70)
        print()

        with open('Blockchain.txt', 'a+') as file:
            file.write(
                f'Bloco: {bloco} - Info Criptografada: {info} - Registro: {blockchain}\n')
        sair = input('Deseja inserir novo bloco? [S/N]: ').upper().strip()
        if sair == 'N':
            break
