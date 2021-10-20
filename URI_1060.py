def main():
    cont: int = 0
    for i in range(6):
        aux = input()
        cont = cont + 1 if aux[0] != '-' else cont

    print(cont, 'valores positivos')


if __name__ == '__main__':
    main()
