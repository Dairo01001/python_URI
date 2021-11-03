def main():
    while True:
        try:
            l = int(input())
            v = list(map(int, input().split()))

            ans = max(v)
            if ans < 10:
                print('1')
            elif ans < 20:
                print('2')
            else:
                print('3')
            
        except:
            break


if __name__ == '__main__':
    main()
