def soma_numeros_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

# Exemplo de uso:
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = soma_numeros_pares(minha_lista)
print(f"A soma dos números pares na lista é: {resultado}")