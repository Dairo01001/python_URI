def res(a: int, b: int, op: chr) -> int:
    if op == '+':
        return a + b

    if op == '-':
        return a - b

    if op == 'x':
        return a * b


def main():
    n = int(input())

    for i in range(n):
        eq = input().split()
        ans = int(eq[-1])
        resp = 'E' + \
            (abs(ans - (res(int(eq[0]), int(eq[2]), eq[1]))) * 'r') + 'ou!'
        print(resp)


if __name__ == '__main__':
    main()
