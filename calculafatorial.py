def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial indefinido para números negativos"
    elif numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número: "))
resultado = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')