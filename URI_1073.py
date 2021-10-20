def imprimir_cuadrado(number: int):
    return f'{number}^{2} = {number * number}'


def main():
    n = int(input())
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(imprimir_cuadrado(i))


if __name__ == '__main__':
    main()
