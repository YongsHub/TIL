from collections import defaultdict


def solution(msg):
    answer = []
    dictionary = defaultdict(int)
    i = 1
    for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dictionary[alpha] = i
        i += 1

    for w in range(len(msg)):
        Input = ''
        Input += msg[w]
        if Input in dictionary:
            answer.append(dictionary[Input])
            if w < len(msg) - 2:
                prev = Input
                prev += msg[w + 1]
                dictionary[prev] = i
                i += 1

    return answer
