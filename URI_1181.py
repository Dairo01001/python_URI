def main():
    L: int = int(input())
    T = input()
    M = list()

    for i in range(12):
        for j in range(12):
            M.append(float(input()))

    suma = sum(M[(12 * L):(12 * L) + 12])
    print(suma if T == 'S' else f'{suma / 12:.1f}')


if __name__ == '__main__':
    main()
