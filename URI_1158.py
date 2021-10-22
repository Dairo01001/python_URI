def main():
    N: int = int(input())

    for i in range(N):
        X, Y = list(map(int, input().split()))
        X = X if X % 2 != 0 else X + 1

        suma: int = 0
        for j in range(Y):
            suma = suma + X
            X += 2
        print(suma)


if __name__ == '__main__':
    main()
    