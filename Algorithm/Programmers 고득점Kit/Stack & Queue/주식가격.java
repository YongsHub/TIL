import java.util.*;


class Solution {

    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Queue<Integer> queue = new LinkedList<>();

        for(int i=0; i<prices.length; i++){
            int sec = 0; // 초
            for(int j=i+1; j<prices.length; j++){
                if(prices[i] <= prices[j]){ // 가격이 떨어지지 않는다면
                    sec++;
                }else{ // 가격이 떨어졌다면
                    sec++;
                    break;
                }
            }
            answer[i] = sec;
        }
        return answer;
    }
}





