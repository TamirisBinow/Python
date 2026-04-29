spares = 0
simpares = 0

for numero in range(10, 100):

    if numero % 2 == 0:
        spares = spares + numero
    else:
        simpares = simpares + numero

print(f'A soma dos números pares é: {spares}')
print(f'A soma dos números ímpares é: {simpares}')