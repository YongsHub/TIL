from itertools import product

n = int(input())
input_lst = []
for _ in range(n):
  input_lst.append(int(input()))
  
lst = [1, 2, 3]
result = []
for i in range(1, 11):
  result += list(map(sum, product(lst, repeat = i)))

  
for i in input_lst:
  count = 0
  for j in result:
    if i == j:
      count += 1
  print(count)