# BFS

[참고 내용 링크](https://youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)<br>
Breadth First Search 알고리즘은 너비 우선 탐색이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데, BFS는 그 반대이다.

- 📌 BFS 구현에서는 선입 선출 방식인 큐 자료구조를 이용하는 것이 정석이다.

인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다.

## 🎈 알고리즘 동작 순서

- 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
- 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
- 3. 2번의 과정을 더 이상 수행할 수 없을때까지 반복한다.

```
# BFS 예제
from collections import deque
# BFS 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 활용
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)
```
