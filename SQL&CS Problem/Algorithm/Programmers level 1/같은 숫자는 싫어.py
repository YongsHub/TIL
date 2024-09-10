def solution(arr):
    answer = []
    current = ' '
    for i in arr:
        if current != i:
            answer.append(i)
            current = i
    return answer
