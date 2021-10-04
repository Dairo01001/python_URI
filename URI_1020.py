def main():
    n = int(input())
    a = n // 365
    n = n - (365 * a)
    m = n // 30
    n = n - (30 * m)
    print(f'{a} ano(s)')
    print(f'{m} mes(es)')
    print(f'{n} dia(s)')


if __name__ == '__main__':
    main()
