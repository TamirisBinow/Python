total = 0 
dias = 0
try:
    while True:
    
        temp = float(input('Digite a temperatura de hoje: '))
        if temp < 28:
            break
        else:
            total = total + temp 
            dias = dias + 1
            
        media = total/dias
    print(f'A média é da estação é: {media:.0f}° ')
    
except Exception as ERRO_EXCECAO:
    print(f'Erro Exceção: {ERRO_EXCECAO}')
    
            
            
        