def main():
    n = list(map(int, input().split()))
    aux = n[:]
    n.sort()
    for i in n:
        print(i)
    print()
    for i in aux:
        print(i)


if __name__ == '__main__':
    main()
