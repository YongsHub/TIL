def solution(n):
    sqrt = n ** 0.5
    if sqrt == int(sqrt):
        sqrt = (sqrt + 1) ** 2
        return sqrt
    else:
        return -1
