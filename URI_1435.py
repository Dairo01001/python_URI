def main():
    while True:
        n = int(input())
        
        if n == 0: break
        M = [[0] * n for i in range(n)]
        
        for i in range(n):
            end_i = n - 1 - i
            for j in range(i, n - i):
                end_j = n - 1 - j
                M[i][j] = i + 1;
                M[j][i] = i + 1;
                M[end_i][end_j] = i + 1
                M[end_j][end_i] = i + 1
        
        for i in range(n):
            for j in range(n - 1):
                print('{}'.format(str(M[i][j]).rjust(3)), end=' ')
            print('{}'.format(str(M[i][n - 1]).rjust(3)))

        print()

        
if __name__ == '__main__':
    main()
