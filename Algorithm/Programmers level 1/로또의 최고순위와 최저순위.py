from collections import defaultdict


def solution(lottos, win_nums):
    answer = []
    correct = 0
    high = 6
    zero = 0
    ranking = defaultdict(int)

    for i in range(1, 8):
        if i == 7:
            ranking[high] = 6
        else:
            ranking[high] = i
            high -= 1

    for i in lottos:
        if i in win_nums:
            correct += 1
        elif i == 0:
            zero += 1

    answer.append(ranking[correct + zero])  # 최고순위1
    answer.append(ranking[correct])  # 최저순위

    return answer
