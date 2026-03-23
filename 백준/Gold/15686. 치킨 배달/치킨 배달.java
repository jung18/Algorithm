import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M;
    static int answer = Integer.MAX_VALUE;
    static int[][] board;
    static boolean[] path; // 치킨집 선택 여부
    static List<Point> chickens = new ArrayList<>(); // 치킨집 목록
    static List<Point> homes = new ArrayList<>(); // 집 목록


    static class Point {
        int i;
        int j;

        public Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                // 치킨집, 집 좌표 저장
                if (board[i][j] == 1) {
                    homes.add(new Point(i, j));
                } else if (board[i][j] == 2) {
                    chickens.add(new Point(i, j));
                }
            }
        }
        path = new boolean[chickens.size()]; // 치킨집 갯수만큼

        backtrack(0, 0);
        System.out.println(answer);
    }

    // 치킨집 조합 뽑기 + 치킨거리 계산
    public static void backtrack(int depth, int start) {
        if (depth == M) {
            int tempDistance = 0;

            for (int i = 0; i < homes.size(); i++) {
                // 각 집별 치킨거리 계산 후 합산
                int tempMin = Integer.MAX_VALUE;
                for (int j = 0; j < chickens.size(); j++) {
                    if (!path[j]) { // 선택한 치킨집만 계산
                        continue;
                    }
                    int dis = Math.abs(chickens.get(j).i - homes.get(i).i) + Math.abs(chickens.get(j).j - homes.get(i).j);
                    tempMin = Math.min(tempMin, dis);
                }
                tempDistance += tempMin;
            }
            // 가장 작은 치킨거리 누적
            answer = Math.min(answer, tempDistance);
            return;
        }

        for (int i = start; i < chickens.size(); i++) {
            path[i] = true;
            backtrack(depth+1, i+1);
            path[i] = false;
        }
    }
}
