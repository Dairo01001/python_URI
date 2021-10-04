def main():
    billetes = [100, 50, 20, 10, 5, 2]
    monedas = [100, 50, 25, 10, 5, 1]

    n = float(input())

    print('NOTAS:')
    for billete in billetes:
        ans = n // billete
        n = n - (ans * billete)
        print(f'{int(ans)} nota(s) de R$ {billete:.2f}')

    print('MOEDAS:')
    n = n * 100
    for moneda in monedas:
        ans = n // moneda
        n = n - (ans * moneda)
        print(f'{int(ans)} moeda(s) de R$ {moneda / 100:.2f}')


if __name__ == '__main__':
    main()
