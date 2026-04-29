def verificar_triangulo(a, b, c):
 
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é triângulo: Lados > 0."
    
    if not (a < b + c and b < a + c and c < a + b):
        return "Não é triângulo."
    
    lados_iguais = 0
    if a == b: lados_iguais = lados_iguais + 1
    if b == c:  lados_iguais = lados_iguais + 1
    if a == c: lados_iguais = lados_iguais + 1
    
    if lados_iguais == 3:
        return "Triângulo Equilátero (3 lados iguais)."
    elif lados_iguais == 2:
        return "Triângulo Isósceles (2 lados iguais)."
    else:
        return "Triângulo Escaleno (0 lados iguais)."

while True:
    print("\n=== MENU ===")
    print("1. Verificar triângulo")
    print("0. Sair")
        
    opcao = input("Opção: ")
        
    if opcao == "0":
            break
    elif opcao == "1":
            try:
                a = float(input("A: "))
                b = float(input("B: "))
                c = float(input("C: "))
                print(verificar_triangulo(a, b, c))
            except ValueError:
                print("Entrada inválida. Use números.")
    else:
            print("Opção inválida.")
