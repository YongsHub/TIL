def solution(numbers, hand):
    answer = []
    left = '*'
    right = '#'
    middle = [2, 5, 8, 0]
    middleMap = {0: [3, 2, 1, 0], 1: [1, 2, 3, 4], 2: [0, 1, 2, 3], 3: [1, 2, 3, 4], 4: [2, 1, 2, 3], 5: [1, 0, 1, 2], 6: [
        2, 1, 2, 3], 7: [3, 2, 1, 2], 8: [2, 1, 0, 1], 9: [3, 2, 1, 2], '*': [4, 3, 2, 1], '#': [4, 3, 2, 1]}
    # hand값을 R or L로 바꾸기 위해
    if hand == "right":
        hand = 'R'
    else:
        hand = 'L'

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer.append('L')
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer.append('R')
        else:
            index = middle.index(i)
            distanceL = middleMap[left][index]
            distanceR = middleMap[right][index]
            #print('왼손에서 거리:', distanceL, '오른손에서 거리:',distanceR)
            if distanceL == distanceR:
                answer.append(hand)
                if hand == 'R':
                    right = i
                else:
                    left = i
            elif distanceL < distanceR:
                answer.append('L')
                left = i
            else:
                answer.append('R')
                right = i

    return ''.join(answer)
