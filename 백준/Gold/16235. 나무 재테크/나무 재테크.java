import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M, K;
    static int[][] board; // 땅
    static int[][] add; // 영양분
    static List<Tree> trees = new ArrayList<>(); // 나무 정보
    static Queue<Tree> dead = new LinkedList<>(); // 죽은 나무
    static int[] dy = { 0, -1, 0, 1, 1, -1, -1, 1 };
    static int[] dx = { 1, 0, -1, 0, 1, -1, 1, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[N][N];
        add = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                add[i][j] = Integer.parseInt(st.nextToken());
                board[i][j] = 5;
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            trees.add(new Tree(x-1, y-1, z, true));
        }

        // K만큼 사계절 반복
        for (int k = 0; k < K; k++) {
            spring();
            summer();
            fall();
            winter();
        }

        System.out.println(trees.size());
    }

    public static void spring() {
        // 양분이 남아있으면 성장, 없으면 죽음
        for (Tree tree : trees) {
            if (board[tree.i][tree.j] >= tree.z) {
                board[tree.i][tree.j] -= tree.z;
                tree.z++;
            } else {
                tree.alive = false;
                dead.add(tree);
            }
        }
    }

    public static void summer() {
        // 죽은 나무들 양분으로 변환
        while (!dead.isEmpty()) {
            Tree deadTree = dead.poll();
            int add = deadTree.z / 2;
            board[deadTree.i][deadTree.j] += add;
        }
    }

    public static void fall() {
        // 나무 번식, 죽은나무 삭제
        List<Tree> newTrees = new ArrayList<>();
        for (Tree tree : trees) {
            if (!tree.alive) {
                continue;
            }

            if (tree.z % 5 == 0) { // 나이가 5의 배수인 경우만
                for (int d = 0; d < 8; d++) {
                    int ni = tree.i + dy[d];
                    int nj = tree.j + dx[d];
                    // 범위 내 주위 8칸에 나이 1 의 나무 추가
                    if (0 <= ni && ni < N && 0 <= nj && nj < N) {
                        newTrees.add(new Tree(ni, nj, 1, true));
                    }
                }
            }
        }

        // 나무 목록 갱신(죽은나무 삭제 + 새 나무 추가)
        for (Tree tree : trees) {
            if (tree.alive) {
                newTrees.add(tree);
            }
        }
        trees = newTrees;
    }

    public static void winter() {
        // 각 칸에 양분 추가
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] += add[i][j];
            }
        }
    }

    static class Tree {
        int i;
        int j;
        int z;
        boolean alive;

        public Tree(int i, int j, int z, boolean alive) {
            this.i = i;
            this.j = j;
            this.z = z;
            this.alive = alive;
        }
    }

}
