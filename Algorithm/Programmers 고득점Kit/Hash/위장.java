
import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();

        for (String[] cloth : clothes) {
            if (map.containsKey(cloth[1])) { // 같은 키가 배열에 존재한다면, 갯수 추가
                int num = map.get(cloth[1]);
                num += 1;
                map.put(cloth[1], num);
                continue;
            }
            map.put(cloth[1], 2); // 선택하지 않는 경우까지 생각해서 2
        }
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            answer = answer * entry.getValue();
        }
        answer -= 1; // 전체 다 선택 안하는 경우 - 1
        return answer;
    }
}