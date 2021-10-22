def main():
    while True:
        N: int = int(input())

        if N == 0:
            break

        suma: int = 0
        N = N if N % 2 == 0 else N + 1

        for i in range(5):
            suma += N
            N += 2
        print(suma)


if __name__ == '__main__':
    main()
