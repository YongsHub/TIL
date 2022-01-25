n, m = map(int, input().split()) # N,M크기의 맵 생성
x, y, direct = map(int, input().split()) # (x,y)에 direct를 바라보고 있는 캐릭터
maps = [[0] * m for _ in range(n)]
past_location = [] # 갔던 곳 위치를 저장하기 위한 리스트
count = 1
past_location.append((x,y))

for i in range(n):
    data = list(map(int, input().split()))
    maps[i] = data


def check(x, y): # 배열 범위 내에 있고 바다가 아닌지 확인하기 위해
  global n, m, maps
  if 0<=x<=n and 0<=y<=m and maps[x][y] != 1:
    return 1
  else:
    return 0

  
def move(): # 움직이는 함수
  direction = [0, 1, 2, 3]
  dx = [-1, 0, 1, 0] # 북, 동, 남, 서
  dy = [0, 1, 0, -1] # 북, 동, 남, 서
  global count, past_location, x, y, direct
  num = direct
  for _ in range(4):
    num -= 1 # 반시계 방향 회전
    # 움직여보고
    move_x = x + dx[num]
    move_y = y + dy[num]
    #갈수 있는지 체크
    if (move_x, move_y) not in past_location:
      if check(move_x, move_y) == False:
        continue
      count += 1
      x = move_x
      y = move_y
      past_location.append((x, y)) # 가본 장소로 추가
      direct = direction[num] # 방향 수정
      return 1
  move_x = x - dx[direct]
  move_y = y - dy[direct]
  if check(move_x, move_y) == True:
    x = move_x
    y = move_y
    return 1
  else: return 0
      
    
     
while True:
  prove = move()
  if prove == False:
    break

print(count)