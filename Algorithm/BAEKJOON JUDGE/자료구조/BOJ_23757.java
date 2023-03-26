import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

// N개의 선물 상자, 아이들 M명 아이가 1번부터 현재 선물이 가장 많이 담겨 있는 상자에서 원하는 만큼 선물을 가져간다. 누가 가져갔던 상자에서 또 가져가도 상관없음
// 자신이 원하는것보다 적은 개수의 선물이 들어있으면 가져가지 못함
// 실망하지 않고 ㅁ모두 선물을 가져갈 수 있는지
public class BOJ_23757 {
    static int N, M;
    static int[] gift;
    static int[] wants;
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
    public static void main(String[] args) throws Exception {
        inputValues();
        check();
    }

    private static void check() {
        for(int i = 0; i < M; i++) {
            int cnt = pq.poll();
            if(wants[i] > cnt) {
                System.out.println(0);
                return;
            }
            pq.add(cnt - wants[i]);
        }
        System.out.println(1);
    }

    private static void inputValues() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        N = input[0];
        M = input[1];

        gift = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        wants = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for(int cnt : gift) pq.add(cnt);
    }
}