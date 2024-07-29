### Question: Layered Architecture 어떻게 구성하여 수행

보통 Layered Architecture는

`4 Tiered Layered Architecture`

- Presentation Layer
- Business Layer
- Persistence Layer
- Data Access Layer
  로 구성되어 있다

Presentation Layer: 사용자가 데이터를 전달하기 위해 화면에 정보를 표시하는 것을 주 관심사로 둔다. Presentation Layer 는 비즈니스 로직이 어떻게 수행되는지 알 필요가 없다. 대표적인 구성요소는 View와 Controller

Business Layer: Persistence Layer가 어떻게 데이터를 어디서, 어떻게 가져오는지에 대해 알 필요가 없다. 단순히, 애플리케이션의 비즈니스 로직을 수행하면 된다 - 그리고, 그 결과를 Presentation Layer에게 전달하면 됨

- Spring data JPA를 활용하는 이유 중 하나는 객체지향 패러다임을 유연하게 활용할 수 있다는 점이다. 이를 위해, Business Layer와 Domain Model을 분리하여 Layer를 두었음

구체적으로는 애플리케이션의 비즈니스 로직과 도메인 모델 패턴에서의 로직을 분리하여 더 작은 단위 테스트를 수행할 수 있는 특징이 있음

Persistence Layer: 어플리케이션의 영속성을 구현하기 위해, 데이터 출처와 그 데이터를 가져오고 다루는 것을 주 관심사로 둔다. 대표적인 구성요소는 Repository, DAO 등이 있다. 프로젝트를 수행하며, Reader와 Writer를 통해 계층을 완전히 분리했음

Database Layer: MySQL, MariaDB, PostgreSQL, MongoDB 등 데이터베이스가 위치한 계층을 의미한다.

### 특징

Layers of Isolation: `수직적으로 구성된 격리된 레이어`
각 계층에서의 변경이 다른 레이어에게 코드 변경에 대한 영향을 줄여줄 수 있다.
