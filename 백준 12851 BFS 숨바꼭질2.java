import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static final int MAX = 100001;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] visited = new int[MAX];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(N);

        int cnt = 0;
        int result = 0;

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            if (curr == K) {
                if (result == 0) result = visited[curr];
                if (result == visited[curr]) cnt++;
                continue;
            }

            int[] nextNums = {curr - 1, curr + 1, curr * 2};
            for (int nextNum : nextNums) {
                if (0 <= nextNum && nextNum < MAX && (visited[nextNum] == 0 || visited[nextNum] == visited[curr] + 1)) {
                    visited[nextNum] = visited[curr] + 1;
                    queue.add(nextNum);
                }
            }
        }

        System.out.println(result);
        System.out.println(cnt);

        sc.close();
    }
}
