def main():

    while True:
        n: int = int(input())
        if n == 0:
            break

        m = [[0] * n for i in range(n)]
        pos = 1
        for i in range(n):
            aux = pos
            for j in range(n):
                m[i][j] = aux
                aux *= 2
            pos *= 2

        lon = len(str(m[n - 1][n - 1]))
        for i in range(n):
            for j in range(n - 1):
                print('{}'.format(str(m[i][j]).rjust(lon)), end=' ')
            print('{}'.format(str(m[i][n - 1]).rjust(lon)))
        print()


if __name__ == '__main__':
    main()
