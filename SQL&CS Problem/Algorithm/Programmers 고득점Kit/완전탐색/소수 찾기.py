from itertools import permutations

def isPrime(number):
    if number <= 2:
        if number == 2:
            return True
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True
        
        
        
        
def solution(numbers):
    answer = 0
    lst = [x for x in numbers]
    cases = []
    result = []
    for i in range(len(lst)):
        cases += list(permutations(lst, i + 1))
    
    for i in cases:
        strNum = ''
        if i[0] == '0':
            i = i[1:]
            if not i:
                continue
        for j in i:
            strNum += j
        if int(strNum) in result:
            continue
        else:
            result.append(int(strNum))
    
    for number in result:
        if isPrime(number):
            answer += 1
            
    
    return answer