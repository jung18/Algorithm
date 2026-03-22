import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int L, C;
    static String[] arr, path;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new String[C];
        path = new String[L];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            arr[i] = st.nextToken();
        }
        Arrays.sort(arr);

        combination(0, 0);
        System.out.println(sb);
    }

    public static void combination(int depth, int start) {
        if (depth == L) {
            if (isValid(path)) {
                for (String p : path) {
                    sb.append(p);
                }
                sb.append("\n");
            }
            return;
        }
        for (int i = start; i < C; i++) {
            path[depth] = arr[i];
            combination(depth+1, i+1);
        }
    }
    
    // 자음 모음 갯수 검사
    public static boolean isValid(String[] path) {
        int vowels = 0;
        int consonants = 0;
        for (String s : path) {
            if ("aeiou".contains(s)) {
                vowels++;
            } else {
                consonants++;
            }
        }
        return vowels > 0 && consonants > 1;
    }
}
