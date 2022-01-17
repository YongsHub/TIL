# Queue와 Stack을 이용한 문제를 해결할 때 사용하기 좋은 TIP

## <span style="color:yellow">Queue</span>

- Queue는 자료구조의 스택과 반대의 구조로써, FIFO의 형태를 가지게 됩니다. 즉, 먼저 들어온 데이터가 가장 먼저 나가는 구조를 말합니다.

<span style="color:yellow">관련 용어</span>

> Enqueue는 큐 맨 뒤에 데이터를 추가 <br>Dequeue는 큐 맨 앞쪽의 데이터를 삭제

> 자바에서는 스택을 클래스로 구현하여 제공하지만 큐는 `Queue인터페이스만 있고 별도의 클래스가 없습니다.` 따라서 Queue인터페이스를 구현한 클래스들을 사용해야 함

# ❗️❗️ArrayList와 LinkedList의 차이를 알아보자

* [참고 Blog](https://devlog-wjdrbs96.tistory.com/64)

### <span style="color:yellow">ArrayList</span>

📌 ArrayList는 중복을 허용하고 순서를 유지하며 인덱스로 원소들을 관리하기 때문에 배열과 상당히 유사하다. 하지만 배열은 크기가 지정되면 고정되지만 ArrayList는 클래스이기 때문에 배열을 추가, 삭제 할 수 있는 메소들도 존재합니다.

📌 `하지만 추가 했을 때 배열이 동적으로 늘어나는 것이 아니라 용량이 꽉 찼을 경우 더 큰 용량의 배열을 만들어 옮기는 작업을 하게 된다`

### ArrayList API

- add() : 원소를 마지막에 추가하기
- add(int index, E element) : 원소를 지정된 위치에 추가하기
  📝 배열에 마지막이 아닌 처음, 중간에 데이터를 넣어야한다면 기존 데이터들을 한칸씩 미뤄서 공간을 만드는 작업이 필요하다. 이 때 여기서 시간 복잡도가 증가하게 됨을 유의하자
- remove(int index) : 원소의 인덱스로 삭제하기
  📝 마지막 원소를 삭제한다면 쉽게 삭제할 수 있지만 중간이나 처음의 원소를 삭제하게 되면 빈 공간을 다시 채우는 과정에서 시간 복잡도가 증가한다.
- get(int index) : 배열은 인덱스에 해당하는 원소를 O(1)에 찾아올 수 있기에 탐색에서 매우 유리하다.

### <span style="color:yellow">LinkedList</span>

📌 LinkedList는 내부적으로 양방향의 연결 리스트로 구성되어 있어서 참조하려는 원소에 따라 처음부터 순방향으로 또는 역순으로 순회할 수 있습니다.

### LinkedList API
* add(E element) : 원소를 마지막에 추가하기
* add(int index, E element): 원소를 지정된 위치에 추가하기

* remove(int index) : 원소를 삭제하기

* get(int index) : 인덱스에 해당하는 원소 찾아오기
📝 LinkedList는 ArrayList와 다르게 인덱스를 통해서 검색을 하는 것이 아니라 Head에서 부터 해당 원소까지 검색해야 하기 때문에 O(n)에 찾을 수 있습니다.
