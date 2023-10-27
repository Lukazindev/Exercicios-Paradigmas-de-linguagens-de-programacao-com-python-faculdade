while True:
    try:
        x = int(input('Digite um número:'))
        break
    except ValueError:
        print('Digite com um número válido')