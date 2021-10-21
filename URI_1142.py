def main():
    N: int = int(input())
    cont: int = 0
    for i in range(N):

        for j in range(3):
            cont = cont + 1
            print(cont, end=' ')
        print('PUM')
        cont = cont + 1


if __name__ == '__main__':
    main()
