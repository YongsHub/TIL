n = int(input())

for i in range(1, n + 1):
  check = list(map(int, str(i)))
  result = i + sum(check)
  if result == n:
    print(i)
    break
  if i == n:
    print(0)