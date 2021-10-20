def main():
    N = int(input())

    for i in range(N):
        x, y = list(map(int, input().split()))

        if y == 0:
            print('divisao impossivel')
        else:
            print(f'{(x / y):.1f}')


if __name__ == '__main__':
    main()
