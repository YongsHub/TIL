## 객체지향 패러다임: 협력, 책임, 역할

1. 객체도 사회적 동물이다. 독립적인 존재가 아니다
2. 객체지향 세계에서 객체는 자아를 가짐
   - 실제 세계에서의 수동적인 존재를 객체지향 세계에 객체로 구현되면 능동적인 존재가 됨
3. 객체지향 세계에서는 독점은 없다.
   - 객체지향 세계에서 모ㄴ 것을 가지고 있는 객체는 없다.
   - Application의 목표를 달성하기 위해서 필요한 기능을 쪼개서 적절한 객체에 분배하고 객체들 간의 적절한 협력을 만들어 주는 것이 목표다

- 협력이란?
  Application의 주요 기능을 구현하기 위해서 `작은 단위로 쪼개진 기능`을 설명하는 한 줄 요약본
  협력은 객체 간의 상호작용을 통해서 이루어진다.
  객체 간의 협력은 메시지를 통해서만 가능하다.

- 책임이란?
  협력에 참여하기 위해서 객체가 맡고(=책임지고)있는 전체 기능 정의서

- 역할이란?
  동일한 책임을 수행하는 객체의 집합체. 동일한 책임을 수행하는 객체가 여러 개 있을 경우, 협력을 개별적으로 만들지 않는다. 동일한 책임을 수행하는 객체들을 대표할 수 있는 특별한 이름을 부여하고 그것들을 슬롯 형태로 관리하면 동적으로 적절한 객체로 결합한다.

## 의존성: 객체의 영원한 친구

A객체가 B객체에게 "give me the money"라는 문맥을 가지는 메시지를 보냈을 때 B객체가 A객체가 보낸 메시지를 처리할 수 있다라는 사실을 `알고 있는 지식(정보)`를 의존성이라고 말한다.

의존성 관계가 높을수록 `강한 결합도`, 낮을수록 `느슨한 결합도`로 표현함

### 올바른 의존성 관계 형성

- Constructor 함수를 통한 의존 관계 형성
  - 왜? 생성자 함수를 통해 의존성 관계 형성을 하나요?에 대해 답할 수 있는가?
- Parameter of Method를 통한 의존 관계 형성
- Setter 함수를 통한 의존 관계 형성

### 변경을 방해하는 의존성 관계

Constructor 함수 의존 관계 형성에서 new 키워드를 통해 관계를 맺는것은 피해야 한다

### 응집도와 결합도

응집도는 클래스에 포함된 내부 요소가 하나의 책임과 연관된 정도와 책임을 수행하기 위해서 필요한 기능들이 하나의 연관 클래스에 잘 정의가 되어 있는지를 알려주는 척도이다.

응집도가 높다고 해서 결합도가 높거나 낮음을 판단할 수는 없다.

하지만, 하나의 책임이 여러 개의 클래스들로 분산 되어 있고 분산된 클래스를 의존하는 객체들이 분산된 클래스의 내부 구현까지 알고 있다면 낮은 응집도와 높은 결합도를 가지는 구조가 될 것이다.

캡슐화를 통한 내부 구현을 숨기는 형태를 가진다면 아무리 많은 클래스가 해당 클래스를 의존한다고 하더라도 높은 응집도와 낮은 결합도를 가지고 있는 클래스라고 이야기 할 수 있지 않을까?

### 상속; 재사용의 함정

부모 클래스와 자식 클래스 간에 강한 결합이 생긴다.
자식 클래스에서 호출하는 부모 클래스의 함수가 수정되거나 부모 클래스의 내부 구현이 변경되면 자식 클래스 또한 변경의 영향을 받아 자식클래스 또한 변경을 적용해야 하는 문제가 있다.

우리가 객체지향 이론과 SOLID 규칙을 지키면서 코딩을 하는 이유는 `변경의 유연한 설계`를 하기 위함인데 상속은 이것을 무력하게 만드는 기법이다

### 합성; 유연한 코드로 가는 길

합성의 경우, 기반 클래스에 필요한 기능을 제공하는 외부 객체를 런타임 시점에 적절하게 선택하여 주입하는 구조를 가진다.
그렇기 때문에 합성 관계는 런타임 시점에 결정된다. 그래서 합성은 작은 기능들을 조합해서 다양한 기능을 만들어낼 수 있다.

## 새로운 문법; 람다(Lambda)

클래스 선언 없이 메서드를 정의할 수 있고, 이것을 값(Object)처럼 사용할 수 있는 함수

간결성과 익명 클래스 대체
복잡한 코드를 간결하게 표현함으로써 간결성과 가독성을 높일 수 있는 이점을 가지고 있다.

함수형 인터페이스란, 오직 하나의 추상 메서드를 정의하는 인터페이스다.

람다 표현식으로 함수형 인터페이스의 추상 메서드 구현을 직접 전달할 수 있으므로 전체 표현식을 함수형 인터페이스의 인스턴스로 취급할 수 있다.
