# Task Definition

- 원하는 Docker 컨테이너를 생성할 때, 어떤 설정으로 몇 개 이상 생성할 지를 정의한 Set이다.
- 컨테이너 이미지, CPU/메모리 리소스 할당 설정, Port 매핑, Volume 설정 같은 것들이 포함되며, 기존 Docker Run명령에서 가능했던 대부분 옵션이 설정 가능하다.
- 컨테이너 오케스트레이션에서는 컨테이너가 필요에 따라서 자동적으로 실행되거나 종료될 수 있는데, 따라서 매번 이러한 설정들을 지정하기 보다 미리 설정들의 집합을 하나의 단위로 정의해놓고 사용 -> 이 단위가 태스크 데피니션이다.
- 한 번 태스크 데피니션을 만들면 이것을 기반으로 특정 설정을 변경함.
- Task definition에는 한 개 이상의 컨테이너에 대해 정의가 가능하며, 내부에 정의된 컨테이너 사이는 link 설정으로 연결이 가능.
- Task Definition에서 정의된 대로 실제 생성된 Container Set들을 Task라고 부르게 된다.

# Container Instance (EC2 Instance)

- ECS는 Container 배포(Task 배포)를 EC2 Instance 기반에 올리도록 설계 되어 있다.
- ECS를 처음 시작하면 생성되는 Default Cluster에는 Container Instance를 자동으로 할당 시켜 주기도 하지만 새롭게 Cluster를 생성하게 되면 직접 Container Instance를 만들어야 한다.
- Container Instance 용 AMI 이미지는 AWS 측에서 제공해 주기 때문에 어렵지 않게 생성이 가능하다.
- 하나의 Container Instance 내부에는 각각의 다른 Task가 여러 개 있을 수 있다.

# Cluster

- Task가 배포되는 Container Instance들은 논리적인 그룹으로 묶이게 되는데 이 단위를 Cluster라고 부른다.
- Task를 배포하기 위한 Instance는 반드시 Cluster에 등록되어야 한다.
