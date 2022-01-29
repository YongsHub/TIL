def solution(numbers):
    length = 0
    for i in numbers:
        length += len(str(i))
    
    max_num = 0
    while numbers:
        currentNum = 0
        for i in numbers:
            check = []
            num_length = length - len(str(i))
            check.append(i)
            max_array = check + [0] * num_length
            checkNumber = ''
            for x in max_array:
                checkNumber += str(x)
            
            if int(checkNumber) > currentNum:
                currentNum = int(checkNumber)
                max_len = len(str(i))
                remove_num = i
        numbers.remove(remove_num)
        length -= max_len
        max_num += currentNum
    
    answer = ''
    for x in str(max_num):
        answer += str(x)
        
    
    return answer