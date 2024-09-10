import sys

input = sys.stdin.readline
# 2 <= N <= 200,000, 2 <= C <= N
N, C = map(int, input().split())
locations = [int(input().rstrip()) for _ in range(N)]
locations.sort()
answer = 0
start = 1 # 시작 값
end = locations[-1] - locations[0] # 마지막 값 - 시작 값
def binary_search(start, end, N):
    answer = 1

    while start <= end:
        middle = (start + end) // 2
        current = locations[0]
        count = 1

        for i in range(1, N):
            if locations[i] >= current + middle:
                count += 1
                current = locations[i]

        if count >= C:
            start = middle + 1
            answer = middle # 개수가 count면 정답은 middle이 된다.
        else:
            end = middle - 1
    return answer


answer = binary_search(start, end, N)
print(answer)



