import math


def main():
    a, b, c = list(map(float, input().split()))
    try:
        x = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        x1 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        print(f'R1 = {x:.5f}')
        print(f'R2 = {x1:.5f}')
    except Exception:
        print('Impossivel calcular')


if __name__ == '__main__':
    main()
