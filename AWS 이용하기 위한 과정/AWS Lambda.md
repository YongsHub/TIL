> Lambda는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있게 해주는 컴퓨팅 서비스입니다. Lambda는 고가용성 컴퓨팅 인프라에서 코드를 실행하고 서버와 운영 체제 유지 관리, 용량 프로비저닝 및 자동 조정, 코드 및 보안 패치 배포, 코드 모니터링 및 로깅 등 모든 컴퓨팅 리소스 관리를 수행합니다. Lambda를 사용하면 거의 모든 유형의 애플리케이션 또는 백엔드 서비스에 대한 코드를 실행할 수 있습니다. Lambda가 지원하는 언어 중 하나로 코드를 공급하기만 하면 됩니다.

### 지원하는 언어

- Lambda는 런타임을 사용하여 여러 언어를 지원한다. 컨테이너 이미지로 정의된 함수의 경우 컨테이너 이미지를 생성할 때 런타임 및 Linux 배포판을 선택, 런타임을 변경하려면 새 컨테이너 이미지를 생성한다.

### Lambda는 실행 환경에서 함수를 호출함.

- 실행 환경은 함수를 실행하는데 필요한 리소스를 관리하는 안전하고 격리된 런타임 환경을 제공함. Node.js 런타임 제공

### Node JS의 Nest FrameWork에서 마주치는 문제점들

> Cold Start는 오랜만에 실행되는 코드를 의미하는데, 사용하는 클라우드 공급자에 따라 코드 다운로드 및 런타임 부트스트랩에서 최종 코드 실행까지 여러 작업에 걸쳐 있기에 이 과정은 여러 요소, 언어, 애플리케이션에 필요한 패키지 수 등에 따라 지연 시간을 크게 늘린다.

> Cold start는 중요하고 우리가 통제할 수 없는 일들이 있지만, 가능한 짧게 만들기 위해 우리가 할 수 있는 일들이 여전히 많다.

### Lambda 트리거 기능

> 람다 트리거란? 람다 함수를 실행할 수 있는 이벤트를 일컫는다. 간단하게, S3에 파일이 적재되면 이를 이벤트로 받아 람다 함수를 실행 할 수도 있고, 브라우저에 URL을 치면 Rest API로서 람다 함수를 실행 할 수도 있다. 이처럼 람다는 다른 AWS 서비스와 유기적으로 연동될 수 있다는 점에서 굉장히 파워풀 하다고 볼 수 있다.

### 이벤트 처리

```
service: dongchin-api

frameworkVersion: '3'

package:
  exclude:
    - node_modules/**

plugins:
  - serverless-plugin-optimize
  - serverless-dotenv-plugin
  - serverless-offline

provider:
  name: aws
  runtime: nodejs14.x
  region: ap-northeast-2
  timeout: 20
  stage: ${opt:stage, 'dev'}

functions:
  api:
    handler: dist/main.handler
    events:
      - http:
          method: ANY
          path: /
      - http:
          method: ANY
          path: '{proxy+}'

resources:
  Resources:
    GatewayResponseDefault4XX:
      Type: 'AWS::ApiGateway::GatewayResponse'
      Properties:
        ResponseParameters:
          gatewayresponse.header.Access-Control-Allow-Origin: "'*'"
          gatewayresponse.header.Access-Control-Allow-Headers: "'*'"
        ResponseType: DEFAULT_4XX
        RestApiId:
          Ref: 'ApiGatewayRestApi'
    GatewayResponseDefault5XX:
      Type: 'AWS::ApiGateway::GatewayResponse'
      Properties:
        ResponseParameters:
          gatewayresponse.header.Access-Control-Allow-Origin: "'*'"
          gatewayresponse.header.Access-Control-Allow-Headers: "'*'"
        ResponseType: DEFAULT_5XX
        RestApiId:
          Ref: 'ApiGatewayRestApi'

custom:
  optimize:
    external: ['swagger-ui-dist']

```

## Swagger

```
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger'
DocumentBuilder.addServer('/') 및 DocumentBuilder.addServer('/dev')를 통해서 Swagger 내에서 Test 경로를 추가할 수 있다.
```
