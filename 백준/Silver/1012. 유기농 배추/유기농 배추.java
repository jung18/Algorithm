import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int T, M, N, K;
    static int[][] board;
    static boolean[][] visited;
    static int answer;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            // 테스트 케이스별 초기화
            board = new int[N][M];
            visited = new boolean[N][M];
            answer = 0;

            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                board[Y][X] = 1;
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(!visited[i][j] && board[i][j] == 1) { // 새 배추
                        bfs(i, j);
                        answer++;
                    }
                }
            }

            System.out.println(answer);
        }
    }

    public static void bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});
        visited[i][j] = true;
        
        while (!q.isEmpty()) {
            int[] poll = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = poll[0] + dy[d];
                int nj = poll[1] + dx[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < M) { // N x M 범위
                    if (!visited[ni][nj] && board[ni][nj] == 1) { // 인접한 새 배추
                        visited[ni][nj] = true;
                        q.add(new int[]{ni, nj});
                    }
                }
            }
        }
    }

}
