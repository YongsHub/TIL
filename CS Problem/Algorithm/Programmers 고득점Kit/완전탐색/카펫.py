def solution(brown, yellow):
    answer = []
    
    
    for i in range(3, 1249): # 행
        for j in range(3, 2500): # 열
            col = (j * 2) + ((i - 2) * 2) # brown은 (열 길이 * 2) + (행 - 2) * 2 
            row = (i * j) - col # Yellow는 행 * 열 - brown갯수
            if col == brown and row == yellow:
                answer = [j, i]
                return answer
                
            
    return answer