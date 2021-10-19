def calculate(salary, increase):
    pay_rise = salary * (increase / 100)
    new_salary = pay_rise + salary
    return new_salary, pay_rise


def solve():
    salario: float = float(input())
    if 0 <= salario <= 400.00:
        per = 15
        a, b = calculate(salario, per)
    elif 400.01 <= salario <= 800.00:
        per = 12
        a, b = calculate(salario, per)
    elif 800.01 <= salario <= 1200.00:
        per = 10
        a, b = calculate(salario, per)
    elif 1200.01 <= salario <= 2000.00:
        per = 7
        a, b = calculate(salario, per)
    else:
        per = 4
        a, b = calculate(salario, per)

    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: {per} %')


if __name__ == '__main__':
    solve()
