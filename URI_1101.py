def swap(a: int, b: int):
    if a > b:
        return b, a
    return a, b


def main():
    while True:
        M, N = list(map(int, input().split()))

        if M < 1 or N < 1:
            break

        M, N = swap(M, N)
        suma: int = 0

        for i in range(M, N + 1):
            print(i, end=' ')
            suma += i

        print(f'Sum={suma}')


if __name__ == '__main__':
    main()
