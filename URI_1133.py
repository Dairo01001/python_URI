def swap(a: int, b: int):
    if a > b:
        return b + 1, a
    return a, b


def main():
    x = int(input())
    y = int(input())

    x, y = swap(x, y)

    for i in range(x, y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)


if __name__ == '__main__':
    main()
