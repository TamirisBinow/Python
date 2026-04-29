
print('Urna de votação')

qvotos = 0 
A = 0
B = 0
C = 0

try:
    while qvotos < 50:
        print('MENU DE OPÇÕES\n 1 - Candidato A\n 2 - Candidato B\n 0 - Nulo ou inválido ')
        voto = int (input('Digite seu voto aqui: '))
        if voto == 1:
            qvotos = qvotos + 1
            A = A + 1
        elif voto == 2:
            qvotos = qvotos + 1
            B = B + 1
        elif voto == 0:
            qvotos = qvotos + 1
            C = C + 1
        else:
            print('Digite uma das opções do menu')
            
    resultadoa = (A / qvotos) * 100
    resultadob = (B / qvotos) * 100
    resultadoc = (C / qvotos) * 100
    
    print(f'Candidato 1: {resultadoa:.0f}%')
    print(f'Candidato 2: {resultadob:.0f}%')
    print(f'Nulos ou Inválidos: {resultadoc:.0f}%')
    
except Exception as ERRO_EXCEXAO:
    print(f'Erro: {ERRO_EXCEXAO}')
    
    
            