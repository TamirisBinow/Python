def converter_tempo(segundos_totais):
   
    horas = segundos_totais // 3600
    restante = segundos_totais % 3600
    minutos = restante // 60
    segundos = restante % 60
    return horas, minutos, segundos

try:
    segundos = int(input("Digite o número de segundos: "))
except Exception as ERRO:
    print(f'Digite um número inteiro: {ERRO}')
h, m, s = 0, 0, 0  
    

for i in range(100):
        h, m, s = converter_tempo(segundos)
        
print(f"Tempo: {segundos} Segundos = {h} Horas(s) + {m} Minuto(s) + {s} Segundos(s)")
