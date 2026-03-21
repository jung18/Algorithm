import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int pc, node;
    static boolean[][] graph;
    static boolean[] visited;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        pc = Integer.parseInt(br.readLine());
        node = Integer.parseInt(br.readLine());

        graph = new boolean[pc+1][pc+1];
        visited = new boolean[pc+1];

        for (int i = 0; i < node; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            // 양방향
            graph[a][b] = true;
            graph[b][a] = true;
        }

        dfs(1);
        System.out.println(answer);
    }

    public static void dfs(int start) {
        visited[start] = true;

        for (int i = 1; i < pc + 1; i++) {
            if (graph[start][i] && !visited[i]) {
                answer++;
                dfs(i);
            }
        }
    }

}