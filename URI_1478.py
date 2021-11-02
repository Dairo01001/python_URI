def main():
    while True:
        n = int(input())
        if not bool(n): break
        m = [[0] * n for i in range(n)]
        
        for i in range(n):
            count = 1
            for j in range(i, n):
                m[i][j] = count
                m[j][i] = count
                count += 1

        for i in range(n):
            for j in range(n - 1):
                print('{}'.format(str(m[i][j]).rjust(3)), end=' ')
            print('{}'.format(str(m[i][n - 1]).rjust(3)))
        print()                


if __name__ == '__main__':
    main()
