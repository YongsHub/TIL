def solution(n, arr1, arr2):
    answer = []
    for first, second in zip(arr1, arr2):
        binary1 = bin(first)[2:]
        binary2 = bin(second)[2:]
        length1 = len(binary1)
        length2 = len(binary2)
        answer.append(((n - length1) * "0" + binary1,
                      (n - length2) * "0" + binary2))

    for index, value in enumerate(answer):
        arr1 = value[0]
        arr2 = value[1]
        newArr = ""
        for i, j in zip(arr1, arr2):
            if i == '1' or j == '1':
                newArr += '#'
            else:
                newArr += " "
        answer[index] = newArr

    return answer
