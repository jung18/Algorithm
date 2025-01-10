import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N;
    private static int M;
    private static int V;
    private static boolean[] visited;
    private static Map<Integer, List<Integer>> graph;

    public static void dfs(int node) {
        if (visited[node]) {
            return;
        }
        visited[node] = true;
        System.out.printf("%d ", node);

        List<Integer> next = graph.get(node);
        if (next == null) {
            return;
        }

        for (Integer i : next) {
            dfs(i);
        }
    }

    public static void bfs(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(node);

        while (!queue.isEmpty()) {
            int curNode = queue.poll();
            visited[curNode] = true;
            System.out.printf("%d ", curNode);

            List<Integer> next = graph.get(curNode);
            if (next != null) {
                for (Integer i : next) {
                    if (!visited[i]) {
                        queue.offer(i);
                        visited[i] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        visited = new boolean[N + 1];
        graph = new HashMap<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            Integer parent = Integer.parseInt(st.nextToken());
            Integer child = Integer.parseInt(st.nextToken());
            // 양방향
            graph.putIfAbsent(parent, new ArrayList<>());
            graph.get(parent).add(child);

            graph.putIfAbsent(child, new ArrayList<>());
            graph.get(child).add(parent);
        }

        // sort
        for (Map.Entry<Integer, List<Integer>> entry : graph.entrySet()) {
            List<Integer> values = graph.get(entry.getKey());
            Collections.sort(values);
        }

        // dfs, bfs
        dfs(V);
        visited = new boolean[N + 1];
        System.out.println();
        bfs(V);
    }
}