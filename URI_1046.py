def tiempo(a, b):
    if b == 0:
        b = 24

    ans = (24 - a) + b

    if a == 0:
        ans = a + b

    if ans > 24:
        ans = b - a

    return ans


def main():
    a, b = list(map(int, input().split()))
    print(f'O JOGO DUROU {tiempo(a, b)} HORA(S)')


if __name__ == '__main__':
    main()
