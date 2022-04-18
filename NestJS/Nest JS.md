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
