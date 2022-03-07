import sys
sys.setrecursionlimit(10 ** 6)


def dfs(computers, check, n):
    if check[n] == True:
        return False
    else:
        check[n] = True

    for index, value in enumerate(computers[n]):
        if value == 1 and check[index] == False:
            dfs(computers, check, index)

    return True


def solution(n, computers):
    answer = 0
    check = [False] * n
    for i in range(n):
        if dfs(computers, check, i):
            answer += 1
    return answer
