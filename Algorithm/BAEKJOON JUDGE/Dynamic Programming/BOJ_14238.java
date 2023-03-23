import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_14238 {
	static String[] input;
	static char[] ans;
	static boolean[][][][] dp;
	static int[] alphabets;
	
	public static void main(String[] args) throws Exception {
		inputValues();
		if(dynamicProgramming(0, 0, 0, 0)) {
			for(int i = 0; i < input.length; i++) {
				System.out.print(ans[i]);
			}
		}else System.out.println(-1);
	}
	
	private static void inputValues() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		alphabets = new int[3];
		input = br.readLine().split("");
		ans = new char[input.length];
		dp = new boolean[input.length][input.length][input.length][input.length];
		for(String alpha : input) {
			if(alpha.equals("A")) alphabets[0]++;
			else if(alpha.equals("B")) alphabets[1]++;
			else if(alpha.equals("C")) alphabets[2]++;
		}
	}
	
	private static boolean dynamicProgramming(int x, int c, int b, int a) {
		if (x == input.length) {
			return true;
		}
		if (dp[x][c][b][a] == true)
			return false;

		dp[x][c][b][a] = true;

		if (alphabets[2] > c) {
			if ((x >= 2 && (ans[x - 1] != 'C' && ans[x - 2] != 'C')) ||
					(x == 1 && ans[x - 1] != 'C') || x == 0) {
				ans[x] = 'C';
				if (dynamicProgramming(x + 1, c + 1, b, a))
					return true;
			}
			else dp[x][c][b][a] = false;
		}
		
		if (alphabets[1] > b) {
			if ((x >= 1 && ans[x - 1] != 'B') || x == 0) {
				ans[x] = 'B';
				if (dynamicProgramming(x + 1, c, b + 1, a))
						return true;
			}else
				dp[x][c][b][a] = false;
		}
		if (alphabets[0] > a) {
			ans[x] = 'A';
			if (dynamicProgramming(x + 1, c, b, a + 1))
				return true;
		}

		return false;
	}
}
