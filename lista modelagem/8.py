
def soma(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1  
    soma = a + b 
    
    for x in range(2, n):
        c = a + b     
        soma = c + 1     
        a, b = b, c   
    
    return soma

try:
    n = int(input("Digite o valor de n: "))
    resultado = soma(n)
    print(f"O somatório dos {n} primeiros termos da série de Fibonacci é: {resultado}")
except Exception as ERRO:
    print(f'ERRO: {ERRO}')
