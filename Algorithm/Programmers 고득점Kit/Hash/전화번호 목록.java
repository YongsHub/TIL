import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<String, Integer>(); // 해쉬맵 클래스생성
        Queue<String> queue = new LinkedList<>();
        int length;
        for (String number : phone_book) {
            map.put(number, number.length());
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            length = entry.getValue();

            for (int i = length - 1; i > 0; i--) {
                String str = entry.getKey().substring(0, i);
                if (map.containsKey(str))
                    return false;
            }
        }
        return answer;
    }
}
// import java.util.*;

// class Solution {
// public boolean solution(String[] phone_book) {
// boolean answer = true;
// HashMap<Integer, String> map = new HashMap<Integer, String>(); // 해쉬맵 클래스 생성

// /* 해쉬 맵에 일단 데이터 삽입 */
// int num = 0;
// for (String phone : phone_book) {
// map.put(num, phone); // key값 Integer, value 값 : String으로 삽입
// num++;
// }

// for (Map.Entry<Integer, String> entry : map.entrySet()) {
// String number1 = entry.getValue();
// for (Map.Entry<Integer, String> compareNumber : map.entrySet()) {
// String comparedNumber = compareNumber.getValue();
// if ((entry.getKey() != compareNumber.getKey()) && number1.length() <=
// comparedNumber.length()) {
// if (number1.equals(comparedNumber.substring(0, number1.length()))) {
// return false;
// }
// }
// }
// }
// return answer;
// }
// }

/*
 * import java.util.*;
 * 
 * 
 * class Solution {
 * public boolean solution(String[] phone_book) {
 * boolean answer = true;
 * HashMap<String , Integer> map = new HashMap<String , Integer>(); // 해쉬맵 클래스
 * 생성
 * Queue<String> queue = new LinkedList<>();
 * int length = phone_book[0].length();
 * 
 * 
 * for(String number : phone_book){ // 전화번호 길이 중, 최소 길이를 구한다.
 * if(length >= number.length()){
 * length = number.length();
 * }
 * }
 * 
 * for(String number : phone_book){
 * if(number.length() == length){
 * queue.add(number); // length와 길이가 같은 배열 요소를 array에 저장
 * }else{
 * map.put(number.substring(0,length),0); // 전부 length와 길이만큼 0부터length길이까지 잘라서
 * 해쉬맵에 저장
 * }
 * }
 * 
 * for(String number : queue){
 * if(map.containsKey(number)) return false;
 * }
 * return answer;
 * }
 * }
 */