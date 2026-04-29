while True:
        try:
            numero = int(input('Digite o número de X: '))

            
            if 10 <= numero and numero <= 90 and numero % 6 == 0:
                soma = soma + numero