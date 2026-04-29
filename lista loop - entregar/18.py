soma = 0
num = 0
try:
    while num < 100:
        numero = int(input(f'Digite um número impár e multiplo de sete: '))

        if numero % 2 != 0 and numero % 7 == 0:
            soma = soma + numero
            num + num + 1
        else:
            print('Número inválido. Ele deve ser ímpar e múltiplo de sete.')

    media = soma / 100
    print(f'\nA média dos 100 números lidos é: {media}')
    
except Exception as ERRO_EXECAO:
    print(f'ERRO: {ERRO_EXECAO}')
