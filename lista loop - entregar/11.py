print('mostrar 50 números subsequentes a um número informado')
try:
    numero = int(input('Digite um número inteiro: '))

    print(f'Os 50 números subsequentes são:\n')
    for i in range(1, 51):
        print(numero + i)
        
except Exception as ERRO_EXCECAO:
    print(f'ERRO:{ERRO_EXCECAO}')
