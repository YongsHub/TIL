n, k = map(int, input().split())
array = []

for _ in range(n): # 화폐 종류에 대해 배열에 담는다.
    array.append(int(input()))

d = [10001] * (k + 1) # k원까지에 대해 인덱스로 이용하기 위해서
d[0] = 0 # 0원인 경우 화폐사용 없이 만들 수 있기 때문에 0가지

for i in range(n):
    for j in range(array[i], k + 1):
        d[j] = min(d[j], d[j - array[i]] + 1) # 점화식에 따른 코드

if d[k] == 10001:
    print(-1)
else:
    print(d[k])