import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] path, arr;
    static int N, M;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        path = new int[M];

        for (int i = 0; i < N; i++) {
            arr[i] = i+1;
        }

        combination(0);
        System.out.println(sb);
    }

    public static void combination(int depth) {
        if (depth == M) {
            for (int p : path) {
                sb.append(p).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = 0; i < N; i++) {
            path[depth] = arr[i];
            combination(depth+1);
        }
    }
}
