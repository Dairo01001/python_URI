def main():
    billetes = [100, 50, 20, 10, 5, 2, 1]
    n = int(input())
    print(n)
    for billete in billetes:
        ans = n // billete
        if ans != 0:
            n = n - (ans * billete)
        print(f'{ans} nota(s) de R$ {billete},00')


if __name__ == '__main__':
    main()
