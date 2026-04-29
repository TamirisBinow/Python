def primo(n):
    if n < 1:
        return False
    if n == 1:
        return True  
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for x in range(500):
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 1:
                print("Digite apenas números positivos.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    if primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
