# 📝 graphql - yoga 란 무엇인가?

[참고링크](https://nomadcoders.co)

> GraphQL Server를 쉽게 설치할 수 있도록 한 것이며, 개발자에게 좋은 퍼포먼스와 경험을 하도록 해준다.

## 📝 graphql로 해결할 수 있는 2가지

- Over-fetching과 Under-fetching 이 있다.

> Over-fetching 이란? 우리는 영화 제목들을 브라우저에서 받고 싶을 때, /movies/ GET 을 통해 받을 것이다. 데이터베이스 입장에서는 영화 제목, 개봉 날짜, 출연진 등등 필요없는 정보들까지 보내게 되는데 이 중에서도 우리는 영화 제목 리스트가 필요한 것이다. -> 이렇게 비효율적인 것을 Overfetching 이라 함.

<span style="color:yellow">Graphql은 overfetching 없이 코드를 짤 수 있고 개발자가 어떤 정보를 원하는 지에 대해 통제 할 수 있고 Frontend에서 영화 제목 정보를 원할 때, 제목만을 전달해 줄 수 있다.</span>

> Under-fetching이란? 우리가 하나의 애플리케이션을 실행 할 때, 유저 정보를 받아오고 게시물들을 받아오며 한 번에 여러 요청을 하는 작업을 할 때 발생한다. 다시 말해 REST에서 하나를 완성 하기 위해 많은 소스를 요청하는 것이라 볼 수 있다. 이것 또한 GraphQL로 해결할 수 있다.

### ❗️ GraphQL에서 URL은 존재하지 않는다

/feed/<br>
/notifications<br>
/usrs/<br>
과 같은 요청을 url 없이 하나의 Query로 원허는 정보를 얻을 수 있다.
Example

```
{
    feed {
        comments
        likeNumber
    }
    notifications {
        isRead
    }
    user {
        userName
        profilePic
    }
}
# 이게 Query이며, 이걸 GraphQL의 Backend에 보내면 이와 같은 요청 정보를 담은 Object를 보내준다. => GraphQl에서 보낸 Javascript Object라고 보면 된다.

# 자바스크립트에서 받은 경우 :
{
    feed: [
        {
            comments:1,
            likeNumber: 20
        }
    ],
    notifications: [
        {
            isRead: true
        },
        {
            isRead: false
        }
    ],
    user: {
        username: "taeyong"
        profile:"http://"
    }
}
```

```
#Set up
yarn add graphql-yoga
yarn global add nodemon
yarn add @babel/core --dev
yarn add @babel/preset-env --dev
yarn add @babel/node --dev
echo '{"presets": ["@babel/preset-env"]}' > babel.config.json
yarn start

scripts -> "start": "nodemon --exec babel-node index.js"
```

## 📝 schema.graphql

> 여기서는 사용자가 뭘 할지에 대해 작성하는 곳이다. query, mutation 등등 작성해야 한다.

## 📝 graphQL Resolvers 란 무엇일까?

> 먼저, GraphQL 서버에서 요청을 받으면 GraphQL 서버가 Query나 Mutation의 정의를 발견하고 GraphQL API 요청에 맞게 전반적인 CRUD 결과물을 수행해줍니다.

### 📝 단순히 query 하고 mutation 하는 것은 Memory 상에서 수행 되기 때문에 Server를 껐다가 키면 원래 상태로 돌아간다.

- ❗️ 어느 Backend를 사용하더라도, GraphQL을 적용할 수 있는데 사용할 수 있는 Backend 중 하나는 다른 API인 REST API가 있다.
- yts.mx 에서 제공하는 REST interface를 통해 활용하기.
