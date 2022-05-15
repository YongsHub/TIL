# Nest JS

Node JS 서버 측 애플리케이션을 구축하기 위한 프레임 워크 프로그레시브 자바스크립트를 사용하고 TypeScript로 빌드되고 완벽하게 지원하며 OOP, FP, FRP 요소를 사용할 수 있게 해준다.

## ❗️ 내부?

내부적으로 Express Framework와 같은 강력한 HTTP 서버 프레임 워크를 사용하며 선택적으로 Fastify를 사용하도록 구성할 수 있다.

## 철학

Node를 위한 훌륭한 라이브러리, 도우미 및 도구가 많이 존재하지만 이들 중 어느 것도 아키텍처의 주요 문제를 효과적으로 해결하지 못함.

Nest -> 개발자와 팀이 고도로 테스트 가능하고 확장 가능하며 느슨하게 결합되고 유지 관리가 쉬운 애플리케이션을 만들 수 있는 즉시 사용 가능한 애플리케이션 아키텍처를 제공함.

## Nest JS CLI로 Nest JS 시작

```shell
npm i -g @nestjs/cli

nest new project-name
또는 현재 위치한 폴더 내 설정은
nest new ./
```

## 👨‍💻 간단한 CRUD Model 만들기

- 게시판을 만들기 때문에 게시글에 관한 모듈과 게시글을 만드는 사람에 대한 인증 모듈이 필요합니다. 그리고 각 모듈을 구성하는 Controller, Service, Repository 등이 있는데 이러한 용어는 Express를 사용할 때도 들어보았을 수 있지만 Nest JS에서는 어떠한 용도로 사용되는지 하나씩 알아보자

## 📌 Nest JS 기본 구조 설명

- eslintrc.js : 개발자들이 특정한 규칙을 가지고 코드를 깔끔하게 짤수있게 도와주는 라이브러리
- prettierrc : 주로 코드 형식을 맞추는데 사용한다. 작은 따옴표를 사용할지 큰 따옴표를 사용할지 -> Code Formatter 역할
- nest-cli.json : nest 프로젝트를 위해 특정한 설정을 할 수 있는 json 파일
- tsconfig.json : 어떻게 타입스크립트를 컴파일 할지 설정
- tsconfig.build.json : tsconfig.json의 연장선상 파일이며 build할 때 필요한 설정들 "excludes"에서 빌드할 때 필요 없는 파일들 작성
- package.json : build -> 운영환경을 위한 빌드, format: 린트에러가 났을지 수정 start: 앱 시작

## Controller란

> controller는 들어오는 요청을 처리하고 클라이언트에 응답을 반환한다. @Controller 데코레이터로 클래스를 데코레이션하여 정의됩니다.

## Handler란

> 핸들러는 @Get, @Post, @Delete 등과 같은 데코레이터로 장식 된 컨트롤러 클래스 내의 단순한 메서드입니다.

## Service란

> Service 안에서는 데이터베이스 관련된 로직을 처리하겠습니다. 데이터베이스에서 데이터를 가져오거나 데이터베이스안에 게시판 생성할때 그 생성한 게시판 정보를 넣어주는 등의 로직을 처리합니다. 이 생성된 파일 안에는 Injectable 데코레이터가 있으며 이 Nest JS는 이것을 이용해 다른 컴포넌트에서 이 서비스를 사용할 수 있게 Injectable만들어줍니다.

## Provider란 ?

> 프로바이더는 Nest의 기본 개념. 대부분 기본 Nest 클래스는 서비스, 리포지토리, 팩토리, 헬퍼 등 프로바이더로 취급될 수 있다. 프로바이더의 주요 아이디어는 종속성으로 주입할 수 있다는 것이다. 즉, 객체는 서로 다양한 관계를 만들 수 있으며 객체의 인스턴스를 "연결"하는 기능은 대부분 Nest 런타임 시스템에 위임될 수 있습니다.

## uuid 모듈 사용하기 위해서

> npm install uuid --save를 이용해서 설치해줍니다. 그 후에 uuid 모듈을 사용하기 위해서는 원하는 곳에서 import 해준다. import {v1 as uuid} from 'uuid';

## DTO (Data Transfer Object)

> 계층 간 데이터 교환을 위한 객체이다. DB에서 데이터를 얻어 Service나 Controller 등으로 보낼 때 사용하는 객체를 말합니다. DTO는 데이터가 네트워크를 통해 전송되는 방법을 정의하는 객체입니다. Interface나 class를 이용해서 정의될 수 있습니다.

## DTO를 쓰는 이유는 무엇인가?

> 데이터 유효성을 체크하는데 효율적이다. 더 안정적인 코드를 만들어 주고 타입스크립트의 타입으로도 사용.

> 게시판에서 title과 description의 property같은 경우는 개수가 적기 때문에 편하겠지만 정말 많은 프로퍼티를 갖고 여러군데에서 이용하며 갑자기 한 곳에서 Property 이름을 바꿔줘야한다면 어떻게 해야할까? 이렇게 되면 애플리케이션을 유지보수하기 힘들어질 수 있다. 따라서 DTO를 이용하자!

## PIPE는 무엇인가?

> @Injectable 데코레이터로 주석이 달린 클래스입니다. 파이프는 data transformation 과 data validation을 위해 사용합니다. 파이프는 컨트롤러 경로 처리기에 의해 처리되는 인수에 대해 작동합니다. Nest는 메소드가 호출되기 직전에 파이프를 삽입하고 파이프는 메소드로 향하는 인수를 수신하고 이에 작동함.

## PIPE 사용하는 법

> Handler - level Pipe, Parameter - level Pipe, Global - level Pipe 3가지 방법이 존재합니다. 기본적으로 사용할 수 있는 PIPE는 6가지가 존재한다.

- ValidationPipe
- ParseIntPipe
- ParseBoolPipe
- ParseArrayPipe
- ParseUUIDPipe
- DefaultValuePipe

## 커스텀 파이프 구현 방법

> 먼저 PipeTransform이란 인터페이스를 새롭게 만들 커스텀 파이프에 구현해주어야 한다. 그리고 이것과 함께 모든 pipe는 transform() 메서드를 필요로 함. 이 메서드는 Nest JS가 인자를 처리하기 위해 사용된다.

## TypeORM (Object Relational Mapping) 소개

> TypeORM은 node.js에서 실행되고 TypeScript로 작성된 객체 관계형 매핑 라이브러리이다. TypeORM은 MySQL, PostgreSQL, MariaDB, SQLite, MS SQL Server, Oracle 등등 여러 데이터 베이스를 지원한다.

> ORM은(Object Relational Mapping)이란 객체와 관계형 데이터베이스의 데이터를 자동으로 변형 및 연결하는 작업입니다. ORM을 이용한 개발은 객체와 데이터베이스의 변형에 유연하게 사용할 수 있습니다. 객체지향 프로그래밍은 클래스를 사용, 관계형 데이터베이스는 테이블을 사용하는데 이들 간의 매핑을 해준다.

> TypeORM 특징과 이점, 모델을 기반으로 데이터베이스 테이블 체계를 자동으로 생성. 데이터베이스에서 개체를 쉽게 삽입, 업데이트 및 삭제가 가능하다. 테이블 간의 매핑을 만듬. 간단한 CLI 명령을 제공, TYPEORM은 간단한 코딩으로 ORM 프레임워크를 사용하기 쉬움.

## Repository 생성하기

> 리포지토리는 엔티티 개와 함께 작동하며 엔티티 찾기, 삽입, 업데이트, 삭제 등을 처리함. 데이터베이스에 관련 된 일은 서비스에서 하는게 아닌 Repository에서 해주면 되는데 이러한 것을 Repository Parttern이라고도 부른다. 데이터베이스에 관련된 일은(Insert, Find, Delete 등등)

- 1. Repository 생성하기 (board.repository.ts)
- 2. 생성한 파일에 Repository를 위한 클래스 생성하기 (생성 시 Repository 클래스를 Extends 해준다.)
- 3. @EntityRepository() 클래스를 사용자 정의 저장소로 선언하는데 사용,사용자 지정 저장소는 일부 특정 엔티티를 관리하거나 일반 저장소 일 수 있습니다.

## remove() vs delete()

> remove: 무조건 존재하는 아이템을 remove 메소드를 이용해서 지워야 한다. 그러지 않으면 에러가 발생함. <br> delete: 만약 아이템이 존재하면 지우고 존재하지 않으면 아무런 영향이 없다. 이러한 차이 때문에 remove를 이용하면 하나의 아이템을 지울 때 두번 데이터베이스를 이용해야 하기 때문에 (아이템 유무 + 지우기) 데이터베이스에 한번만 접근해도 되는 delete메서드를 사용하자. 다큐멘테이션은 https://github.com/typeorm/typeorm/blob/master/docs/repository-api.md

# AuthModule

## 📌 AuthController, UserEntity, AuthService, UserRepository, JWT, Passport 등등

## CLI를 이용한 모듈 컨트롤러 서비스 생성

- nest g module auth : auth 모듈 생성
- nest g controller auth --no-spec : auth 컨트롤러 생성
- nest g service auth --no-spec : auth 서비스 생성

## 📎 User를 위한 Entity 생성

유저에 대한 인증을 하는 것이니 유저가 필요하다. 그래서 유저 데이터를 위한 유저 Entity를 생성.

1. user.entity.ts 파일 생성
2. 파일 소스 코드 작성

## 📎 Repository 생성

User Entity를 생성, 수정, 삭제등의 로직을 처리하기 위해서 Repository를 생성

1. user.repository.ts 파일 생성
2. 소스 코드 작성

```
ex) user module안에 foreFeature의 기능!
imports: [
    TypeOrmModule.forFeature([BoardRepository]) forFeature는 이 모듈 안에 레파지토리를 등록해주는 역할.
]
```

## 중복된 닉네임을 방지하기 위해서

1. repository에서 findOne 메소드를 이용해서 이미 같은 유저 이름을 가진 아이디가 있는지 확인하고 없다면 데이터를 저장하는 방법. 하지만 이 방법은 데이터베이스 처리를 두번 해줘야 한다.

- @unique(['usernmae']) 과 같은 데코레이터를 이용할 수 있다.
  테스트 해보면 이미 있는 유저를 다시 생성하려 하면 아래와 같은 에러가 나온다. 하지만 그냥 500 에러를 던져버리는데, 그 이유는 Nest JS에서 에러가 발생하고 그걸 try catch 구문인 catch에서 잡아주지 않는다면 이 에러가 Controller 레벨로 가서 500 에러를 던져 버린다.

따라서, try catch 구문으로 에러를 잡아줘야한다.

## 📎 비밀번호 암호화 하기

> bcryptjs : 이 기능을 구현하기 위해서 bcryptjs 모듈을 사용

- npm install bcrypt --save

## 비밀번호를 데이터베이스에 저장하는 방법

1. 1234 -> 1234 (최악의 방법)
2. 비밀번호를 암호화 키와 함께 암호화 (양방향) : 암호화 키가 노출되면 알고리즘은 대부분 오픈되어 있기 때문에 위험도가 높다.
3. SHA256 복호화는 불가능하지만 레인보우 테이블을 이용해 알아낼 수 있다.
4. 솔트(salt) + 비밀번호(Plain Password)를 해시로 암호화 해서 저장 === bcrpyt
   bcrypt.genSalt() bcrypt.hash(password, salt);

### ❗️ 로그인을 할 때, 로그인한 고유 유저를 위한 토큰을 생성해야 하는데 그 토큰을 생성할 때 JWT라는 모듈을 사용함.

### 📌 JWT 개념 다시 한번 정리하기

- JWT(JSON Web Token)는 당사자간에 정보를 JSON 개체로 안전하게 전송하기 위한 컴팩트하고 독립적인 방식을 정의하는 개방형 표준 (RFC 7519)이다. 이 정보는 디지털 서명이 되어 있으므로 확인하고 신뢰할 수 있습니다. 간단하게 얘기 하자면 정보를 안전하게 전할 때 혹은 유저의 권한 같은 것을 체크를 하기 위해서 사용하는데 유용한 모듈이다.

필요한 모듈 설치하기

- @nestjs/jwt : nestjs에서 jwt를 사용하기 위해 필요한 모듈
- @nestjs/passport : nestjs에서 passport를 사용하기 위해 필요한 모듈
- passport : passport 모듈
- passport-jwt : jwt 모듈
- npm i @nestjs/jwt @nestjs/passport passport passport-jwt --save

### 📌 Passport, Jwt 이용해서 토큰 인증 후 유저 정보 가져오기

- JWT를 이용하여 유저가 로그인 할 때 토큰을 생성해줬었는데, 이제는 그 유저가 요청을 보낼 때 그 요청 안에 있는 Header에 토큰을 넣어서 요청을 보내는데 요청 안에 Payload가 있다. 그리고 payload 안에 유저 이름을 넣어줬었는데 토큰이 유효한 토큰인지 서버에서 secret text를 이용해서 알아내면 payload 안에 유저 이름을 이용해서 데이터베이스 안에 있는 유저 이름에 해당하는 유저 정보를 모두 가져올 수 있다. 이러한 처리를 쉽게 해주는게 Passport 모듈이다. 그래서 Passport 모듈을 이용해서 이 부분을 구현해보자.
