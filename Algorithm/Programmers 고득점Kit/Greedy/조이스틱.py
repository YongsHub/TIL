def solution(name):
    answer = 0
    curIndex = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    _name = ['A' for _ in range(len(name))]
    for i in range(len(name)):
        # 알파벳 인덱스가 0이면 즉 A이면
        _index = alphabet.index(name[i])
        if _index == 0:
            if curIndex == i:
                curIndex -= 1
                answer -= 1
            continue
        else:
            answer += 1
        
        # 알파벳 인덱스가 13 초과이면
        if _index > 13:
            answer += 26 - _index
            curIndex += 1
            
        # 0보다 크고 13이하이면
        elif 0 < _index <= 13:
            answer += _index
            curIndex += 1
            
        
    return answer