def solution(p, i=0, answer=[0]):
    if i == 0:
        answer = [0] * len(p)
    # i == n이라면 종료
    print('i', i)
    if i == len(p) - 1:
        return answer
    minValue = 10 ** 9
    j = len(p) - 1

    for idx, value in enumerate(p):
        # 현재의 minValue보다 작다면
        if idx < i:
            continue
        if minValue > value:
            minValue = value
            j = idx

    if i != j:  # i와 j가 다르다면
        p[i], p[j] = p[j], p[i]
        answer[i] += 1
        answer[j] += 1
    i = i + 1
    print(p)
    # 재귀로 함수 호출
    solution(p, i, answer)

    return answer


answer = solution([2, 5, 3, 1, 4])
print(answer)
