import java.util.*;


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Queue<Integer> q = new LinkedList<>(); // 큐 선언
        List<Integer> answerList = new ArrayList<>(); // return 배열을 담기 위한 리스트
        
        for(int i = 0; i<progresses.length;i++){ // 작업 갯수 만큼 반복한다.
            double days = (100 - progresses[i]) / (double)speeds[i]; // 남은 진도를 개발 속도로 나누면 일수를 알 수 있다.
            int date = (int)Math.ceil(days); // ex) 2.xx 이면 3일 째 기능이 개발된다.
            
            if(!q.isEmpty() && q.peek() < date){ // 큐가 비어있지 않고, 큐의 맨 앞의 요소가 현재 남은 일수보다 작으면 조건문을 만족한다.
                answerList.add(q.size()); // 정답리스트에 큐의 크기만큼 추가
                q.clear(); // 큐 초기화 시킴
            }
            
            q.offer(date); // 조건문에 걸리지 않으면 큐에 date 값 삽입
        }
        answerList.add(q.size()); // 큐에 데이터가 있으면 크기만큼 answerList에 추가
        int[] answer = new int[answerList.size()]; // answer 배열을 answerList사이즈만큼 선언
        
        for(int i=0;i<answer.length;i++){
            answer[i] = answerList.get(i); // answer 배열에 answerList의 요소값을 저장한다.
        }
        return answer;
    }
}
