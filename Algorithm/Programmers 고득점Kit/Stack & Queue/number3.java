import java.util.*;

class Solution {
    int weight; // 견딜 수 있는 무게 변수
    int bridge_length; // 다리 길이
    int answer; // 경과 시간
    Queue<Integer> wait_queue;
    Queue<Integer> passing_queue;

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        /*
         * bridge_length : 최대 지나갈 수 있는 트럭 개수 weight: 다리가 견딜 수 있는 무게 truck_weights : 대기트럭
         */
        this.weight = weight;
        this.bridge_length = bridge_length;
        this.answer = 0;
        wait_queue = new LinkedList<>(); // 대기 트럭
        passing_queue = new LinkedList<>(); // 다리를 건너는 트럭
        for (int i : truck_weights) { // 대기 트럭 큐에 삽입
            wait_queue.offer(i);
        }

        insert_truck(); // 먼저 삽입

        while (!passing_queue.isEmpty()) {
            if (move())
                return answer;
        }
        return answer;
    }

    public boolean insert_truck() { // 트럭을 삽입하기 위한 메서드
        while (!wait_queue.isEmpty()) {
            if (this.weight - wait_queue.peek() >= 0) { // 삽입되는 것이 버틸 수 있는 무게라면
                passing_queue.offer(wait_queue.peek()); // 대기 트럭 맨 앞 삽입
                this.weight -= wait_queue.peek();
                wait_queue.poll(); // 대기 트럭 맨 앞 삭제
                answer++; // 경과 시간 + 1
                return false;
            } else {
                passing_queue.offer(0); // 0삽입
                answer++; // 경과 시간 + 1
                return false;
            }
        }
        if (passing_queue.peek() == -1) { // -1이 맨 앞에 온다면 종료시킨다.
            answer++;
            return true;
        }
        passing_queue.offer(-1); // -1 삽입
        answer++; // 경과 시간 + 1
        return false;
    }

    public boolean move() {
        if (passing_queue.size() == this.bridge_length && passing_queue.peek() == 0) {
            passing_queue.poll(); // 0 제거 해준다.
        } else if (passing_queue.size() == this.bridge_length && passing_queue.peek() != 0) {
            this.weight += passing_queue.peek(); // 나갈 트럭의 weight만큼 다시 더해준다.
            passing_queue.poll(); // 트럭 내보낸다.
        } else {
            if (insert_truck())
                return true;
        }
        return false;
    }
}