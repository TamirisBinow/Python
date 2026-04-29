turma = []
aluno = []

indice = 0   # ITERAÇÃO / INDEXAÇÃO:
print('MENU')
print('1: CADASTRAR ALUNO')
print('2: EXIBIR A LISTA DA TURMA')
print('QUALQUER TECLA: SAIR DO PROGRAMA')
while True:
  try:
    opcao = int(input('Sua opação: '))
    if(opcao < 1 or opcao > 2):
      print('Fim do programa')
      break
    elif(opcao == 1):
      print(f"Dados do Aluno {indice  + 1}: ") # ENUMERAÇÃO
      # LER: Variável Nome (string)
      while True:
        try:
          nome = input('Nome: ')
          if(len(nome) < 2):
            print('ERRO NO NOME: Escolha de novo.')
          else:
            break
        except:
          print('ERRO DE EXCECAO NO NOME: Escolha de novo.')
      # LER: Variável Matricula (int)
      while True:
        try:
          matricula = int(input('Matrícula (XXX): '))
          if(matricula < 100 or matricula > 999):
            print('ERRO NA MATRÍCULA: Escolha de novo.')
          else:
            break
        except:
          print('ERRO DE EXCECAO NA MATRÍCULA: Escolha de novo.')
      # LER: Variável Nota 1° Bimestre (float): [0.0, 10.0]
      while True:
        try:
          B1 = float(input('Nota 1° Bimestre [0.0, 10.0]: '))
          if(B1 < 0.0 or B1 > 10.0):
            print('ERRO NA NOTA 1° BIMESTRE: Escolha de novo.')
          else:
            break
        except:
          print('ERRO DE EXCECAO NA NOTA 1° BIMESTRE: Escolha de novo.')
      # LER: Variável Nota 2° Bimestre (float): [0.0, 10.0]
      while True:
        try:
          B2 = float(input('Nota 2° Bimestre [0.0, 10.0]: '))
          if(B2 < 0.0 or B2 > 10.0):
            print('ERRO NA NOTA 2° BIMESTRE: Escolha de novo.')
          else:
            break
        except:
          print('ERRO DE EXCECAO NA NOTA 2° BIMESTRE: Escolha de novo.')
          
      aluno = [nome, matricula, B1, B2] # Lista: Aluno
      turma.append(aluno)
      indice =+ 1  # ITERAÇÃO
    else:
      # RELATÓRIO: MENU: OPÇÃO 2
      if(len(turma) == 0):
        print('Turma vazio')
      else:
        print(f'LISTA DOS {len(turma)} ALUNOS DA TURMA: ')
        for indice, valor in enumerate(turma):
          print(f'ALUNO {indice + 1}: ')
          print(f'NOME: {valor[0]}')
          print(f'MATRÍCULA: {valor[1]}')
          print(f'NOTA 1° BIMESTRE: {valor[2]: .1f}')
          print(f'NOTA 2° BIMESTRE: {valor[3]: .1f}\n')
  except:
    print('Fim do programa')
    break