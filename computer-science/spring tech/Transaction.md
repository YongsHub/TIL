### Transactional

- 트랜잭션 readOnly = true를 사용할 때, 성능상 이점
  readOnly = true를 설정하게 되면 JPA는 해당 트랜잭션 내에서 조회하는 Entity는 조회용임을 인식하고 변경 감지를 위한 Snapshot을 따로 보관하지 않으므로 메모리가 절약되는 성능상 이점 역시 존재한다.

- 최적화
  트랜잭션은 가능한 짧은 범위로

- OSIV

- 등등..
