import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_2636 {
    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int totalCnt = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = input[0], M = input[1];
        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j = 0; j < M; j++) {
                map[i][j] = input[j];
                if(map[i][j] == 1) totalCnt++;
            }
        }

        bfs(N, M);
    }

    private static void bfs(int N, int M) {
        int time = 0, cnt = totalCnt;
        while (totalCnt > 0) {
            Queue<int[]> queue = new LinkedList<>();
            Queue<int[]> cheeses = getCheese(queue, N, M);
            totalCnt -= cheeses.size();
            if(totalCnt > 0) cnt = totalCnt;
            time++;
            changeCheeseToAir(cheeses);
        }

        System.out.println(time);
        System.out.println(cnt);
    }

    private static void changeCheeseToAir(Queue<int[]> cheeses) {
        for (int[] node : cheeses) {
            map[node[0]][node[1]] = 0;
        }
    }

    private static Queue<int[]> getCheese(Queue<int[]> queue, int N, int M) {
        boolean[][] visited = new boolean[N][M];
        Queue<int[]> cheeses = new LinkedList<>();
        visited[0][0] = true;
        queue.add(new int[]{0, 0});

        while (!queue.isEmpty()) {
            int[] node = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = node[0] + dx[i], ny = node[1] + dy[i];
                if(nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) continue;
                if(map[nx][ny] == 1) {
                    cheeses.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
                else if(map[nx][ny] == 0) {
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return cheeses;
    }
}
