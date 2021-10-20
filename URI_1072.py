def ran(x: int) -> bool:
    return 10 <= x <= 20


def main():
    n = int(input())

    dentro: int = 0

    for i in range(n):
        x = int(input())
        dentro = dentro + 1 if ran(x) else dentro

    print(dentro, 'in')
    print(n - dentro, 'out')


if __name__ == '__main__':
    main()
