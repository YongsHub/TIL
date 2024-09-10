def solution(a, b):
    answer = 0
    if a >= b:
        start = b
        end = a
    else:
        start = a
        end = b

    for i in range(start, end + 1):
        answer += i

    return answer
