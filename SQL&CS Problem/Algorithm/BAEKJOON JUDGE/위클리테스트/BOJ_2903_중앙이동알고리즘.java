import java.util.Scanner;
/**
 * 점화식을 찾아내면 풀 수 있는 문제
 */
public class BOJ_2903_중앙이동알고리즘 {
    public static void main(String[] args) {
        int[] value = new int[16];
        Scanner sc = new Scanner(System.in);
        value[1] = 9;
        int start = 3, num = 1;
        for (int i = 2; i < 16; i++) {
            num *= 2;
            int temp = start + num;
            value[i] = temp * temp;
            start = temp;
        }

        int n = sc.nextInt();
        System.out.println(value[n]);
    }
}