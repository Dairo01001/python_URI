def main():
    I: int = 1
    J: int = 7
    while I < 10:
        aux_index: int = 0
        while aux_index < 3:
            print(f'I={I} J={J - aux_index}')
            aux_index += 1

        J += 2
        I += 2


if __name__ == '__main__':
    main()
