# Queue와 Stack을 이용한 문제를 해결할 때 사용하기 좋은 TIP

## <span style="color:yellow">Queue</span>

- Queue는 자료구조의 스택과 반대의 구조로써, FIFO의 형태를 가지게 됩니다. 즉, 먼저 들어온 데이터가 가장 먼저 나가는 구조를 말합니다.

<span style="color:yellow">관련 용어</span>

> Enqueue는 큐 맨 뒤에 데이터를 추가 <br>Dequeue는 큐 맨 앞쪽의 데이터를 삭제

> 자바에서는 스택을 클래스로 구현하여 제공하지만 큐는 `Queue인터페이스만 있고 별도의 클래스가 없습니다.` 따라서 Queue인터페이스를 구현한 클래스들을 사용해야 함

# ❗️❗️ArrayList와 LinkedList의 차이를 알아보자

- [참고 Blog](https://devlog-wjdrbs96.tistory.com/64)

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

- add(E element) : 원소를 마지막에 추가하기
- add(int index, E element): 원소를 지정된 위치에 추가하기

- remove(int index) : 원소를 삭제하기

- get(int index) : 인덱스에 해당하는 원소 찾아오기
  📝 LinkedList는 ArrayList와 다르게 인덱스를 통해서 검색을 하는 것이 아니라 Head에서 부터 해당 원소까지 검색해야 하기 때문에 O(n)에 찾을 수 있습니다.

# 문제를 해결하기 위한 사고력

## 📌 큐를 활용하기 위한 관련된 자료형 선언 및 메서드

- 📝 Queue<Integer> q = new LinkedList<>(); : 링크드리스트를 활용한 큐
- 📌 q.offer(); 큐에 데이터 삽입 📌 q.poll(); 맨 앞 데이터 삭제 📌 q.peek(); 맨 앞 요소 값 확인
- 📌 q.length or q.size();

## Java는 객체 지향적으로 접근이 가능하다.

- 클래스 내 inner class를 생성하여 객체로서 요소들을 생각할 수 있다.

<br><br>

## 📌 Stack의 특징 및 관련 메서드

> 먼저 들어간 자료가 나중에 나오는 Last in First Out 구조이다.<br>시스템 해킹에서 버퍼오버플로우 취약점을 이용한 공격을 할 때 스택 메모리의 영역에서 함<br>인터럽트 처리, 수식의 계산, 서브루틴의 복귀 번지 저장에 쓰인다.<br>그래프 깊이 우선 탐색에서 사용.<br>재귀적 함수 호출에서 사용

### Method

- push() : 데이터 삽입, pop():맨 위 데이터 삭제, peek() : 맨 위의 값을 출력하고 싶을 때 사용

그 외의 메서드

- size(), empty() : true or false, contains(1) : stack에 1이 있는지 check(있다면 true)

# Hash에 대해 공부

<span style="color : yellow">해시란? 데이터를 다루는 기법 중 하나로, 특히 Hash는 검색과 저장에서 아주 우수한 성능을 보여 많이 쓰임새를 얻고 있습니다.</span>

- 🔴 Hash의 핵심은 KEY와 VALUE 입니다. Key와 Value가 한 쌍으로 존재하며, 우리는 Key와 Value의 쌍을 Hash Table이라고 부릅니다. Key는 Hash에서 매핑할 때 사용하는 인덱스라고 생각하면 된다. Key는 절대로 중복되지 않는다는 특징을 가지고 있다.
- ❗️ 만약 같은 Key에 값을 넣으면 이전 값은 사라지고 나중에 들어온 값만 남는다. Value는 Key로 매핑했을 때 나오는 값을 말한다.

## Hash가 제시된 이유가 무엇일까?

- ArrayList와 LinkedList의 한계를 극복하기 위해서 제시된 방법이라고 생각하면 된다.

<span style="color:yellow">데이터 추가/삭제 시, 기존 데이터를 밀어내거나 당기는 작업이 필요하지 않음, 특별한 알고리즘을 이용하여 데이터와 연관된 고유 숫자를 만들어서 인덱스로 사용</span>

- Hash Table에서 key를 테이블에 저장할 때, Key값을 hash method를 이용해 계산을 수행한 후, 그 결과값을 배열의 인덱스로 사용하여 저장한다. 여기서 key값을 계산하는 것이 hash method이다.

📌 자바에서는 Object클래스의 hashcode() 메서드를 이용하여 모든 객체의 HashCode를 쉽게 구함.

### HashMap 생성

- HashMap<String , Integer> map = new HashMap<>();

### HashMap 관련 메서드

- put(K key, V value);
  map.put("숫자",1);
- putAll();
  하나의 Map을 또 다른 Map에 추가할 때, 사용
- remove(Object Key);
  하나의 Key를 입력하여 데이터 삭제
- size(); 개수 반환
- values(); 저장된 요소들을 컬렉션 형태로 출력
- isEmpty();
- get(Object Key);
- clear();
- clone();
- containsKey(Object Key);
- containsValue(Object value);
- entrySet();

## HashMap 클래스 forEach를 활용하여 반복문을 실행하는 방법

```
HashMap<String,Integer> map = new HashMap<>();
for(Map.Entry<String,Integer> entry : map.entrySet()){
    entry.getValue() or entry.getKey() 를 활용하면 된다.
}
```

## 📌 알아두면 유용한 Method

- getOrDefault(Object key, V DefaultValue)
- 매개 변수 : 이 메서드는 두 개의 매개 변수를 허용하는데, key는 값을 가져와야 하는 요소의 키입니다. defaultValue는 지정된 키로 매핑된 값이 없는 경우 반환되어야 하는 기본 값.

<span style="color : yellow"> 반환 겂은 찾는 key가 존재한다면 해당 key에 매핑되어 있는 값을 반환하고, 그렇지 않으면 디폴트 값이 반환된다는 것이다.</span>

## 배열 정렬

- 오름차순 : Arrays.sort(array) 내림차순 : Arrays.sort(list, Collections.reverseOrder());

## ArrayList 정렬

- Collections.sort(arrayList); 내림차순 : Collections.sort(arrayList, Collections.reverseOrder());

# Comparable 인터페이스를 활용한 객체 내 변수들 비교

```
# 예시
class Music implements Comparable<music>{
  int uniqueNumber;
  int playingCount;

  @Override
  public int compareTo(Music music){
    if(music.playingCount < playingCount){
      return 1;
    }else{
      return -1;
    }
  }
}
```
