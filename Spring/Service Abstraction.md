**내용 저작권은 Toby의 Spring에 있습니다**

## Service Abstraction

자바에서는 표준 스펙, 상용 제품, 오픈 소스 등등 사용 방법과 형식이 다르지만 기능과 목적이 유사한 기술이 존재함.

같은 자바의 표준 기술 중에서도 플랫폼과 컨텍스트에 차이가 있거나 발전한 역사가 달라서 목적이 유사한 여러 기술이 공존하기도 함

DAO에 트랜잭션을 적용해보면서 스프링이 어떻게 성격이 비슷한 여러 종류의 기술을 추상화하고 이를 일관된 방법으로 사용할 수 있도록 지원하는지 실펴봄

---

예를 들어서,
사용자 레벨 관리 작업을 수행하는 도중에 네트워크가 끊기거나 서버에 장애가 생겨서 작업을 할 수 없으면, 그때까지 변경된 사용자의 레벨은 그대로 둘까? 에 관련해서

중간에 문제가 발생된다면 -> 그때까지 진행된 변경 작업도 모두 취소시키도록 결정하는 케이스들이 많다.

### 어떻게 작업 중간에 예외를 강제로 만들어서 테스트할 수 있을까?

가장 쉬운 방법은 예외를 강제로 발생시키도록 애플리케이션 코드를 수정하는 것이다.

하지만 테스트를 위해 코드를 함부로 건드리는 것이 좋은걸까?

그래서 이런 경우, 테스트용으로 특별히 만든 UserService의 대역을 사용하는 것이 좋음

-> 예외상황을 만들어서 테스트할 수 있지만, 전체 롤백을 어떻게 만들 수 있을지 고려해봐야함

### 트랜잭션 동기화

비즈니스 로직을 담고 있는 UserService Method 안에서 트랜잭션의 경계를 설정해 관리하려면 어떻게 해야할까?

- Transaction 동기화 저장소는 작업 스레드마다 독립적으로 Connection Object를 저장하고 관리하기 때문에 다중 사용자를 처리하는 서버의 멀티스레드 환경에서도 충돌이 날 염려는 없음

- 이렇게 Transaction 동기화 기법을 사용하면 파라미터를 통해 일일이 Connection 오브젝트를 전달할 필요가 없어짐.

문제는 멀티스레드 환경에서도 안전한 트랜잭션 동기화 방법을 구현하는 일이 기술적으로 간단하지 않다는 점인데, 스프링은 JdbcTemplate과 더불어 트랜잭션 동기화 기능을 지원하는 유틸리티 메소드를 제공함

```Java
private DataSource dataSource;

public void setDataSource(DataSource dataSource) { //Connection을 생성할 때 사용할 DataSource를 DI받음
    this.dataSource = dataSource;
}
```

```Java
public void upgradeLevels() throws Exception {
    //트랜잭션 동기화 관리자를 이용해 동기화 작업을 초기화함
    TrasactionSynchronizationManager.initSynchronization();
    //DB 커넥션을 생성하고 트랜잭션을 시작함
    Connection c = DataSourceUtils.getConnection(dataSource);
    c.setAutoCommit(false);

    try {
        List<User> users = userDao.getAll();
        for(User user : users) {
            if(canUpgradeLevel(user)) {
                upgradeLevel(user);
            }
        }
        c.commit();
    } catch(Exception e) {
        c.rollback();
        throw e;
    } finally {
        //스프링 유틸리티 메소드를 이용해 DB 커넥션을 안전하게 닫음
        DataSourceUtils.releaseConnection(c, dataSource);
        //동기화 작업 종료 및 정리
        TransactionSynchronizationManager.unbindResource(this.dataSource);
        TransactionSynchronizationManager.clearStynchronization();
    }
}
```

- 스프링이 제공하는 유틸리티 메소드를 쓰는 이유는 DataSourceUtils의 getConnection() 메소드는 Connection Object 생성 뿐만 아니라 트랜잭션 동기화에 사용하도록 저장소에 바인딩해주기 때문
- 트랜잭션 동기화가 되어 있는 채로 JdbcTemplate을 사용하면 JdbcTemplate의 작업에서 동기화 시킨 DB 커넥션을 사용하게 됨
- 따라서, UserDao를 통해 진행되는 모든 JDBC 작업은 upgradeLevels()메소드에서 만든 Connection 오브젝트를 사용하고 같은 트랜잭션에 참여하게 됨

## 궁금해진 JdbcTemplate의 동작 방식

지금까지 JdbcTemplate은 update()나 query() 같은 JDBC 작업의 템플릿 메소드를 호출하면 직접 Connection을 생성하고 종료하는 일을 모두 담당했음

- JdbcTemplate은 영리하게 동작하도록 설계되어 있음. 만약 미리 생성돼서 트랜잭션 동기화 저장소에 등록된 DB커넥션이나 트랜잭션이 없는 경우에는 JdbcTemplate이 직접 DB 커넥션을 만들고 트랜잭션을 시작해서 JDBC 작업을 진행함

- 반면, upgradeLevels() 메소드에서 처럼 트랜잭션 동기화를 시작해놓았다면 그때부터 실행되는 JdbcTemplate의 메소드에서는 직접 Connection을 생성하는 것이 아니라 트랜잭션 동기화 저장소에 들어 있는 DB 커넥션을 가져와서 사용함 -> 이를 통해, 이미 시작된 트랜잭션에 참여하는 것

### 하나의 트랜잭션 처리 코드에서 글로벌 트랜잭션 방식

어떤 회사에서 여러 개의 DB에 데이터를 넣는 작업을 해야 할 필요가 있을 때 -> 한 개 이상의 DB로의 작업을 하나의 트랜잭션으로 만드는건 JDBC의 Connection을 이용한 트랜잭션 방식인 로컬 트랜잭션으로는 **_불가능_** 하다.

각 DB와 독립적으로 만들어지는 Connection을 통해서가 아니라, 별도의 트랜잭션 관리자를 통해 트랜잭션을 관리하는 글로벌 트랜잭션(Global Transaction)방식을 사용해야함

> 따라서, 자바는 JDBC 외에 이런 글로벌 트랜잭션을 지원하는 트랜잭션 매니저를 지원하기 위한 JTA(Java Transaction API)를 제공하고 있음

따라서, UserService는 자신의 로직이 바뀌지 않았음에도 기술환경에 따라서 코드가 바뀌는 코드가 돼버렸다.

여기서 끝나는 것이 아니라 또 다른 고객관리 구매사에서 자신들이 Hibernate를 이용해 UserDao를 직접 구현했다고 알려왔다.

당연히 DI를 이용해서 UserDao의 데이터 액세스 기술은 얼마든지 변경이 가능하다. 그런데 문제는 여기서 발생함.

> Hibernate를 이용한 트랜잭션 관리 코드는 JDBC나 JTA의 코드와 또 다른다는 것. Hibernate는 Connection을 직접 사용하지 않고 Session이라는 것을 사용하고, 독자적인 트랜잭션 API를 사용함.

| 결론적으로 UserService를 Hibernate의 Session과 Transaction 오브젝트를 사용하는 트랜잭션 경계 설정 코드로 변경할 수 밖에 없게됨

| 서비스 레이어와 로우레벨의 트랜잭션 기술과 API의 변화에 상관없이 일관된 API를 가진 추상화 계층을 활용해야함

### 메일 발송 기능 추상화

JavaMail은 확장이나 지원이 불가능하도록 만들어진 악명 높은 표준 API중 하나이다.

JavaMail 대신 테스트용 JavaMail로 대체를 어떻게 할까?
서비스 추상화를 적용하면 된다.

스프링은 JavaMail에 대한 추상화 기능을 제공하고 있다.

```Java
public interface MailSender {
    void send(SimpleMailMessage simpleMessage) throws MailException;
    void send(SimpleMailMessage[] simpleMessages) throws MailException;
}
```

이 인터페이스는 SimpleMailMessage라는 인터페이스를 구현한 클래스에 담긴 메일 메시지를 전송하는 메소드로만 구성되어 있는데, 기본적으로 JavaMail을 사용해 메일 발송 기능을 제공하는 JavaMailSenderImpl을 사용하면 됨

```Java
private void sendUpgradeEmail(User user) {
    JavaMailSenderImpl mailSender = new JavaMailMessage();
    mailSender.setHost("mail.server.com");

    SimpleMailMessage mailMessage = new SimpleMailMessage();
    mailMessage.setTo(user.getEmail());
    ...

    mailSender.send(mailMessage);
}
```

**복잡한 코드는 정리됐지만 JavaMail API를 사용하는 JavaMailSenderImpl 클래스의 오브젝트를 코드에서 직접 사용하기 때문에 JavaMail API를 사용하지 않는 테스트용 오브젝트로 대체할 수는 없다**

그렇다면 무엇을 해야할까?

Spring의 DI를 적용할 차례다. 원하는건 실제 JavaMail을 사용하지 않고 메일 발송 기능이 포함된 코드를 테스트하는 것이다.

Spring이 제공한 메일 전송 기능에 대한 인터페이스가 있으니 이를 구현해서 테스트용 메일 전송 클래스를 만드는 것이다.

**아무런 기능이 없는 MailSender 구현 빈 클래스**

```Java
public class DummyMailSender implements MailSender {
    public void send(SimpleMailMessage simpleMessage) throws MailException;
    public void send(SimpleMailMessage[] simpleMessages) throws MailException;
}
```

DummyMailSender는 MailSender 인터페이스를 구현했을 뿐, 하는 일이 없음

따라서, 트랜잭션과 같이 추상화를 말할 수도 있지만, 테스트를 어렵게 만드는 건전하지 않은 방식으로 설계된 API를 사용할 때도 유용하게 쓰일 수 있다.

## 결론

- 트랜잭션 경계 설정 코드가 비즈니스 로직 코드에 영향을 주지 않게 하려면 스프링이 제공하는 트랜잭션 서비스 추상화를 이용
- 서비스 추상화는 테스트하기 어려운 JavaMail같은 기술에도 적용가능
- 비즈니스 로직을 담은 코드는 데이터 액세스 로직을 담은 코드와 깔끔하게 분리되는 것이 바람직함. 비즈니스 로직 코드 또한 내부적으로 책임과 역할에 따라서 깔끔하게 메소드로 정리돼야 함
