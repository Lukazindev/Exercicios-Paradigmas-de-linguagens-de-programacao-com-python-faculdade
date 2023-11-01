from time import sleep
from threading import Thread
def calcular_cubo(num, tempo_espera):
    print(f'\nCubo: {num * num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_cubo')

def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')

t1 = Thread(target=calcular_quadrado, args=(5,3))
t2 = Thread(target=calcular_cubo, args=(5,2))
t1.start()
t2.start()
t1.join()# esperar até completar a execução da thread 1
t2.join()# esperar até completar a execução da thread 2
print('A execução foi concluida!')