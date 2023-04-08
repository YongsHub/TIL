import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Combinations 문제 -> 조합에 대한 활용 이해
 * 중복 처리 -> HashMap 자료구조 활용
 */
public class BOJ_16722_결합 {
    static List<Picture> pictures = new ArrayList<>();
    static boolean[] visited = new boolean[9];
    static int[] arr = new int[3];
    static Map<String, Boolean> cases = new HashMap<>();
    static int possibleCnt = 0;
    public static void main(String[] args) throws Exception {
        String[] input;
        int gameCount;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb;
        int[] numbers = new int[3];

        for (int i = 0; i < 9; i++) {
            input = br.readLine().split(" ");
            pictures.add(new Picture(input[0], input[1], input[2]));
        }
        // 3개를 고르는 조합 중에 합이 되는 경우를 전부 체크
        combinations(0, 0, 3);
        gameCount = Integer.parseInt(br.readLine());
        boolean getThreePoint = false;
        Map<String, Boolean> temp = new HashMap<>();
        int point = 0;
        int curSumCnt = 0;
        for (int i = 0; i < gameCount; i++) {
            input = br.readLine().split(" ");
            if(input[0].equals("H")) { // H라면
                sb = new StringBuilder();
                numbers[0] = Integer.parseInt(input[1]) - 1;
                numbers[1] = Integer.parseInt(input[2]) - 1;
                numbers[2] = Integer.parseInt(input[3]) - 1;
                Arrays.sort(numbers);
                sb.append(numbers[0]).append(numbers[1]).append(numbers[2]);
                if(cases.get(sb.toString()) && !temp.containsKey(sb.toString())) {
                    point++;
                    curSumCnt++;
                } else {
                  point--;
                }
                temp.put(sb.toString(), true);
            } else { // G라면
                if(possibleCnt == curSumCnt && !getThreePoint) {
                    point += 3;
                    getThreePoint = true;
                } else {
                    point--;
                }
            }
        }

        System.out.println(point);
    }

    private static void combinations(int start, int cnt, int R) {
        if (cnt == R) {
            //합이 되는지 체크
            checkValidateSum();
            return;
        }

        for (int i = start; i < 9; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            arr[cnt] = i;
            combinations(i + 1, cnt + 1, R);
            visited[i] = false;
        }
    }

    private static void checkValidateSum() {
        Picture picture1 = pictures.get(arr[0]);
        Picture picture2 = pictures.get(arr[1]);
        Picture picture3 = pictures.get(arr[2]);
        Arrays.sort(arr);
        StringBuilder key = new StringBuilder();
        key.append(arr[0]).append(arr[1]).append(arr[2]);
        Set<String> colorSet = new HashSet<>();
        Set<String> shapeSet = new HashSet<>();
        Set<String> backgroundSet = new HashSet<>();

        colorSet.add(picture1.color);colorSet.add(picture2.color);colorSet.add(picture3.color);
        shapeSet.add(picture1.shape);shapeSet.add(picture2.shape);shapeSet.add(picture3.shape);
        backgroundSet.add(picture1.background);backgroundSet.add(picture2.background);backgroundSet.add(picture3.background);
        if(colorSet.size() != 1 && colorSet.size() != 3) {
            cases.put(key.toString(), false);
            return;
        }
        if(shapeSet.size() != 1 && shapeSet.size() != 3) {
            cases.put(key.toString(), false);
            return;
        }
        if (backgroundSet.size() != 1 && backgroundSet.size() != 3) {
            cases.put(key.toString(), false);
            return;
        }
        cases.put(key.toString(), true);
        possibleCnt++;
    }
}

class Picture {
    String color;
    String shape;
    String background;

    public Picture(String shape, String color, String background) {
        this.color = color;
        this.shape = shape;
        this.background = background;
    }
}