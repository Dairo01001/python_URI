def solve():
    suma: float = 0.0
    cont: int = 0
    while cont < 2:
        score = float(input())

        if 0 <= score <= 10:
            suma += score
            cont += 1
        else:
            print('nota invalida')

    print(f'media = {(suma / cont):.2f}')


def main():
    solve()

    while True:
        ans = int(input('novo calculo (1-sim 2-nao)\n'))
        if ans == 1:
            solve()
        elif ans == 2:
            break


if __name__ == '__main__':
    main()

