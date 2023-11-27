from itertools import combinations


def solution(numbers):
    answer = []
    indexList = [i for i in range(len(numbers))]
    choice = list(combinations(indexList, 2))

    for a, b in choice:
        result = numbers[a] + numbers[b]
        if result not in answer:
            answer.append(result)

    answer.sort()

    return answer
