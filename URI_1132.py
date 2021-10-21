def swap(a: int, b: int):
    if a > b:
        return b, a
    return a, b


def main():
    x = int(input())
    y = int(input())

    suma: int = 0
    x, y = swap(x, y)

    for i in range(x, y + 1):
        if i % 13 != 0:
            suma = suma + i
    print(suma)


if __name__ == '__main__':
    main()
