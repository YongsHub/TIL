## Spring 핵심 이해

Spring에서는 Application Context를 IoC 컨테이너라 하기도 하고, 간단히 스프링 컨테이너라고도 함
더하여, 빈 팩토리라고 부를 수도 있음.

애플리케이션 컨텍스트는 Application Context Interface를 구현하는데 Application Context는 BeanFactory 인터페이스를 상속했으므로 일종의 빈 팩토리라고 부를 수 있는 것.

### Bean

---

빈 또는 빈 오브젝트는 스프링이 IoC 방식으로 관리하는 오브젝트
라는 뜻임
주의할 점은 스프링을 사용하는 애플리케이션에서 만들어지는 모든 오브젝트가 다 빈은 아니라는 사실

### configuration metadata

---

Spring의 metadata는 애플리케이션 컨텍스트 또는 빈 패토리가 IoC를 적용하기 위해 사용하는 메타 정보를 의미
실제로 메타데이터는 컨테이너에 어떤 기능을 세팅하거나 조정하는 경우에도 사용하지만, IoC 컨테이너에 의해 관리되는 애플리케이션 오브젝트를 생성하고 구성할 때 사용

### Singleton Pattern

싱글톤 패턴의 한계를 이해하고 Spring의 Singleton Registry를 이해하는 것이 좋다고 생각된다.

| 자바에서 싱글톤을 구현하는 방법은 보통 이렇다

- 클래스 밖에서는 오브젝트를 생성하지 못하도록 생성자를 private으로 만듬
- 생성된 싱글톤 오브젝트를 저장할 수 있는 자신과 같은 타입의 스태틱 필드를 정의

* 스태틱 팩토리 메서드인 getInstance()를 만들고 이 메서드가 최초로 호출되는 시점에서 한번만 오브젝트가 만들어지게 함
* 한번 오브젝트가 만들어지고 난 후에는 getInstance() 메서드를 통해 이미 만들어져 스태틱 필드에 저장해둔 오브젝트를 넘겨줌

---

### 한계

- private 생성자를 갖고 있기에 상속할 수 없음
- 싱글톤은 테스트하기가 힘들다
- 서버환경에서는 싱글톤이 하나만 만들어지는 것을 보장하지 못함

| 따라서, 스프링은 직접 싱글톤 형태의 오브젝트를 만들고 관리하는 기능을 제공함. 그것이 바로 싱글톤 레지스트리이다. 싱글톤 레지스트리의 장점은 평범한 자바 클래스를 싱글톤으로 활용하게 해준다는 점

| 스프링 싱글톤 레지스트리 덕분에 싱글톤 방식으로 사용될 애플리케이션 클래스라도 public 생성자를 가질 수 있음

**_가장 중요_**

싱글톤 패턴과 달리 스프링이 지지하는 객체지향적인 설계방식과 원칙, 디자인 패턴등을 적용하는데 아무런 제약이 없음

따라서, 스프링은 IoC 컨테이너일 뿐만 아니라, 고전적인 싱글톤 패턴을 대신해서 싱글톤을 만들고 관리해주는 싱글톤 레지스트리라는 점!

---
