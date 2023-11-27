from itertools import combinations_with_replacement
n = int(input())
input_lst = []
for _ in range(n):
  input_lst.append(int(input()))


def triangle(n):
  result = (n * (n + 1)) / 2
  return result


n = 1
lst = []
while n <= 1000:
  result = triangle(n)
  if result <= 1000:
    lst.append(int(result))
  else:
    break
  n += 1

result = list(map(lambda x: x[0] + x[1] + x[2], combinations_with_replacement(lst, 3)))


for i in input_lst:
  if i in result:
    print(1)
  else:
    print(0)