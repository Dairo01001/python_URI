def main():
    exp_lab = {'C': 0, 'R': 0, 'S': 0}
    total: int = 0

    n = int(input())

    for i in range(n):
        number, tipo = input().split()
        exp_lab[tipo] += int(number)
        total += int(number)

    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {exp_lab["C"]}')
    print(f'Total de ratos: {exp_lab["R"]}')
    print(f'Total de sapos: {exp_lab["S"]}')
    print(f'Percentual de coelhos: {((exp_lab["C"] * 100) / total):.2f} %')
    print(f'Percentual de ratos: {((exp_lab["R"] * 100) / total):.2f} %')
    print(f'Percentual de sapos: {((exp_lab["S"] * 100) / total):.2f} %')


if __name__ == '__main__':
    main()
