mix1 = 0
mix2 = 0 
mix3 = 0
pessoas = 0 

try :

    print('VOTAÇÃO\n Digite:\n MIX 1 = 1\n MIX 2 = 2\n MIX 3 = 3\n ')
    while True:
        voto = int (input('VOTO: '))
        
        if voto == 0:
            break
        elif voto == 1:
            mix1 = mix1 + 1
            pessoas = pessoas + 1 
        elif voto == 2:
            mix2 = mix2 + 1
            pessoas = pessoas + 1 
        elif voto == 3:
            mix3 = mix3 + 1
            pessoas = pessoas + 1 
        else:
            print('Digite um número válido')
        
except Exception as ERRO_EXCECAO:
        print(f'Erro exceção: {ERRO_EXCECAO}')
        
porcentagem1 = (mix1/pessoas) * 100
porcentagem2 = (mix2/pessoas) * 100
porcentagem3 = (mix3/pessoas) * 100

print(f'A porcentagem de clientes que preferem o mix 1 é: {porcentagem1:.2f}')
print(f'A porcentagem de clientes que preferem o mix 2 é: {porcentagem2:.2f}')
print(f'A porcentagem de clientes que preferem o mix 3 é: {porcentagem3:.2f}')

    