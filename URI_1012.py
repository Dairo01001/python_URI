PI = 3.14159


def main():
    a, b, c = list(map(float, input().split()))
    print(f'TRIANGULO: {(a * c) / 2:.3f}')
    print(f'CIRCULO: {(PI * c ** 2):.3f}')
    print(f'TRAPEZIO: {((a + b) * c) / 2:.3f}')
    print(f'QUADRADO: {b ** 2:.3f}')
    print(f'RETANGULO: {a * b:.3f}')


if __name__ == '__main__':
    main()
