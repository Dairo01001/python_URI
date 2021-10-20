def main():
    cont: int = 0
    for i in range(5):
        inp = int(input())
        if inp % 2 == 0:
            cont = cont + 1

    print(cont, 'valores pares')


if __name__ == '__main__':
    main()
