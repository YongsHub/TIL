def substract(n):
  n -= 1
  return n


def divide(n, k):
  n /= k
  return n

  
n, k = map(int, input().split()) 

count = 0
result = n
while True:
  if result == 1:
    break

  if result % k == 0:
    result = divide(result, k)
    count += 1
  else:
    result = substract(result)
    count += 1

print(count)