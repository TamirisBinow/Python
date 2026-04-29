try:
    n = int(input('Digite o valor de n: '))

    linferior = int(input('Digite o Limite Inferior: '))
    lsuperior = int(input('Digite o Limite Superior: '))

    if n >= 2 and lsuperior >= linferior:
        print(f'Múltiplos de {n} no intervalo [{linferior}, {lsuperior}]:')
        
        num = linferior
        while num <= lsuperior:
            if num % n == 0:
                print(num)
            num = num + 1
    else:
        print("Valores inválidos! Verifique as condições.")
        
except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')