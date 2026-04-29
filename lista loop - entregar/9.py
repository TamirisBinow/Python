soma = 0

while True:
        try:
            numero = int(input('Digite um número (entre 10 e 90): '))
        
            if numero == 0:
                break
            
            if 10 >= numero and numero <= 90 and numero % 5 == 2:
                soma = soma + numero
            else:

                print('Este número não atende aos critérios. Tente outro.')
        
        except Exception as ERRO_EXCECAO:
            print(f'Ocorreu um erro inesperado: {ERRO_EXCECAO}')
            break

print(f'A soma final dos números válidos é: {soma}')