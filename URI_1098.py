def main():
    I = 0
    while I <= 20:
        i_value = I / 10
        J = 1
        while J < 4:
            j_value = J + i_value

            if i_value == int(i_value):
                print(f'I={int(i_value)} J={int(j_value)}')
            else:
                print(f'I={i_value} J={j_value}')

            J += 1

        I += 2


if __name__ == '__main__':
    main()
