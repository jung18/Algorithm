import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int[][] board;
    static boolean[][] visited;
    static List<Integer> answers = new ArrayList<>();
    static int[] dy = {0, -1, 0, 1};
    static int[] dx = {1, 0,  -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            String[] row = br.readLine().split("");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // 새 집 발견시 bfs 시작
                if (board[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j);
                }
            }
        }

        Collections.sort(answers);
        System.out.println(answers.size());
        for (int answer : answers) {
            System.out.println(answer);
        }
    }

    public static void bfs(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});
        visited[i][j] = true;
        int cnt = 1;

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            for (int d = 0; d < 4; d++) {
                int ni = poll[0] + dy[d];
                int nj = poll[1] + dx[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if (visited[ni][nj] || board[ni][nj] == 0) {
                        continue;
                    }
                    visited[ni][nj] = true;
                    queue.add(new int[]{ni, nj});
                    cnt++;
                }
            }
        }
        answers.add(cnt);
    }
}
