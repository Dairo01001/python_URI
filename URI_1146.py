def main():
    while True:
        x: int = int(input())

        if not bool(x):
            break

        for i in range(1, x):
            print(i, end=' ')
        print(x)


if __name__ == '__main__':
    main()
