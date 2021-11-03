def main():
    c = int(input())
    for i in range(c):
        name, n = input().split()
        if name == 'Thor' or name == 'thor':
            print('Y')
        else:
            print('N')

if __name__ == '__main__':
    main()
