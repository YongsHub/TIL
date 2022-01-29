def solution(array, commands):
    answer = []
    for command in commands: # 0, 1, 2행을 받아온다.
        i, j, k = command[0], command[1], command[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer