def main():
    suma = 0
    cont = 0
    for i in range(6):
        aux = input()
        if aux[0] != '-':
            suma = suma + float(aux)
            cont = cont + 1

    print(cont, 'valores positivos')
    print(f'{suma / cont:.1f}')


if __name__ == '__main__':
    main()
