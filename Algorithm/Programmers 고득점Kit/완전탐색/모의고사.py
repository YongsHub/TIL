def solution(answers):
    lst = [[1, 2, 3, 4, 5] * 2000, [2, 1, 2, 3, 2, 4, 2, 5] * 1250, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000]
    answer = []
    result = 0
    compareNum = 0
    
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == lst[i][j]:
                result += 1
        if result > compareNum:
            answer = []
            answer.append(i + 1)
            compareNum = result
        elif compareNum == result:
            answer.append(i + 1)
        result = 0
        
    answer.sort()
    return answer