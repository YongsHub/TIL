n = int(input()) #전자부품 갯수 입력
types = list(map(int, input().split()))
m = int(input())
m_types = list(map(int, input().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
    
  mid = (start + end) // 2 # 중간 지점 
  if array[mid] == target:
    return mid
  elif array[mid] < target:
    return binary_search(array, target, mid + 1, end)
  else:
    return binary_search(array, target, start, mid - 1)


types.sort()

for i in m_types:
  result = binary_search(types, i, 0, len(types) - 1)
  if result == None:
    print('no', end=' ')
  else:
    print('yes', end=' ')