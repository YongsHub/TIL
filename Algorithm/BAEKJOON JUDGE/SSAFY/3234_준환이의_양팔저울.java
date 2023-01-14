
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class SW_3234 {
    static int[] weights;
    static List<ArrayList<Integer>> results;
    static int N;
    static boolean[] visited = new boolean[1001];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T;
        int left, right;

        T=Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++) {
            results = new ArrayList<>();
            N = Integer.parseInt(br.readLine());
            weights = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            permutations(0, new ArrayList<Integer>());
            for(ArrayList<Integer> arr : results) {
                System.out.println(arr);
            }
        }
    }

    public static void permutations(int cnt, ArrayList<Integer> arr) {
        if(cnt == N) {
            results.add(new ArrayList<>(arr));
            return;
        }

        for(int i = 0; i < N; i++) {
            if(visited[weights[i]]) {
                continue;
            }
            visited[weights[i]] = true;
            arr.add(weights[i]);
            permutations(cnt + 1, arr);
            visited[weights[i]] = false;
            arr.remove(arr.size() - 1);
        }
    }
}