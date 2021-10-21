def main():
    codings = [0, 0, 0, 0]

    while True:
        code: int = int(input())

        if 1 <= code < 4:
            codings[code] = codings[code] + 1

        if code == 4:
            break

    print('MUITO OBRIGADO')
    print(f'Alcool: {codings[1]}')
    print(f'Gasolina: {codings[2]}')
    print(f'Diesel: {codings[3]}')


if __name__ == '__main__':
    main()
