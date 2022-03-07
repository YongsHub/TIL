def solution(N, stages):
    answer = []

    for i in range(1, N + 1):
        count = 0
        fail = 0
        for j in stages:
            if j >= i:
                count += 1
            if j == i:
                fail += 1

        if count == 0:
            answer.append((0, i))
        else:
            answer.append((fail / count, i))

    answer.sort(key=lambda x: (-x[0], x[1]))

    for index, value in enumerate(answer):
        answer[index] = value[1]
    return answer
