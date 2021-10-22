def main():
    N: int = int(input())
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)


if __name__ == '__main__':
    main()
