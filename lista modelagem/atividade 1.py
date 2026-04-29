empresa = []
funcionario = []
func = 0
p1 = 0
p2 = 0


def Nome(Nome):
 while True:
        try:
            nome = input('Digite seu nome: ')
            if(len(nome) < 2):
                print('ERRO NO NOME: Escolha de novo.')
            else:
                return Nome
        except:
            print('ERRO DE EXCECAO EM NOME: escolha de novo.')  
            
            
            
def Cargo(Cargo):
     while True:
        try:
            cargo = input('Digite seu cargo: ')
            if(len(cargo) < 2):
                print('ERRO NO CARGO: Escolha de novo.')
            else:
                return Cargo
        except:
            print('ERRO DE EXCECAO EM CARGO: escolha de novo.')  
    
    
def PlanoSaude(p1, p2):
    while True:
        try:
            plano = int(input('Você tem plano de saúde? 1 - sim ou 2 - não: '))
            if plano == 1:
                p1 += 1
                return p1, p2        # <── retorna aqui
            elif plano == 2:
                p2 += 1
                return p1, p2        # <── retorna aqui
            else:
                print('Escolha corretamente (1 ou 2).')
        except:
            print('ERRO DE EXCECAO EM PLANO: escolha de novo.')

    
def Salario(salario):
    while True:
        try:
            salario = float('Digite seu sálario: ')
            if salario < 1000:
                print('Digite corretamente.')
            else:
                return salario 
        except:
            print('ERRO DE EXCECAO EM SALARIO: escolha de novo.')
           
            
def senha():
    quantidade = 0
    for contador in range(1000, 10001):  # inclui 10000
        if contador % 2 != 0 and contador % 39 == 0:
            quantidade += 1
    return quantidade



    

