def main():
    pesos = [0.2, 0.3, 0.4, 0.1]
    notas = list(map(float, input().split()))
    prom = 0.0
    i = 0
    for nota in notas:
        prom = prom + (nota * pesos[i])
        prom = float(str(prom)[:4])
        i = i + 1

    print(f'Media: {prom:.1f}')
    if prom >= 7.0:
        print('Aluno aprovado.')
    elif prom < 5.0:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        nota = float(input())
        print(f'Nota do exame: {nota:.1f}')
        prom = (prom + nota) / 2
        if prom >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f'Media final: {prom:.1f}')


if __name__ == '__main__':
    main()
