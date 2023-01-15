import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution
{
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visited;
    static int[][] arr;
    static int N;
    static int answer;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T;
        T = Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

        for(int test_case = 1; test_case <= T; test_case++) {
            N = Integer.parseInt(br.readLine());
            answer = Integer.MAX_VALUE;
            arr = new int[N][N];
            visited = new boolean[N][N];

            for(int i = 0; i < N; i++) {
                String st = br.readLine();
                for(int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(String.valueOf(st.charAt(j)));
                }
            }

            System.out.printf("#%d %d\n", test_case, dfs(0, 0, 0));
        }
    }

    public static int dfs(int x, int y, int cost) {
        if(x == N - 1 && y == N - 1) {
            return Math.min(answer, cost);
        }
        if(x < 0 || x >= N || y < 0 || y >= N || visited[x][y]) {
            return answer;
        }
        cost += arr[x][y];
        visited[x][y] = true;
        answer = Math.min(answer, dfs(x -1, y, cost));
        answer = Math.min(answer, dfs(x + 1, y, cost));
        answer = Math.min(answer, dfs(x, y - 1, cost));
        answer = Math.min(answer, dfs(x, y + 1, cost));
        visited[x][y] = false;
        return answer;
    }
}