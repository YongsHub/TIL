import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
//투 포인터 활용
//종류에 따른 배열을 만들어서 중복 시 해당 인덱스에 대해 늘림
public class BOJ_15961 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = input[0],  d = input[1], k = input[2], c = input[3]; // N : 접시의 수, d : 초밥의 가짓수, k : 연속해서 먹는 접시의 수, c : 쿠폰 번호
        int[] sushi = new int[N];
        int answer = 0;
        int[] types = new int[d + 1];
        int curCnt = 0;

        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        int start = 0, end = 0;

        while (start < N) {
            if(Math.abs(end - start) >= k) {
                if(types[c] == 0) {
                    answer = Math.max(answer, curCnt + 1);
                } else {
                    answer = Math.max(answer, curCnt);
                }
                types[sushi[start]]--;
                if(types[sushi[start]] == 0) curCnt--;
                start++;
            }
            if(types[sushi[end]] == 0) {
                types[sushi[end]]++;
                curCnt++;
            } else {
              types[sushi[end]]++;
            }
            end = (end + 1 >= N) ? (end + 1) % N : end + 1;
        }
        System.out.println(answer);
    }
}
