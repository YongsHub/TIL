import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>(); // 해쉬 맵 선언

        for (String name : participant) {
            if (map.containsKey(name)) { // 동명이인이 있다는 것을 고려하기 위해서
                int value = map.get(name); // p의 value 값을 저장
                value += 1;
                map.put(name, value);
                continue; // 추가해주고 바로 반복문 실행
            }

            map.put(name, 1);
        }

        for (String name : completion) {
            if (map.containsKey(name)) { // 완주자 이름을 포함하고 있다면
                int value = map.get(name);
                value -= 1;
                map.put(name, value);
            }
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() != 0) {
                return entry.getKey();
            }
        }
        return answer;
    }
}