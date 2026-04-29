
somatemp = 0
ndias = 0

while True:
    try:
        temp = float(input(f'Digite a temperatura do dia: '))
        
        if -15 <= temp <= 5:

            somatemp = somatemp + temp
            ndias = ndias + 1
        else:
            print(f'A temperatura está fora do intervalo de inverno.')
            break 
    except Exception as ERRO_EXCECAO:
        print(f'ERRO: {ERRO_EXCECAO}')

if ndias > 0:

    media = somatemp / ndias
    
    print(f"A temperatura média da estação foi de: {media:.2f}°C")
else:
    print("Nenhuma temperatura de inverno foi inserida para calcular a média.")