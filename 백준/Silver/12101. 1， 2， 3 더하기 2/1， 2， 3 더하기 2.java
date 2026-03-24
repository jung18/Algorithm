import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, k, cnt;
    static boolean stop = false;
    static List<Integer> arr = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        cnt = 0;

        backtrack(0);
        if (!stop) {
            System.out.println(-1);
        }
    }

    public static void backtrack(int sum) {
        if (stop) {
            return;
        }

        if (sum > n) { // 합이 n을 넘으면 종료
            return;
        }

        if (sum == n) {
            cnt++;
        }

        if (cnt == k) { // k번째 찾으면
            stop = true; // 종료 설정
            for (int i = 0; i < arr.size()-1; i++) {
                sb.append(arr.get(i)).append("+");
            }
            sb.append(arr.get(arr.size()-1));
            System.out.println(sb);
            return;
        }

        for (int i = 1; i < 4; i++) {
            arr.add(i);
            backtrack(sum+i);
            arr.remove(arr.size()-1);
        }
    }
}
