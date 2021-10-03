import math


def main():
    x, y = list(map(float, input().split()))
    x1, y1 = list(map(float, input().split()))
    print(f'{math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2):.4f}')


if __name__ == '__main__':
    main()
