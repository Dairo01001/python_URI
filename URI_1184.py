def main():
    S = input()

    M = [[0] * 12 for i in range(12)]
    for i in range(12):
        for j in range(12):
            M[i][j] = float(input())

    suma: float = 0
    count: int = 0
    for i in range(12):
        for j in range(i):
            suma += M[i][j]
            count += 1

    print(f"{suma:.1f}" if S == "S" else f"{suma / count:.1f}")


if __name__ == '__main__':
    main()
