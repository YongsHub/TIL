**내용 저작권은 Toby의 Spring에 있습니다**

## AOP

AOP? 스프링의 3대 핵심 기술 중 하나이다.
스프링의 기술 중, 가장 이해하기 힘든 난해한 용어와 개념을 가진 기술이다.
AOP를 바르게 이용하려면 필연적인 등장배경과 스프링이 그것을 도입한 이유, 적용을 통해 얻을 수 있는 장점이 무엇인지에 대한 충분한 이해가 필요함

**스프링에 적용된 가장 인기 있는 AOP의 적용 대상은 바로 선언적 트랜잭션 기능이다**
서비스 추상화를 통해 많은 근본적인 문제를 해결했던 트랜잭션 경계설정 기능을 AOP를 이용해 더욱 세련되고 깔끔한 방식으로 바꿔볼 수 있음

더하여, 과정 속에 AOP를 도입해야 했던 이유도 알아봐야 한다.

비즈니스 로직이 주인이어야 할 메소드 안에 이름도 길고 트랜잭션 코드가 더 많은 자리를 차지하는 모습이 별로다.

따라서, 한 번에 두 개의 Service Interface 구현 클래스를 동시에 이용하면 어떨까?
지금 해결하려고 하는 문제는 Service에는 순수하게 비즈니스 로직을 담고 있는 코드만 놔두고 트랜잭션 경계설정을 담당하는 코드를 외부로 빼내려는 것. 하지만 클라이언트가 Service의 기능을 제대로 이용하려면 트랜잭션이 적용돼야 함.

따라서 Trasaction 설정만 해주는 ServiceTx를 구현하여 비즈니스 로직을 담은 Service를 DI하여 구현하는 방법이 존재함.

---

스프링의 테스트용 컨텍스트에서 가져올 빈들을 생각해보자. 기존에는 Service 클래스 타입의 빈을 @Autowired로 가져다가 사용했음. 하지만 Service는 이제 인터페이스로 바뀌었음. 인터페이스라고 하더라도 Autowired로 가져오는데 아무런 문제가 없음.
인터페이스 타입을 가진 두 개의 빈이 존재한다면 기본적으로 하나의 빈을 결정할 수 없을때는 필드 이름을 이용해 빈을 찾음

결과적으로 UserService는 인터페이스로 변경했으므로 테스트 코드는 이제 구체적인 정보는 알지 못한 채 -> 컨테이너가 제공해주는 대표적인 UserService 구현 오브젝트를 사용함

---

가장 편하고 좋은 테스트 방법 -> 가능한 한 작은 단위로 쪼개서 테스트

클래스 하나가 동작하도록 테스트를 만드는 것과 클래스 수십 개가 얽히고 섥혀서 동작하도록 만드는 것 중에서 어던 것이 논리적인 오류를 착기 쉬울지는 분명함.
하지만 그럴 수 없는 경우가 많음 -> 테스트 대상이 다른 오브젝트와 환경에 의존하고 있다면 작은 단위의 테스트가 주는 장점을 얻기 힘들다.

따라서, 목 오브젝트 등의 테스트 대역을 이용해 의존 오브젝트나 외부의 리소스를 사용하지 않도록 고립시켜서 테스트하는 방법이 존재함.

단위테스트의 단위는 정하기 나름이겠지만 -> 고립시키는 것을 명칭해보자

### Dynamic Proxy 와 Factory Bean

- 트랜잭션 관련 코드와 핵심 비즈니스 코드를 지금까지 분리할 수 있다는 사실을 알았고, 클래스를 따로 만들었다 -> ServiceTx, Service
  이렇게 분리된 부가기능을 담은 클래스(ServiceTx)는 중요한 특징이 있음

> 부가 기능 외의 나머지 모든 기능은 핵심기능을 가진 클래스로 위임해주어야 함, 핵심 기능은 부가기능을 가진 클래스의 존재 자체를 모름. 따라서 부가기능이 핵심기능을 사용하는 구조가 되는 것

부가 기능 코드에서는 핵심기능으로 요청을 위임해주는 과정에서 자신이 가진 부가적인 기능을 적용해줄 수 있음. 비즈니스 로직 코드에서 트랜잭션 기능을 부여해주는 것이 바로 그런것.

> 자신이 마치 클라이언트가 사용하려고 하는 실제 대상인 것 처럼 위장해서 클라이언트의 요청을 받아주는 것을 대리자, 대리인과 같은 역할을 한다고 해서 프록시라고 부름

**프록시를 통해 최종적으로 요청을 위임받아 처리하는 실제 오브젝트를 타깃(Target)이라 부름**

- 프록시는 클라이언트가 타깃에 접근하는 방법을 제어하기 위해서 사용
- 타깃에 부가적인 기능을 부여해주기 위해 사용

| 두 가지 모두 대리 오브젝트라는 개념의 프록시를 두고 사용한다는 점은 동일하나, 디자인 패턴에서는 다른 패턴으로 구분

### 데코레이터 패턴

> 데코레이터 패턴은 타깃에 부가적인 기능을 런타임 시 다이내믹하게 부여해주기 위해 프록시를 사용하는 패턴을 말함. 즉, 다이내믹하게 기능을 부가한다는 의미는 컴파일 시점, 즉 코드상에서 어떤 방법과 순서로 프록시와 타깃이 연결되어 사용되는지 정해져 있지 않다는 뜻이다.

**_데코레이터 패턴은 인터페이스를 통해 위임하는 방식이기 때문에 어느 데코레이터에서 타깃으로 연결될지 코드 레벨에서는 미리 알 수 없다._**

### 프록시 패턴

**_일반적으로 사용하는 프록시라는 용어와 디자인 패턴에서 말하는 프록시 패턴은 구분할 필요가 있음_**

프록시 패턴에서의 의미는 프록시를 사용하는 방법 중에서 타깃에 대한 접근 방법을 제어하려는 목적을 가진 경우를 말함

- 프록시 패턴의 프록시는 타깃의 기능을 확장하거나 추가하지 않음
- 대신 클라이언트가 타깃에 접근하는 방식을 변경해준다

타깃 오브젝트를 생성하기가 복잡하거나, 당장 필요하지 않은 경우 꼭 필요한 시점까지 오브젝트를 생성하지 않는 편이 좋음

**_그런데 타깃 오브젝트에 대한 레퍼런스가 미리 필요할 수 있음_**

`이럴때 프록시 패턴을 적용하면 됨`

클라이언트에게 타깃에 대한 레퍼런스를 넘겨야 하는데, 실제 타깃 오브젝트는 만드는 대신 프록시를 넘겨주는 것
그리고 프록시의 메소드를 통해 타깃을 사용하려고 시도하면 그때, `프록시가 타깃 오브젝트를 생성하고 요청을 위임해주는 식이다.`

이렇게 프록시 패턴은 타깃의 기능 자체에는 관여하지 않으면서 접근하는 방법을 제어해주는 프록시를 이용하는 것이다.
타깃과 동일한 인터페이스를 구현하고 클라이언트와 타깃 사이에 존재하면서 기능의 부가 또는 접근 제어를 담당하는 오브젝트를 모두 프록시라 부를 것이다.

`다만, 사용의 목적이 기능의 부가인지, 접근 제어인지를 구분해보면 각각 어떤 목적으로 프록시가 사용됐는지, 그에 따라 어떤 패턴이 적용됐는지 알 수 있을 것`

### Dynamic Proxy

`다이내믹 프록시는 프록시 팩토리에 의해 런타임 시 다이내믹하게 만들어지는 오브젝트임`

다이나믹 프록시 오브젝트는 타깃의 인터페이스와 같은 타입으로 만들어짐
클라이언트는 다이나믹 프록시 오브젝트를 타깃 인터페이스를 통해 사용할 수 있음

프록시 팩토리에게 인터페이스 정보만 제공해주면 해당 인터페이스를 구현한 클래스의 오브젝트를 자동으로 만들어줌

부가기능은 프록시 오브젝트와 독립적으로 InvocationHandler를 구현한 오브젝트에 담음
InvocationHandler 인터페이스는 메소드 한개만 가진 간단한 인터페이스이다.

`기존에 사용하던 ServiceTx를 Dynamic Proxy방식으로 변경해볼 수 있다`
ServiceTx는 서비스 인터페이스의 메소드를 모두 구현해야 하고 트랜잭션이 필요한 메소드마다 트랜잭션 처리 코드가 중복돼서 나타나는 비효율적인 방법으로 만들어져 있다. 트랜잭션이 필요한 클래스와 메소드가 증가하면 ServiceTx처럼 프록시 클래스를 일일이 구현하는 것은 매우 큰 부담

**따라서 트랜잭션 부가 기능을 제공하는 Dynamic Proxy를 만들어 적용하는 방법이 효율적**

```Java
public class TransactionHandler implements InvocationHandler {
    private Object target; // 부가기능을 제공할 target object 어떤 type의 object도 가능
    private PlatformTransactionManager transactionManager; // 트랜잭션 기능을 제공하는 데 필요한 트랜잭션 매니저
    private String pattern; // 트랜잭션을 적용할 메소드 이름 패턴

    public void setTarget(Object target) {
        this.target = target;
    }

    public void setTransactionManager(PlatformTransactionManager transactionManager) {
        this.transactionManager = transactionManager;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        if(method.getName().startsWith(pattern)) { // 트랜잭션 적용 대상 메소드를 선별해서 트랜잭션 경계설정 기능을 부여
            return invokeInTransaction(method, args);
        } else {
            return method.invoke(target, args);
        }
    }

    private Object invokeInTransaction(Method method, Object[] args) throws Throwable {
        TransactionStatus status = this.transactionManager.getTransaction(new DefaultTransactionDefinition());

        try {
            Object ret = method.invoke(target, args);
            this.transactionManager.commit(status);
            return ret;
        } catch (InvocationTargetException e) {
            this.transactionManager.rollback(status);
            thorw e.getTargetException();
        }
    }
}
```

트랜잭션을 적용하면서 타깃 오브젝트의 메소드를 호출하는 것은 ServiceTx에서와 동일하다.
한가지 차이점은 롤백을 적용하기 위한 예외는 RuntimeException 대신 `InvocationTargetException`을 잡도록 해야함
Refection의 메소드인 Method.invoke()를 이용해 타깃 오브젝트의 메소드를 호출할 때는 타깃 오브젝트에서 발생하는 예외가 `InvocationTargetException`으로 한번 더 포장돼서 전달되기 때문임.
