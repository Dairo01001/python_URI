def main():
    x = int(input())
    y = int(input())

    sum_impares: int = 0
    for i in range(min(x, y) + 1, max(x, y)):
        sum_impares = sum_impares + i if i % 2 != 0 else sum_impares

    print(sum_impares)


if __name__ == '__main__':
    main()
