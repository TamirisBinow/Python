vip = 0
standard = 0
tclientes = 0

try:
    while True:
        print('1 - Cadastrar Cliente')
        print('0 - Sair do Programa')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            salario = float(input('Digite o salário do cliente: '))
            tclientes = tclientes + 1
            
            if salario >= 5000:
                vip = vip + 1
            else:
                standard = standard + 1
        
        elif opcao == '0':
            break
        else:
            print('Opção inválida! Tente novamente.')

    percvip = (vip / tclientes) * 100
    percstandard = (standard / tclientes) * 100
        
    print(f'Total de clientes: {tclientes:.2f}')
    print(f'clientes vip({percvip:.2f}%)')
    print(f'clientes standard({percstandard:.2f}%)')
    
except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')
