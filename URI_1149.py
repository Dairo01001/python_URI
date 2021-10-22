def main():
    numbers = list(map(int, input().split()))

    A = numbers[0]
    N = numbers[-1]

    ans = 0

    for i in range(1, N + 1):
        ans += A
        A += 1

    print(ans)


if __name__ == '__main__':
    main()
