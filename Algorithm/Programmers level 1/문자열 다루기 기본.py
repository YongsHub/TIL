def solution(s):
    answer = True
    count = len(s)
    for i in s:
        if i.isnumeric() == False:  # 정수인지 확인하는 함수
            return False

    if (count == 4 or count == 6) and answer == True:
        return answer
    else:
        return False
