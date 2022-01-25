n = int(input())

count = 0
for time in range(0,n+1):
  for min in range(0,60):
    for sec in range(0,60):
      if '3' in str(sec) + str(min) + str(time):
        count += 1

print(count)

# 문자열을 더해서 '3' 이 있는지 확인하는 아이디어를 떠올리자!