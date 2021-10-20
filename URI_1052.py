MONTHS = ['',
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def solve(month: int) -> str:
    return MONTHS[month]


def main():
    print(solve(int(input())))


if __name__ == '__main__':
    main()
