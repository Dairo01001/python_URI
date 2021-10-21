def main():
    N: int = int(input())

    for i in range(1, N + 1):
        print(i, i ** 2, i ** 3)
        print(i, i ** 2 + 1, i ** 3 + 1)


if __name__ == '__main__':
    main()
