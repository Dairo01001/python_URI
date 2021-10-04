def main():
    a, b = list(map(int, input().split()))
    print('Sao Multiplos' if max(a, b) % min(a, b) == 0 else 'Nao sao Multiplos')


if __name__ == '__main__':
    main()
