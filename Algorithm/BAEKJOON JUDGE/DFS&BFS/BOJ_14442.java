import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_14442 {
    static int N, M, K;
    static int[][] map;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        N = input[0];
        M = input[1];
        K = input[2];

        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        bfs();
    }

    private static void bfs() {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        int[][][] visited = new int[K + 1][N][M];
        for (int i = 0; i < K + 1; i++) {
            for (int j = 0; j < N; j++) {
                Arrays.fill(visited[i][j], Integer.MAX_VALUE);
            }
        }
        visited[0][0][0] = 1;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 0});

        while (!queue.isEmpty()) {
            int[] node = queue.poll();

            if (node[0] == N - 1 && node[1] == M - 1) {
                System.out.println(visited[node[2]][node[0]][node[1]]);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = node[0] + dx[i], ny = node[1] + dy[i];
                if(nx < 0 || nx >= N || ny < 0 || ny >= M ||  visited[node[2]][node[0]][node[1]] + 1 >= visited[node[2]][nx][ny]) continue;
                if (map[nx][ny] == 1 && node[2] < K && visited[node[2]][node[0]][node[1]] + 1 < visited[node[2] + 1][nx][ny]) {
                    visited[node[2] + 1][nx][ny] = visited[node[2]][node[0]][node[1]] + 1;
                    queue.add(new int[]{nx, ny, node[2] + 1});
                }else if(map[nx][ny] == 0) {
                    visited[node[2]][nx][ny] = visited[node[2]][node[0]][node[1]] + 1;
                    queue.add(new int[]{nx, ny, node[2]});
                }
            }
        }
        System.out.println(-1);
    }
}
