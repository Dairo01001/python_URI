def solve(number: int) -> str:
    if number == 0: return 'NULL'
    if number > 0:
        if number % 2 == 0:
            return 'EVEN POSITIVE'
        else:
            return 'ODD POSITIVE'
    else:
        if number % 2 == 0:
            return 'EVEN NEGATIVE'

    return 'ODD NEGATIVE'


def main():
    n = int(input())
    for i in range(n):
        number = int(input())
        print(solve(number))


if __name__ == '__main__':
    main()
