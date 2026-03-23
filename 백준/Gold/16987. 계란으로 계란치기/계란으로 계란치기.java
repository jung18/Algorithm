import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, answer;
    static Egg[] eggs;

    static class Egg {
        int s; // 내구도
        int w; // 무게
        boolean broken = false;

        public Egg(int s, int w) {
            this.s = s;
            this.w = w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        eggs = new Egg[N];
        answer = 0;

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            eggs[i] = new Egg(s, w);
        }

        backtrack(0, 0);
        System.out.println(answer);
    }

    public static void backtrack(int depth, int cnt) {
        if (depth == N) { // 마지막 계란일 때
            answer = Math.max(answer, cnt);
            return;
        }

        if (eggs[depth].broken || cnt == N-1) { // 손에 든 계란 깨짐 or 깨지지 않은 계란 없음
            backtrack(depth+1, cnt);
            return;
        }

        int tmp = cnt;
        for (int i = 0; i < N; i++) {
            if (depth == i || eggs[i].broken) { // 자기 자신 or 깨진 계란
                continue;
            }
            attack(depth, i);
            // 깨지면 카운트 +1
            if (eggs[i].broken) {
                cnt++;
            }
            if (eggs[depth].broken) {
                cnt++;
            }
            backtrack(depth+1, cnt);
            // 값 복구
            restore(depth, i);
            cnt = tmp;
        }
    }

    public static void attack(int depth, int i) {
        eggs[depth].s -= eggs[i].w;
        eggs[i].s -= eggs[depth].w;
        if (eggs[depth].s <= 0) {
            eggs[depth].broken = true;
        }
        if (eggs[i].s <= 0) {
            eggs[i].broken = true;
        }
    }

    public static void restore(int depth, int i) {
        eggs[depth].s += eggs[i].w;
        eggs[i].s += eggs[depth].w;
        if (eggs[depth].s > 0) {
            eggs[depth].broken = false;
        }
        if (eggs[i].s > 0) {
            eggs[i].broken = false;
        }
    }
}
