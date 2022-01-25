garden = [[0] * 8 for i in range(8)] # 8 * 8 체스판
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]
location = [0, 0] # x축 y축
input = input()
move = [(-1,2),(1,2),(-1,-2),(1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
# 체스판 초기화
for i in range(8):
  for j in range(8):
    if str(row[i]) == input[1] and column[j] == input[0]:
      location[0] = i
      location[1] = j
    garden[i][j] = (row[i],column[j])

count = 0
for check in move:
  dx = location[0] + check[0]
  dy = location[1] + check[1]
  if 0 <= dx <= 8 and 0 <= dy <= 8:
    count += 1

print(count)