def solution(x, n):
    answer = [x] * n

    for i in range(2, len(answer) + 1):
        answer[i - 1] = answer[i - 1] * i
    return answer
