n, m = map(int, input().split())

array = []
for i in range(n): # 화폐 종류에 대해 입력받기
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0 # 0원을 만드는데는 0개의 화폐가 필요
for i in range(n): # 화폐 종류의 갯수
    for j in range(array[i], m + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])