
def solve():
    tabla = {
        '61': 'Brasilia',
        '71': 'Salvador',
        '11': 'Sao Paulo',
        '21': 'Rio de Janeiro',
        '32': 'Juiz de Fora',
        '19': 'Campinas',
        '27': 'Vitoria',
        '31': 'Belo Horizonte'
    }

    coding = input()

    if coding in tabla.keys():
        print(tabla[coding])
    else:
        print('DDD nao cadastrado')


if __name__ == '__main__':
    solve()
