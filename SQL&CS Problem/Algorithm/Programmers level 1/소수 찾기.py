def prime(n):
    check = [True] * (n + 1)

    for i in range(2, n + 1):
        if check[i] == True:
            for j in range(i + i, n + 1, i):
                check[j] = False
    return check


def solution(n):
    check = prime(n)
    answer = 0
    for i in range(2, n + 1):
        if check[i] == True:
            answer += 1

    return answer
