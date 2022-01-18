# 생각할 수 있는 여러 방법들

```import java.util.*;

class Solution {
    class Truck { // 트럭 객체 생성
        int weight;
        int move;

        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }

        public void moving() {
            move++;
        }
    }

    public int solution(int bridgeLength, int weight, int[] truckWeights) {
        Queue<Truck> waitQ = new LinkedList<>();
        Queue<Truck> moveQ = new LinkedList<>();

        for (int t : truckWeights) {
            waitQ.offer(new Truck(t)); // 대기 트럭 갯수 만큼 트럭 객체를 생성
        }

        int answer = 0;
        int curWeight = 0;

        while (!waitQ.isEmpty() || !moveQ.isEmpty()) { // 대기 트럭 & 움직이는 트럭 큐가 비어있지 않을때까지 무한 반복
            answer++;

            if (moveQ.isEmpty()) { // 움직이는 트럭 큐가 비었다면
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
                continue;
            }

            for (Truck t : moveQ) { // 매 반복마다 트럭은 움직여야 한다.
                t.moving();
            }

            if (moveQ.peek().move > bridgeLength) { // 다리를 지나 나왔다면 -> moveQ에서 제거해준다.
                Truck t = moveQ.poll();
                curWeight -= t.weight;
            }

            if (!waitQ.isEmpty() && curWeight + waitQ.peek().weight <= weight) { // 대기 큐가 비어있지 않고, 대기 큐 peek()의 weight + 현재weight를 더했을 때 weight보다 작거나 같으면
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
            }
        }

        return answer;
    }
}
```

## 기억 남는 문제

> 🎈문제들을 직접 다 푸는 것에 성공했지만, number3를 풀고 나서 다른 사람들이 푼 방식을 보면서 놀랬던 문제이다.

## <span style="color:yellow">객체 지향적으로 생각해보자</span>

- 📌 inner class 로 class truck을 생성하여 직접 bridge를 건너가는 truck 객체들로 아이디어들을 생각해 낸 것이 흥미로웠다.

- 📌 내가 풀었던 방식은 다리 길이를 큐의 공간으로 생각하여 풀었다. 즉 weight보다 작으면 waitQ에서 꺼내어 삽입하고, weight보다 크면 0을 삽입, waitQ에 대기 트럭이 없는 경우 -1을 삽입, -1을 만나면 종료하는 방식
