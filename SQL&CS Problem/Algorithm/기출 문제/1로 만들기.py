n = int(input())

d = [0] * 30001 # 1 <= n <= 30000

for i in range(2, n + 1):
  d[i] = d[i - 1] + 1 # 1을 뺀 경우는 전부 가능하기 때문에

  if i % 2 == 0: # 2로 나누어 떨어진다면
    d[i] = min(d[i], d[i // 2] + 1) # 1을 더하는 이유는 2로 나눈 횟수 때문에
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)


print(d[n])