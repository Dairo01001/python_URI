def is_triangulo(a: float, b: float, c: float) -> bool:
    return abs(a - c) < b < a + c


def main():
    a, b, c = list(map(float, input().split()))
    if is_triangulo(a, b, c):
        print(f'Perimetro = {a + b + c :.1f}')
    else:
        print(f'Area = {((a + b) * c) / 2 :.1f}')


if __name__ == '__main__':
    main()
