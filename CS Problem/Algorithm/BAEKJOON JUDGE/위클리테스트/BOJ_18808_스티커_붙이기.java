import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class BOJ_18808_스티커_붙이기 {
    static List<int[][]> stickers = new LinkedList<>();
    static int[][] map;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = input[0], M = input[1], K = input[2];
        map = new int[N][M];
        int answer = 0;

        for (int i = 0; i < K; i++) { // 각 스티커 배열에 집어 넣기
            input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[][] arr = new int[input[0]][input[1]];
            for (int j = 0; j < arr.length; j++) {
                arr[j] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            stickers.add(arr);
        }

        start(N, M);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(map[i][j] == 1) answer++;
            }
        }
        System.out.println(answer);
    }

    private static void start(int N, int M) {
        for (int[][] sticker : stickers) {
            checkValidate(sticker, N, M);
        }
    }

    private static void checkValidate(int[][] sticker, int N, int M) {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (bfs(j, k, sticker)) {
                        attacheSticker(j, k, sticker);
                        return;
                    }
                }
            }
            sticker = rotate(sticker);
        }
    }

    private static void attacheSticker(int startX, int startY, int[][] sticker) {
        for (int i = 0; i < sticker.length; i++) {
            for (int j = 0; j < sticker[0].length; j++) {
                if(sticker[i][j] == 0) continue;
                map[i + startX][j + startY] = 1;
            }
        }
    }
    private static boolean bfs(int startX, int startY, int[][] sticker) {
        for (int i = 0; i < sticker.length; i++) {
            for (int j = 0; j < sticker[0].length; j++) {
                if(startX + i < 0 || startX + i >= map.length || startY + j < 0 || startY + j >= map[0].length) {
                    return false;
                }
                if(sticker[i][j] == 0) continue;
                if(map[i + startX][j + startY] == 1) return false;
            }
        }
        return true;
    }

    private static int[][] rotate(int[][] arr) { // 90도 씩 회전 하는 메서드
        int row = arr.length;
        int column = arr[0].length;
        int[][] newArr = new int[column][row];

        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                newArr[i][j] = arr[row - j - 1][i];
            }
        }
        return newArr;
    }
}