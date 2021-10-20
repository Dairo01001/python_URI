def swap(a: int, b: int):
    if a > b:
        return b, a
    return a, b


def main():
    N: int = int(input())
    for i in range(N):
        x, y = list(map(int, input().split()))
        suma = 0

        x, y = swap(x, y)

        for j in range(x + 1, y):
            if j % 2 != 0:
                suma += j

        print(suma)


if __name__ == '__main__':
    main()
