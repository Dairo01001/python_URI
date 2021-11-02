def main():
    n, k = list(map(int, input().split()))
    estu = list()

    for i in range(n):
        estu.append(input())

    estu.sort()
    print(estu[k - 1])


if __name__ == '__main__':
    main()
