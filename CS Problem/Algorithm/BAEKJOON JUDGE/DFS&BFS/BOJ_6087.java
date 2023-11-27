import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_6087 {
    static int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1};
    static char[][] map;
    static int H, W, startX, startY, endX, endY;
    static int[][][] visited;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        map = new char[H][W];
        boolean flag = false;
        visited = new int[4][H][W]; // 4방향, 높이, 넓이
        for (int i = 0; i < H; i++) {
            char[] line = br.readLine().toCharArray();
            for (int j = 0; j < W; j++) {
                map[i][j] = line[j];
                if (!flag && map[i][j] == 'C') {
                    startX = i;
                    startY = j;
                    flag = true;
                } else if (flag && map[i][j] == 'C') {
                    endX = i;
                    endY = j;
                }
            }
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < H; j++) {
                for (int k = 0; k < W; k++) {
                    visited[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }
        System.out.println(bfs(startX, startY) - 1);
    }

    private static int bfs(int x, int y) {
        Deque<int[]> queue = new LinkedList<>();
        int direct = -1;
        int mirrorCnt = 0;
        int answer = Integer.MAX_VALUE;
        queue.add(new int[]{x, y, direct, mirrorCnt});
        while (!queue.isEmpty()) {
            int[] node = queue.pollFirst();
            x = node[0];
            y = node[1];
            direct = node[2];
            mirrorCnt = node[3];
            if(mirrorCnt >= answer) continue;
            if (x == endX && y == endY) {
                answer = mirrorCnt;
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if(nx < 0 || nx >= H || ny < 0 || ny >= W  || map[nx][ny] == '*') continue;
                if(mirrorCnt >= visited[i][nx][ny]) continue;
                if (direct != i) {
                    visited[i][nx][ny] = mirrorCnt + 1;
                    queue.offer(new int[]{nx, ny, i, mirrorCnt + 1});
                } else {
                    visited[i][nx][ny] = mirrorCnt;
                    queue.offerFirst(new int[]{nx, ny, direct, mirrorCnt});
                }
            }
        }
        return answer;
    }
}