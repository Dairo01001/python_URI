def main():
    n = int(input())

    for i in range(n):
        numbers = list(map(float, input().split()))
        print(f'{(numbers[0] * 0.2 + numbers[1] * 0.3 + numbers[2] * 0.5):.1f}')


if __name__ == '__main__':
    main()
