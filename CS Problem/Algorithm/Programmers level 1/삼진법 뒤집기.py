def makeMeasure(number, lst):
    if (number // 3) > 0:
        lst.append(number % 3)
        if (number // 3) == 1 or (number // 3) == 2:
            lst.append(number // 3)
        return makeMeasure(number // 3, lst)
    return lst


def solution(n):
    answer = 0
    lst = []

    if n == 1:
        return 1

    lst = makeMeasure(n, lst)
    lst.reverse()
    for i in range(len(lst)):
        answer += (3 ** i) * lst[i]
    return answer
