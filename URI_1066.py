def main():
    pares: int = 0
    positivos: int = 0
    negativos: int = 0

    for i in range(5):
        num = int(input())

        if num > 0:
            positivos = positivos + 1
        elif num < 0:
            negativos = negativos + 1

        pares = pares + 1 if num % 2 == 0 else pares

    print(pares, 'valor(es) par(es)')
    print(5 - pares, 'valor(es) impar(es)')
    print(positivos, 'valor(es) positivo(s)')
    print(negativos, 'valor(es) negativo(s)')


if __name__ == '__main__':
    main()
