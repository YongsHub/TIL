from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)
arr = [0] * (n + 1)


def func(k):
    if(k == m):
        print(*arr[:m])
        return None

    for i in range(1, n + 1):
        if visited[i] is False:
            arr[k] = i
            visited[i] = True
            func(k + 1)
            visited[i] = False


func(0)

# lst = list(permutations(list(i for i in range(1, n + 1)), m))
# for tup in lst:
#     print(*tup)
