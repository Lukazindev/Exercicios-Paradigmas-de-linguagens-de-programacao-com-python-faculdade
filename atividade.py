from threading import Thread
from multiprocessing import process
#x = int(input())
#y = int(input())

#x = x/y
#y = y/x

#print(y)

#x = int(input())
#y = int(input())

#x = x % y
#x = x % y
#y = y % x

#print(y)

#x = 1 / 2 + 3 // 3 + 4 ** 2

#print(x)

#a,b = 0,1

#while b < 10:

#    print(b)
#    a,b = b, a+b

#a = 0

#for i in range(30):
#    if a%2 == 0:
#        a+= 1
#        continue
#    else:
#        if a%5 == 0:
#            break
#else:
#    a+= 3
#    print(a)

#def Fatorial ( n ):
#    if(n == 1) or (n == 0):
#        return 1
#    else:
#        return Fatorial(n - 1)*n

#def foo(n):
#    if n > 1:
#        return n * foo(n - 1)
#    return n
#print(foo(4))

#minha_lista = [0, 5, 10, 15, 20, 25, 30]

#def filtro(numero):
#    if numero > 10:
#        return True
#    return False

#minha_lista_filtrada = filter(filtro, minha_lista)

#print(minha_lista_filtrada)

minha_lista = []

def funcao():
    for i in range(100000):
        minha_lista.append(1)
    for i in range(100000):
        minha_lista.pop()

if __name__ == '__main__':
    processos = []
    for indice in range(10):
        processo = process(target=funcao)
        processos.append(processo)
        processo.start()
    
    print(len(minha_lista))
    for processo in processos:
        processo.join()
    print(len(minha_lista))