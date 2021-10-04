def main():
    tabla = {'1': 4.0, '2': 4.5, '3': 5.0, '4': 2.0, '5': 1.5}
    x, y = input().split()
    print(f'Total: R$ {tabla[x] * int(y):.2f}')


if __name__ == '__main__':
    main()
