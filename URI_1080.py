def main():
    max_number: int = 0
    index: int = 0

    for i in range(1, 101):
        number = int(input())
        if number > max_number:
            max_number = number
            index = i

    print(max_number)
    print(index)


if __name__ == '__main__':
    main()
