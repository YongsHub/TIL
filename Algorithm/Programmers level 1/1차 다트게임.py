def solution(dartResult):
    answer = []
    threeShots = []
    define = {'S': 1, 'D': 2, 'T': 3}
    shot = ""

    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            threeShots.append(shot)
            shot = ""
            threeShots.append(dartResult[i])
        else:
            if dartResult[i] != '#' and dartResult[i] != '*':
                shot += dartResult[i]
            else:
                threeShots.append(dartResult[i])

    for i in threeShots:
        index = len(answer) - 1

        if i.isalpha():
            answer[index] = answer[index] ** define[i]
        elif i == '#':
            answer[index] = -answer[index]
        elif i == '*':
            if index == 0:
                answer[index] = answer[index] * 2
            else:
                answer[index] = answer[index] * 2
                answer[index - 1] = answer[index - 1] * 2
        else:
            answer.append(int(i))

    return sum(answer)
