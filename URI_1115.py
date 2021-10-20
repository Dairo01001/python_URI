def solve(x: int, y: int) -> str:
    if x > 0 and y > 0:
        return 'primeiro'

    if x > 0 and y < 0:
        return 'quarto'

    if x < 0 and y < 0:
        return 'terceiro'

    if x < 0 and y > 0:
        return 'segundo'


def main():
    while True:
        x, y = list(map(int, input().split()))

        if x == 0 or y == 0:
            break

        print(solve(x, y))


if __name__ == '__main__':
    main()
