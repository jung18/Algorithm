import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] arr, path;
    static int K;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());

            if (K == 0) {
                break;
            }

            arr = new int[K];
            path = new int[6]; // 6개 조합만

            for (int i = 0; i < K; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            collections(0, 0);
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void collections(int i, int start) {
        if (i == 6) {
            for (int k = 0; k < 6; k++) {
                sb.append(path[k]).append(" ");
            }

            sb.append("\n");
            return;
        }
        for (int k = start; k < K; k++) {
            path[i] = arr[k];
            collections(i+1, k+1);
        }
    }

}