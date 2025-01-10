import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N;
    private static int M;
    private static int[][] board;
    private static int min = Integer.MAX_VALUE;
    private static int[][] dir = new int[][]{{1, -1}, {1, 0}, {1, 1}};

    public static void dfs(int i, int j, int tmp, int preDir) {
        if (i == N-1) {
            min = Math.min(min, tmp);
            return;
        }

        if (tmp >= min) {
            return;
        }

        if (preDir == 3) {
            for (int k = 0; k < 3; k++) {
                processNextDfs(i, j, tmp, k);
            }
        } else {
            for (int k = 0; k < 3; k++) {
                if (k != preDir) {
                    processNextDfs(i, j, tmp, k);
                }
            }
        }
    }

    private static void processNextDfs(int i, int j, int tmp, int k) {
        int ni = i + dir[k][0];
        int nj = j + dir[k][1];
        if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
            dfs(ni, nj, tmp + board[ni][nj], k);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int j = 0; j < M; j++) {
            dfs(0, j, board[0][j], 3);
        }

        System.out.println(min);
    }
}