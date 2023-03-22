import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// 스트리밍 시, 누가 개강총회에 왔는지 알 수 없음,누가 자리에 끝까지 남아 있었는지 알 수 음, 스트리밍을 단숞 ㅣ틀어놓기만 했는지 알수 없음
// 출석부 관리 2가지 케이스
// 1. 총회 시작 전,시작 시간 이전에 대화를 한적이 있는 학회원 닉네임 보고 체크, 시작하자마자 채팅기록까지 가능
// 2. 끝내고 나서, 개강총회가 끝나자마자 채팅 기록을 남겼거나, 개강총회 스트리밍이 끝나자마자 채팅 기록을 남겼거나만 체크
public class BOJ_19583 {
    static int answer = 0;
    static Map<String, Boolean> recordsOfEnd = new HashMap<>();
    static Map<String, Boolean> recordsOfStart = new HashMap<>();
    public static void main(String[] args) throws Exception {
        inputValues();
        countByRecords();
        System.out.println(answer);
    }

    private static void inputValues() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] openings = br.readLine().split(" ");
        String startTime = openings[0];
        String endTime = openings[1];
        String endStreamingTime = openings[2];

        String str;

        while((str = br.readLine()) != null) {
            String[] arr = str.split(" ");
            String time = arr[0];
            String name = arr[1];

            if(startTime.compareTo(time) >= 0) {
                recordsOfStart.put(name, true);
            }else if(endTime.compareTo(time) <= 0 && endStreamingTime.compareTo(time) >= 0){
                recordsOfEnd.put(name, true);
            }
        }
    }

    private static void countByRecords() {
        for(String name : recordsOfEnd.keySet()) {
            if(recordsOfStart.containsKey(name)) answer++;
        }
    }
}