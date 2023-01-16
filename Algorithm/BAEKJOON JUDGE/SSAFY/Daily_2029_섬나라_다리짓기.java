import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Daily_2029_섬나라_다리짓기 {
    static int maxLength = 1;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] arr;
    static int N;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(arr[i][j] == 1) {
                    getMaxLength(i, j);
                }
            }
        }
        System.out.println(maxLength);
    }

    public static void getMaxLength(int x, int y) {
        int maxValue = 0;
        for(int i = 0; i < 4; i++) {
            int value = 0;
            int nx = x;
            int ny = y;
            do {
                nx = nx + dx[i];
                ny = ny + dy[i];
                if(checkIndexBound(nx, ny)) {
                    break;
                }
                value++;
            }while(arr[nx][ny] != 1);
            maxValue = Math.max(maxValue, value);
        }

        maxLength = Math.max(maxLength, maxValue);
    }

    public static boolean checkIndexBound(int x, int y) {
        return x < 0 || x >= N || y < 0 || y >= N;
    }
}
