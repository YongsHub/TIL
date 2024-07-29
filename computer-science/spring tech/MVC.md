### Spring Web Filter

Filter는 스프링의 독자적인 기능이 아니라 DispatherServlet 으로의 요청 전 \* 후에 동작하여 사용자의 요청이나 응답의 최전방에 존재함

---

### Interceptor

Interceptor는 Filter와 크게 다른 차이점은 Context가 다르다는 것이다. 인터셉터는 Spring Container 영역에 존재하여 DispatcherServlet이 실행이 되고 나서 호출된다.

따라서, Spring Container로부터 Bean을 주입받을 수 있다는 특징이 있음: 인증/인가 등과 같은 공통 작업.

---

### Spring DispatcherServlet

첫번째로, Client로부터 Web Request가 왔을 때, 각 요청에 따라 각기 다른 Servlet이 Servlet Container에서 생성되었는데, 이와 관련하여 설정하는 것들의 공통적인 특징이 발견되었음. 이러한 부분을 FrontController 한가지로 공통적인 부분을 처리하는 것으로 시작함. ->
공통적인 부분: 웹 보안, 다국어 처리... 등등

DispatcherServlet은
이와 같이 FrontController와 같은 역할을 대신 수행하는 것으로 정의할 수 있음. Spring MVC에서 제공하는데 이를 활용. 단, Spring Container를 대표하는 interface인 WebApplicationContext를 필요로 하고 해당 Container에 등록된 싱글톤 객체인 Bean들을 호출하여 요청을 위임함

---

### Argument Resolver

Spring에서 Resolver의 동작 방식

1. Client Request 요청
2. Dispatcher Servlet에서 해당 요청 처리
3. Client Request에 대한 Handler Mapping
   - 3.1 RequestMapping에 대한 매칭 (RequestMappingHandlerAdapter가 수행)
   - 3.2 Interceptor 처리
   - 3.3 Argument Resolver 처리 <-- Argument Resolver 실행 지점
   - 3.4 Message Converter 처리
4. Controller Method invoke

ArgumentResolver를 사용하면 컨트롤러 메서드의 파라미터 중 특정 조건에 맞는 파라미터가 있다면, 요청에 들어온 값을 이용해 원하는 객체를 만들어 바인딩

---

### IoC 와 DI

DI, IoC 사실 차이점이라기보다 두 가지의 개념이 다른 부분도 있지만 연관 관계가 있다라고 표현하고 싶습니다. DI는 의존성 주입이라고 표현하는데, A -> B를 의존하고 있다라고할 때, A가 B가 필요하니 직접 생성하여 사용하는게 일반적입니다. 하지만, 이런 생성권을 직접 가지고 있는게 아니라, 주입해줄 수 있는 즉 Spring Container를 활용해 인스턴스 타입에 맞는 객체를 대신해서 제공하겠다는 것에서 의존성 주입의 개념이 생겨났고, 흔히 말하는 객체의 타입을 인터파이스나 추상 클래스로 선언하여 다형성을 만들어갈 수 있음.
IoC는 제어의 역전인라고 불리는데 A가 가지고 있던 B의 제어권이 흔히 말하는 Spring Container에게 제어권이 넘어갔다고 해서 제어의 역전이라고 부르는 IoC라고 할 수 있습니다. -> 즉, 객체의 Life Cycle 제어권이 넘어갔다라고 할 수 있음

---

### Spring과 Spring Boot

Spring Boot는 기본적으로 Serverless를 위해 만들어진 프레임워크라고 설명하면 좋을 것 같습니다. 공식 문서에서도 "Stand Alone"이라는 말이 자주 보이는데 우리가 흔히 말하는 WAS의 대표 주자인 Tomcat, 설정, 보안 등등 설정에 많은 시간을 소요하고 구축하는데 비용이 들게 되는데 이러한 부분에 대해 큰 고민 없이 핵심 비즈니스 도메인을 개발할 수 있다는 것이 Spring과 Spring Boot간의 큰 차이라고 설명할 수 있을 것 같습니다.

그래서 Spring Boot는 이론적으로 `"자기 주장이 강하다"라는 특징이 있음` 정해주는대로 개발을 빠르게 해라. 라는 의미를 내포함

이외에도 AutoConfiguration과 같은 특징이 객체지향 패러다임에서 Bean으로 제공되어야할 때 구성하기 편하다는 점. 여기서 활용되는 특징은 조건부 자동구성 등등... 편하다는 특징이 있습니다.
