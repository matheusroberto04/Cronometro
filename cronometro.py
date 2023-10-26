import time

def cronometro(segundos):
    while segundos >= 0:
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        print(f"{minutos:02d}:{segundos_restantes:02d}", end='\r')
        time.sleep(1)
        segundos -= 1
    print("Tempo encerrado!")

tempo_total = int(input("Digite o tempo em segundos: "))
cronometro(tempo_total)
