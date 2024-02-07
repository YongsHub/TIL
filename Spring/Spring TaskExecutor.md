## 해당 내용은 Spring Docs를 기반으로 정리 및 학습했습니다

Executor는 single threaded 또는 비동기로 동작할 수 있습니다.

> Spring의 추상화는 Java SE와 Jakarta EE 환경 사이에 대해 상세한 구현을 추상화했음

### TaskExecutor Types

Spring 6.1 버전부터 ThreadPoolTaskExecutor는 Spring의 라이프사이클 관리를 통한 일시 중지/다시 시작 기능 및 우아한 종료 기능을 제공합니다.

Spring's의 TaskExecutor를 구현은 흔히 DI 기술을 활용하여 사용합니다.

```kotlin
@Configuration
@EnableScheduling
class ScheduleConfig {

	@Bean
	fun taskExecutor(): TaskExecutor {
		val threadPoolTaskExecutor = ThreadPoolTaskExecutor()

		threadPoolTaskExecutor.corePoolSize = 5
		threadPoolTaskExecutor.maxPoolSize = 10
		threadPoolTaskExecutor.queueCapacity = 25

		return threadPoolTaskExecutor
	}
}
```

ThreadPoolTaskExecutor에 대해 설정 docs: https://kapentaz.github.io/spring/Spring-ThreadPoolTaskExecutor-%EC%84%A4%EC%A0%95/#

### Spring TaskSchedular Abstraction

```java
public interface TaskScheduler {

	Clock getClock();

	ScheduledFuture schedule(Runnable task, Trigger trigger);

	ScheduledFuture schedule(Runnable task, Instant startTime);

	ScheduledFuture scheduleAtFixedRate(Runnable task, Instant startTime, Duration period);

	ScheduledFuture scheduleAtFixedRate(Runnable task, Duration period);

	ScheduledFuture scheduleWithFixedDelay(Runnable task, Instant startTime, Duration delay);

	ScheduledFuture scheduleWithFixedDelay(Runnable task, Duration delay);
```

추상화된 서비스를 통해서 원하는 로직들을 구현할 수 있습니다.

> 가장 간단한 방법은 Runnable과 Instant만을 매개변수로 받는 schedule 메서드입니다. 이 메서드를 사용하면 지정된 시간 이후에 작업이 한 번 실행됩니다. 나머지 모든 메서드는 작업을 반복해서 실행할 수 있습니다. fixed-rate 및 fixed-delay 메서드는 간단한 주기적 실행을 위한 것이지만 Trigger를 받는 메서드는 훨씬 더 유연합니다.

### 비즈니스의 요구 사항이 특정 시간에 대해 Task를 수행하도록 해야 한다면?

특정 시간에 대해 스케쥴을 등록하여 우아한 설계를 할 수 있다고 판단했습니다.
