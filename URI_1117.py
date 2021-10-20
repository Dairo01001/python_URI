def main():
    cont: float = 0.0
    suma: int = 0

    while cont < 2:
        score = float(input())

        if 0 <= score <= 10:
            suma += score
            cont += 1
        else:
            print('nota invalida')

    print(f'media = {suma / cont:.2f}')


if __name__ == '__main__':
    main()
