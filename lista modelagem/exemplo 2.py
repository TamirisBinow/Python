catalogo = []
livro = []
indice = 0

print('MENU')
print('1 - Cadastrar livro')
print('2 - Exibir catálogo')
print('Qualquer outro número - Sair')

while True:
    try:
menu = int(input('Digite a opção que deseja: '))
    except ValueError:
    print('Finalizando o programa')
        break

    if menu == 1:
        print(f'Produto {indice + 1}: ')

        # Título
        while True:
            titulo = input('Digite o titulo do livro: ').strip()
     if len(titulo) < 2:
                print('Título inválido')
    else:
                break

        # Código (100–999)
        while True:
            try:
                codigo = int(input('Digite o código do produto (100-999): '))
                if codigo < 100 or codigo > 999:
                    print('Código inválido')
                else:
                    break
            except ValueError:
                print('ERRO: código deve ser inteiro.')

        # Ano (1900–2100)
        while True:
            try:
                ano = int(input('Digite o ano do livro (1900-2100): '))
                if ano < 1900 or ano > 2100:
                    print('Ano inválido')
                else:
                    break
            except ValueError:
                print('ERRO: ano deve ser inteiro.')

        # Nota (0–10)
        while True:
            try:
                nota = float(input('Digite a nota do livro (0-10): '))
                if nota < 0.0 or nota > 10.0:
                    print('Nota inválida')
                else:
                    break
            except ValueError:
                print('ERRO: nota deve ser número.')

        livro = [titulo, codigo, ano, nota]
        catalogo.append(livro)
        indice += 1

    elif menu == 2:
        if len(catalogo) == 0:
            print('Nenhum livro cadastrado')
        else:
            print(f'Lista de livros cadastrados ({len(catalogo)}):')
            for i, livro in enumerate(catalogo, start=1):
                titulo, codigo, ano, nota = livro
                print(f'Livro {i}:')
                print(f'  título: {titulo}')
                print(f'  código: {codigo}')
                print(f'  ano: {ano}')
                print(f'  nota: {nota:.2f}')
    else:
        print('Finalizando o programa')
        break
