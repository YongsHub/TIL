def solution(sizes):
    answer = [0, 0]

    for x, y in sizes:
        if x >= y:
            bigSize = x
            smallSize = y
        else:
            bigSize = y
            smallSize = x

        maxLength = max(answer)
        if bigSize > maxLength:
            index = answer.index(maxLength)
            if index == 1:
                anotherIndex = 0
            else:
                anotherIndex = 1
            answer[index] = bigSize
            if answer[anotherIndex] < smallSize:
                answer[anotherIndex] = smallSize
        else:
            minLength = min(answer)
            if minLength < smallSize:
                index = answer.index(minLength)
                answer[index] = smallSize

    width, height = answer[0], answer[1]
    return width * height
