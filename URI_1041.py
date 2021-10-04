def coordenadas(x: float, y: float) -> str:

    if x == 0 and y == 0:
        return 'Origem'

    if y == 0:
        return 'Eixo X'

    if x == 0:
        return 'Eixo Y'

    if x > 0 and y > 0:
        return 'Q1'

    if x < 0 and y > 0:
        return 'Q2'

    if x < 0 and y < 0:
        return 'Q3'

    if x > 0 and y < 0:
        return 'Q4'


def main():
    x, y = list(map(float, input().split()))
    print(coordenadas(x, y))


if __name__ == '__main__':
    main()
