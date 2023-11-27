import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class BOJ_2852 {
    static int N;
    static int[] scores = new int[3];
    static Map<String, Integer> times = new HashMap<>();
    public static void main(String[] args) throws Exception {
        inputValues();
        startGame();
        StringBuilder sb;
        if(scores[1] > 0) {
            sb = new StringBuilder();
            int min = scores[1] / 60;
            if(min < 10) {
                sb.append(0);
                sb.append(min);
                sb.append(":");
            }else {
                sb.append(min);
                sb.append(":");
            }
            int sec = scores[1] % 60;
            if(sec < 10) {
                sb.append(0);
                sb.append(sec);
            }else {
                sb.append(sec);
            }
            System.out.println(sb);
        } else {
            System.out.println("00:00");
        }
        if(scores[2] > 0) {
            sb = new StringBuilder();
            int min = scores[2] / 60;
            if(min < 10) {
                sb.append(0);
                sb.append(min);
                sb.append(":");
            }else {
                sb.append(min);
                sb.append(":");
            }
            int sec = scores[2] % 60;
            if(sec < 10) {
                sb.append(0);
                sb.append(sec);
            }else {
                sb.append(sec);
            }
            System.out.println(sb);
        }else {
            System.out.println("00:00");
        }
    }

    private static void inputValues() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String[] input;
        for(int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            times.put(input[1], Integer.parseInt(input[0]));
        }
    }

    private static void startGame() {
        int min = 0, sec = 0;
        int cntA = 0;
        int cntB = 0;

        for(; min < 48; min++) {
            for(int i = 0; i < 60; i++) {
                StringBuilder sb = new StringBuilder();
                if(min < 10) {
                    sb.append(0);
                    sb.append(min);
                    sb.append(":");
                }else {
                    sb.append(min);
                    sb.append(":");
                }

                if(sec < 10) {
                    sb.append(0);
                    sb.append(sec);
                }else {
                    sb.append(sec);
                }
                if(times.containsKey(sb.toString())) {
                    int winTeam = times.get(sb.toString());
                    if(winTeam == 1) cntA++;
                    else cntB++;
                }
                if(cntA > cntB) scores[1]++;
                else if(cntB > cntA) scores[2]++;
                sec++;
            }
            sec = 0;
        }
    }
}