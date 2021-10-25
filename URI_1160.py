def main():
    T: int = int(input())

    for i in range(T):
        data = input().split()

        PA, PB = list(map(int, data[:2]))
        G1, G2 = list(map(float, data[2:]))

        cont: int = 0
        while PA <= PB:
            cont += 1
            PA += (PA * G1) // 100
            PB += (PB * G2) // 100

            if cont > 100:
                break

        if cont > 100:
            print('Mais de 1 seculo.')
        else:
            print(f'{cont} anos.')


if __name__ == '__main__':
    main()
