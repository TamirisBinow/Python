try:
    empregados = 0
    desempregados = 0
    pessoas = 0
    total_habitantes = 10000
    
    while pessoas < total_habitantes:
        resposta = input(f'Pessoa você está empregado no momento? (sim/nao): ')
            
        if resposta == 'sim':
            empregados = empregados + 1
            pessoas = pessoas + 1
        elif resposta == 'nao':
            desempregados = desempregados + 1
            pessoas = pessoas + 1
        else:
            print('Entrada inválida. Por favor, digite "sim" ou "nao".')

    porcempregados = (empregados / total_habitantes) * 100
    porcdesempregados = (desempregados / total_habitantes) * 100
    
    print(f'Total de pessoas empregadas: {empregados:.2f}')
    print(f'Total de pessoas desempregadas: {desempregados:.2f}')
    print(f'Porcentagem de empregados: {porcempregados:.2f}%')
    print(f'Porcentagem de desempregados: {porcdesempregados:.2f}%')

except Exception as ERRO_EXCECAO:
    print(f'Erro: {ERRO_EXCECAO}')