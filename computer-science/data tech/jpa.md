### Spring Data JPA

Spring 프레임워크와 JPA라는 기반위에 JPA를 편리하게 사용하도록 도와주는 기술

- 기본적인 CRUD API에 대해 인터페이스로 제공
  Java Persistent API를 기반으로 레파지토리를 쉽게 사용할 수 있게 만들어졌음

특징
실행 가능한 단순한 쿼리들에 대해 많은 보일러플레이트 코드들이 쓰여져 있음
예를 들어, 페이지네이션, auditing 등 다양한 필요 옵션들

Spring Data Repository 추상화에서 중앙 인터페이스는 Repository이다.
여기서 CRUDRepository나 ListCrudRepository 인터페이스는 정교한 CRUD functionality를 제공함

선택이 아니라 `필수`

JPA를 활용한 Domain Model Pattern 활용

- JPA의 cascade 대표적으로 활용
- 이외에도 Entity, Table, Embedded 등등 구현 기술이 있는데 구현하고 있는 기능들이 아직 단순한 기능들이 많아서 이론적으로 미리 공부를 해두고 도메인이 고도화됨에 따라 리팩토링이 필요할 것으로 보임

---

### JPA 이점

- Dirty Check

- Lazy Loading

- 객체지향 패러다임으로 가는 도메인 모델 패턴을 활용할 수 있음

- 영속성 Context를 활용한 1차 캐시

### Collection Fetch Join 페이징

ManyToOne이나 OneToOne은 fetch join시 데이터 중복 문제가 발생하지 않아서 페이징에 큰 문제가 없음
하지만 OneToMany같이 데이터베이스에서 발생한 쿼리가 특정 Entity에 대해 데이터 중복이 발생하게 됨

- 이를 해결하는 법: select distinct를 활용하면 Hibernate 엔진에서 중복을 제거해줌

`그렇다면 페이징은 어떻게 해결할 것인가?`

중복의 데이터를 해결하기 위해서는

1. 쿼리 분배 - 대상 Entity 페이징으로 조회 + 다음 컬렉션들 In 쿼리
2. Lazy Loading으로 대상 Entity 페이징 + hibernates_batch_size 설정으로 자동으로 in 쿼리
