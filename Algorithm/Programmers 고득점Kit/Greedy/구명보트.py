from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people)) # 오름차순으로 정렬
    
    while deq:
        if len(deq) == 1: # 한개가 남았다면 보트 갯수 추가하면 break
            answer += 1
            break
        
        if deq[0] + deq[-1] <= limit: # 정렬된 deque에서 첫 번째 요소와 마지막 요소가 limit보다 작거나 같으면
            deq.popleft()
            deq.pop()
            answer += 1
            continue
        else:
            deq.pop()
        
        answer += 1
    return answer