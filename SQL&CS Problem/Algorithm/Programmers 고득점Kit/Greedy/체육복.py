def solution(n, lost, reserve):
    remove = []
    answer = 0
    for i in lost: # 도난 당했는데, 여유 체육복이 있다면 제거해야 할 목록으로 추가
        if i in reserve:
            remove.append(i)
    
    for i in remove: # 도난 리스트와 여유 리스트에서 제거
        lost.remove(i)
        reserve.remove(i)
    
    for i in range(1, n + 1): # 1명부터 n명까지
        if i not in lost:
            answer += 1
            continue
        
        if i - 1 in reserve: # 앞의 학생이 여벌이 있다면
            reserve.remove(i - 1)
            answer += 1
        elif i + 1 in reserve: # 뒤의 학생이 여벌이 있다면
            reserve.remove(i + 1)
            answer += 1
        
    return answer