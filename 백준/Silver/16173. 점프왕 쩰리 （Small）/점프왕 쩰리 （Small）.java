import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int[][] board;
    private static int N;
    private static boolean answer = false;

    public static void dfs(int i, int j) {
        if (i == N-1 && j == N-1) {
            answer = true;
            return;
        }
        if (0 <= i && i < N && 0 <= j && j < N) {
            int next = board[i][j];

            if (next == 0) {
                return;
            }

            dfs(i + next, j);
            dfs(i, j + next);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 0);
        if (answer) {
            System.out.println("HaruHaru");
        } else {
            System.out.println("Hing");
        }
    }
}