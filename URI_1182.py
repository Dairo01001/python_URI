def main():
    C: int = int(input())
    T = input()

    M = list()
    for i in range(12):
        for j in range(12):
            M.append(float(input()))

    suma: float = 0.0
    for i in range(12):
        suma += M[(i * 12) + C]

    print(f'{suma:.1f}' if T == 'S' else f'{suma / 12:.1f}')


if __name__ == '__main__':
    main()
