def main():
    input()
    salario = float(input())
    ventas = float(input())
    print(f'TOTAL = R$ {salario + (ventas * 0.15):.2f}')


if __name__ == '__main__':
    main()
