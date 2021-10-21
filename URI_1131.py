def main():
    gana_a: int = 0
    gana_b: int = 0
    empate: int = 0

    while True:
        a, b = list(map(int, input().split()))

        if a == b:
            empate = empate + 1
        elif a > b:
            gana_a = gana_a + 1
        else:
            gana_b = gana_b + 1

        opc = input('Novo grenal (1-sim 2-nao)\n')
        if opc == '2':
            break

    print(f'{gana_a + gana_b + empate} grenais')
    print(f'Inter:{gana_a}')
    print(f'Gremio:{gana_b}')
    print(f'Empates:{empate}')
    if gana_a == gana_b:
        print('Não houve vencedor')
    elif gana_a > gana_b:
        print('Inter venceu mais')
    else:
        print('Gremio venceu mais')


if __name__ == '__main__':
    main()
