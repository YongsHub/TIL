from itertools import combinations
def solution(number, k):
    answer = ''
    
    lst = list(combinations(number, len(number) - k))
    
    answer = ''.join(max(lst))
    return answer