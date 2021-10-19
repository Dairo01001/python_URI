def delta(h0: int, h1: int) -> int:
    h1 = 24 if h1 == 0 else h1
    ans: int = 24 - h0 + h1
    ans = h0 + h1 if h0 == 0 else ans
    ans = h1 - h0 if ans > 24 else ans
    return ans


def solve():
    h0, m0, h1, m1 = list(map(int, input().split()))
    ans_h: int = delta(h0, h1)
    ans_m: int = 60 - m0 + m1
    if ans_m >= 60:
        ans_m -= 60
    else:
        ans_h = ans_h - 1

    ans_h = 0 if ans_h == 24 and ans_m != 0 else ans_h

    print(f'O JOGO DUROU {ans_h} HORA(S) E {ans_m} MINUTO(S)')


if __name__ == '__main__':
    solve()

