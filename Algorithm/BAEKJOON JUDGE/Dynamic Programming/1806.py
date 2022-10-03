N, S = map(int,input().split())
nums = list(map(int,input().split()))
start, end = 0, 0
s = nums[0]
ans = 100001
 
while True:
    if s >= S:
        s -= nums[start]
        ans = min(ans, end - start + 1)
        start += 1
    else:
        end += 1
        if end == N:
            break
        s += nums[end]
 
print(0) if ans == 100001 else print(ans)
