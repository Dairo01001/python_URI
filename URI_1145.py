def main():
    x, y = list(map(int, input().split()))

    cont: int = 1
    aux: int = 1

    while True:

        print(cont, end=' ' if aux < x else '\n')

        aux += 1
        if aux > x:
            aux = 1

        cont += 1

        if cont > y:
            break


if __name__ == '__main__':
    main()
