def eh_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    if numero <= 3:
        return True  # 2 e 3 são primos
    if numero % 2 == 0 or numero % 3 == 0:
        return False  # Números divisíveis por 2 ou 3 não são primos

    # Verificando divisibilidade a partir de 5 até a raiz quadrada do número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")