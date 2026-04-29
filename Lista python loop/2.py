quantidade =  0
soma = 0
print('Escrever um algoritmo para exibir os múltiplos de 11, a soma e a média dos múltiplos de 11, em ordem decrescente (inversa), compreendidos entre o intervalo: [200 100].')
for numero in range(200, 100, -1):
    if numero % 11 == 0:
        quantidade = quantidade + 1
        soma += numero
        media = soma / quantidade
        print(f'  {quantidade}° múltiplo: {numero}')

print(f'A soma total: {soma}')
print(f'A média é: {media}')