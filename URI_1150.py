def main():
    X: int = int(input())
    Y: int = int(input())

    while Y <= X:
        Y = int(input())

    cont: int = 1
    answer: int = X

    while answer < Y:
        X += 1
        answer += X
        cont += 1

    print(cont)


if __name__ == '__main__':
    main()
