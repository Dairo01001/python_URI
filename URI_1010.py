def main():
    prod = list(map(float, input().split()))
    prod1 = list(map(float, input().split()))
    print(f'VALOR A PAGAR: R$ {(prod[1] * prod[2]) + (prod1[1] * prod1[2]):.2f}')


if __name__ == '__main__':
    main()
