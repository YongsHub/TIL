n, m = map(int, input().split()) 

data = [[0] * m for _ in range(0,n)]

num = -1
for i in data:
  col = list(map(int, input().split()))
  i = col
  x = min(i)
  if num <= x:
    num = x

print(num)