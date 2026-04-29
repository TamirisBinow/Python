quantidade =  0
soma = 0
for numero in range(9, 91, 1):
    if numero % 3 == 0 and numero % 2 != 0 and not numero % 5  == 0:
        quantidade = quantidade + 1
        soma += numero
        print(f'  {quantidade}° múltiplo: {numero}')

print(f'A soma total: {soma}')
print(f'A quantidade é: {quantidade}')