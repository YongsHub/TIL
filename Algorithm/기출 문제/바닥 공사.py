n = int(input())

d = [0] * 1001

d[1] = 1 # 가로가 1일 때 경우의 수
d[2] = 3 # 가로가 2일 때 경우의 수

for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2] * 2


print(d[n])