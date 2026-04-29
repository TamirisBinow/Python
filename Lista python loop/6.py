pessoas = 0
quantidade = 100
a = 0
b = 0
c = 0 

while pessoas < quantidade:
    try:
        salario = float(input(f'Digite o seu salário: '))
        
        if salario >= 14970.75:
            a = a + 1 
        elif salario >= 4990.25:
            b = b + 1 
        else: 
            c = c + 1 
        
        pessoas = pessoas + 1 
        
    except Exception as ERRO_EXCECAO:
          print(f'Erro exceção: {ERRO_EXCECAO}')
        


porcentagemA = (a / quantidade) * 100
porcentagemB = (b / quantidade) * 100
porcentagemC = (c / quantidade) * 100

print(f'A porcentagem do grupo que recebe 15 salários mínimos ou mais é: {porcentagemA:.2f}%')
print(f'A porcentagem do grupo que recebe de 5 a menos de 15 salários mínimos é: {porcentagemB:.2f}%')
print(f'A porcentagem do grupo que recebe menos de 5 salários mínimos é: {porcentagemC:.2f}%')