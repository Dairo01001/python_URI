def main():
    N = int(input())
    X = list(map(int, input().split()))

    minimo: int = X[0]
    index: int = 0
    for i in range(1, N):
        if minimo > X[i]:
            minimo = X[i]
            index = i

    print(f'Menor valor: {minimo}')
    print(f'Posicao: {index}')


if __name__ == '__main__':
    main()
