def main():
    aux = list(map(float, input().split()))
    aux.sort(reverse=True)
    a, b, c = aux

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
        return

    A = a ** 2
    B = b ** 2
    C = c ** 2

    if A == B + C:
        print('TRIANGULO RETANGULO')

    if A > B + C:
        print('TRIANGULO OBTUSANGULO')

    if A < B + C:
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
        return

    if a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    main()
