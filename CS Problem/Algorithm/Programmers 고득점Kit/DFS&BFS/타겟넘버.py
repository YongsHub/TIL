def solution(numbers, target):
    answer = 0
    tmp = []
    result = [0]
    for i in numbers:  # 더하기 빼기를 number개수만큼 트리형식으로 수행한다.
        if len(result) > 0:
            tmp.append(result.pop())
        for j in range(len(tmp)):
            result.append(tmp[j] - i)
            result.append(tmp[j] + i)
        tmp = result
        result = []

    answer = tmp.count(target)
    return answer
