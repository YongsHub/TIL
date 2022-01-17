import java.util.*;


class Solution {
    public int solution(int[] priorities, int location) {
        int num = priorities[location]; // 중요도 배열에 index가 location인 배열 값을 저장한다.
        Queue<Integer> q_location = new LinkedList<>(); // q라는 큐 선언
        Queue<Integer> q_data = new LinkedList<>(); // q라는 큐 선언
        int order = 1; // 순서를 저장하기 위한 변수
        int answer = 0;
        boolean check;
        
        for(int i = 0; i < priorities.length; i++){ // 제한사항 첫 번째를 만족해야 한다.
            q_location.offer(i); // 큐에 0부터 ~ 배열 크기까지 저장한다.
            q_data.offer(priorities[i]); // 실제 값 저장
        }
        
        while(!q_data.isEmpty()){ // 큐가 비어있지 않을 때
            int first = q_data.peek(); // 큐의 첫번째 값 저장
            int first_location = q_location.peek();
            
            if(first < Arrays.stream(priorities).max().getAsInt()){ // 문서 J보다 중요도가 높은 문서가 존재한다면
                check = true;
                q_data.poll(); // 가장 앞에 있는 문서J 대기목록에서 꺼내고
                q_location.poll();
                q_data.offer(first); // 맨 뒤로 저장
                q_location.offer(first_location);
            }else{
                check = false;
                for(int i=0; i<priorities.length; i++){
                    if(priorities[i] == first){
                        priorities[first_location] = 0; // 최대값이 큐에서 삭제될 것이기에 priorities에서 값을 0으로 둔다.
                    }
                }
            }
            
            if(!check && first == num && first_location == location){
                answer = order;
                return answer;
            }else if(!check){
                q_data.poll(); // 문서 J 삭제하고
                q_location.poll();
                order++; // order 값 증가시킨다.
            }
        }
        return answer;
    }
}
