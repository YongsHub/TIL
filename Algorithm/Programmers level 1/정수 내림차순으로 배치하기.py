def solution(n):
    n = list(str(int(n)))
    return int(''.join(sorted(n, reverse=True)))
