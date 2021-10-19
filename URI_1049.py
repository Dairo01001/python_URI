def solve():
    table = {'vertebrado': {'ave': {'carnivoro': 'aguia',
                                    'onivoro': 'pomba'},
                            'mamifero': {'onivoro': 'homem',
                                         'herbivoro': 'vaca'}
                            },
             'invertebrado': {'inseto': {'hematofago': 'pulga',
                                         'herbivoro': 'lagarta'},
                              'anelideo': {'hematofago': 'sanguessuga',
                                           'onivoro': 'minhoca'}
                              }
             }

    print(table[input()][input()][input()])


if __name__ == '__main__':
    solve()
