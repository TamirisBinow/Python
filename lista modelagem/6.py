def imc(peso, altura, sexo):
    if sexo == 'm':
        imc = 0.95 * peso / (altura ** 2)
    elif sexo == 'h':
        imc = 1.05 * peso / (altura ** 2)
    return imc


sexo = input('Digite seu gênero (h/m): ')

if sexo not in ['h', 'm']:
    print('Gênero inválido!')
else:
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))

    resultado_imc = imc(peso, altura, sexo)
    print(f'Seu IMC é: {resultado_imc:.2f}')
