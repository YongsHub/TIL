import sys
sys.setrecursionlimit(10 ** 6)


def makeOne(num, n):
    if num == 1:
        return n
    elif num % 2 == 0:  # 짝수라면
        n += 1
        n = makeOne(num // 2, n)
    else:
        num *= 3
        num += 1
        n += 1
        n = makeOne(num, n)
    return n


def solution(num):
    answer = 0
    n = makeOne(num, 0)
    return n if n <= 500 else -1
