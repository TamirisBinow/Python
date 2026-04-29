# Escrever um algoritmo que leia vários números reais (um por um) e exiba, em porcentagem, a quantidade de positivos e de negativos lidos. Pare o programa quando o usuário digitar ZERO
positivo = 0 
negativo = 0 
tentativas = 0
while True:
    try:
        numero = float (input('Digite um número real, ou zero para sair: '))
        if numero == 0:
            break
        if numero > 0:
            positivo = positivo + 1
            tentativas = tentativas + 1
        else:
            negativo = negativo + 1
            tentativas = tentativas + 1
    except Exception as ERRO:
        print(f'Erro: {ERRO}')
        
print(f'A porcentagem de números positivos é: {(positivo/tentativas)*100}')
print(f'A porcentagem de números negativos é: {(negativo/tentativas)*100}')
