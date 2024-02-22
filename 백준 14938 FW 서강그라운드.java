import java.io.*;
import java.util.*;

public class Main {
    static final int INF = (int) 1e9;
    static final int MAX = 101;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int[] items = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dist = new int[MAX][MAX];
        for (int[] row : dist) Arrays.fill(row, INF);
        for (int i = 1; i <= n; i++) dist[i][i] = 0;

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            dist[a][b] = dist[b][a] = l;
        }

        floydWarshall(n, dist);

        int maxItems = 0;
        for (int i = 1; i <= n; i++) {
            int total = 0;
            for (int j = 1; j <= n; j++) {
                if (dist[i][j] <= m) {
                    total += items[j];
                }
            }
            maxItems = Math.max(maxItems, total);
        }

        bw.write(maxItems + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    static void floydWarshall(int n, int[][] dist) {
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }
}
