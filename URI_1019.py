def main():
    n = int(input())
    h = n // 3600
    n = n - (3600 * h)
    m = n // 60
    n = n - (60 * m)
    print(f'{h}:{m}:{n}')


if __name__ == '__main__':
    main()
