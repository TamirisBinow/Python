def calcular_contracheque(salario_bruto, num_dependentes):
    
    salario_minimo = 1412.00
    

    inss = salario_bruto * 0.11
    plano_saude = salario_bruto * 0.02
    total_descontos = inss + plano_saude
    

    vale_alimentacao = salario_minimo + (salario_bruto * 0.05 * num_dependentes)
    

    salario_liquido = salario_bruto - total_descontos + vale_alimentacao
    
    return salario_liquido, total_descontos

while True:
    print("\n=== MENU ===")
    print("1. Calcular contracheque")
    print("0. Sair")
        
    opcao = input("Opção: ")
        
    if opcao == "0":
        break
    elif opcao == "1":
            try:
                salario_bruto = float(input("Salário Bruto: "))
                num_dependentes = int(input("Dependentes: "))
                
                liquido, descontos = calcular_contracheque(salario_bruto, num_dependentes)
                
                print(f"\nSalário Líquido: R$ {liquido:.2f}")
                print(f"Total Descontos: R$ {descontos:.2f}")
                
            except ValueError:
                print("Entrada inválida. Use números.")
    else:
            print("Opção inválida.")
