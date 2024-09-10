n = int(input())
datas = list(input().split())

# R 과 L은 열의 값 +1 또는 -1 U,D은 행의 값 +1 또는 - 1

map = [[0] * n for _ in range(0,n)]

for i in range(0, n):
  for j in range(0, n):
    map[i][j] = (i+1, j+1)

row = 0
col = 0

for location in datas:
  if location == 'R' and 0 <= col < n - 1:
    col += 1
  elif location == 'L' and 0 < col <= n - 1:
    col -= 1
  elif location == 'U' and 0 < row <= n - 1:
    row -= 1
  elif location == 'D' and 0<= row < n - 1:
    row += 1
  else:
    pass

print(map[row][col][0], map[row][col][1])