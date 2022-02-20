def solution(numbers, hand):
    answer = ''
    # Keypad Coordinate: 0123456789*(10)#(11)
    distance = [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [
        1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [2, 3]]

    # initial position
    left = 10
    right = 11

    for i in numbers:
        # LEFT HAND
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        # RIGHT HAND
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        # DISTACNE COMPARISON
        else:
            ldist = abs(distance[i][0] - distance[left][0]) + \
                abs(distance[i][1] - distance[left][1])
            rdist = abs(distance[i][0] - distance[right][0]) + \
                abs(distance[i][1] - distance[right][1])
            if ldist > rdist:
                answer += 'R'
                right = i
            elif ldist < rdist:
                answer += 'L'
                left = i
            # distance equals
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer
