def main():
    I: int = 1
    while I < 10:
        J: int = 7

        while J > 4:
            print(f'I={I} J={J}')
            J -= 1

        I += 2


if __name__ == '__main__':
    main()
