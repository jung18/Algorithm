import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int top = 0, answer = 0;
    static int[][] board;
    static boolean[][] visited;
    static int[] dy = { 0, -1, 0, 1};
    static int[] dx = { -1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                top = Math.max(top, board[i][j]);
            }
        }

        for (int h = 0; h < top; h++) { // 모든 높이에 대해서
            visited = new boolean[N][N];
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i][j] || board[i][j] <= h) {
                        continue;
                    }
                    bfs(i, j, h);
                    cnt++;
                }
            }
            answer = Math.max(cnt, answer);
        }

        System.out.println(answer);
    }

    public static void bfs(int i, int j, int h) {
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{i, j});
        visited[i][j] = true;

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            for (int d = 0; d < 4; d++) {
                int ni = poll[0] + dy[d];
                int nj = poll[1] + dx[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if (visited[ni][nj] || board[ni][nj] <= h) {
                        continue;
                    }
                    visited[ni][nj] = true;
                    q.add(new int[]{ni, nj});
                }
            }
        }
    }
}
