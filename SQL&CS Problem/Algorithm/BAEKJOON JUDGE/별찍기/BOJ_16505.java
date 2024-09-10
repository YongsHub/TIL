import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static char[][] stars = new char[1][1];
    static int n;
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        stars[0][0] = '*';

        stars = makeStar(1);
        int size = (int)Math.pow(2, n);
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < (size - i); j++) {
                sb.append(stars[i][j]);
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

    public static char[][] makeStar(int start) {
        char[][] newStars;
        int size = (int) Math.pow(2, start);
        if(start == n + 1) {
            return stars;
        }
        newStars = new char[size][size];
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                newStars[i][j] = ' ';
            }
        }
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                if(j < size - i) {
                    newStars[i][j] = stars[i % (size/2)][j % (size/2)];
                }
            }
        }
        stars = newStars;
        return  makeStar(start + 1);
    }
}