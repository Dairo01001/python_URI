def main():
    while True:
        try:
            n = int(input())

            result = [['3'] * n for i in range(n)]
            
            x_1 = 0
            x_2 = n - 1
            for i in range(n):
                result[i][x_1] = '1'
                result[i][x_2] = '2'
                x_1 += 1
                x_2 -= 1

            for i in range(n):
                print(''.join(result[i]))

        except:
            break


if __name__ == '__main__':
    main()
