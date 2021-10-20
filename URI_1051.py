def solve(salary: float):

    if salary > 4500.00:
        dif = salary - 4500.00
        return (dif * 0.28) + 270.0 + 80.0

    if salary > 3000.00:
        dif = salary - 3000.00
        return (dif * 0.18) + 80.0

    if salary > 2000.00:
        dif = salary - 2000.00
        return dif * 0.08


def main():
    salary: float = float(input())

    if salary <= 2000.00:
        print('Isento')
    else:
        print(f'R$ {solve(salary):.2f}')


if __name__ == '__main__':
    main()
