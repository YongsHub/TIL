def solution(name):
    answer = 0
    max_move = len(name) - 1
    
    while name[max_move] == 'A' and max_move > 0:
        max_move -= 1
    
    if max_move < 0:
        return answer
    
    for idx, value in enumerate(name):
        up_down = min(ord(value) - ord('A'), ord('Z') - ord(value) + 1) # 위 아래 움직이는 최솟값
        answer += up_down
        
        next_index = idx + 1 # 현재 인덱스에서의 다음 인덱스 값
        
        count = 0
        while next_index < len(name) and name[next_index] == 'A':
            count += 1
            next_index += 1
        
        if idx + 1 <= count: # 연속된 A의 갯수보다 앞의 갯수가 작거나 같을때
            max_move = min(max_move, idx + idx + len(name[idx + 1:]) - count)
    return answer + max_move