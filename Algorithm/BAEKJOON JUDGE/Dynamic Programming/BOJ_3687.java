import java.io.*;
import java.util.*;

public class BOJ_3687 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        long[] dp = new long[101];
        Arrays.fill(dp, Long.MAX_VALUE);
        getMinNumber(dp);
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());

            long minNumber = dp[n];
            String maxNumber = getMaxNumber(n);
            sb.append(minNumber).append(" ").append(maxNumber).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static String getMaxNumber(int n) {
        StringBuilder sb = new StringBuilder();
        int length = n / 2;

        if ((n & 1) == 1) { // 홀수라면
            sb.append("7");
        } else {
            sb.append("1");
        }

        sb.append("1".repeat(Math.max(0, length - 1)));
        return sb.toString();
    }

    private static void getMinNumber(long[] dp) {
        dp[2] = 1;
        dp[3] = 7;
        dp[4] = 4;
        dp[5] = 2;
        dp[6] = 6;
        dp[7] = 8;
        dp[8] = 10;

        String[] add = {"1", "7", "4", "2", "0", "8"};

        for (int i = 9; i <= 100; i++) {
            for (int j = 2; j <= 7; j++) {
                String cur = dp[i - j] + add[j - 2];
                dp[i] = Math.min(dp[i], Long.parseLong(cur));
            }
        }
    }
}