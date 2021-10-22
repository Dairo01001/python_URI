def main():
    suma: int = 0
    cont: int = 0

    while True:
        age: int = int(input())
        if age < 0:
            break

        suma += age
        cont += 1

    print(f'{suma / cont:.2f}')


if __name__ == '__main__':
    main()
