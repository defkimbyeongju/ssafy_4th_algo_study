import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static boolean bfs(ArrayList<ArrayList<Integer>> graph, int start, int[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = 1;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int adjNode : graph.get(node)) {
                if (visited[adjNode] == 0) {
                    visited[adjNode] = -visited[node];
                    queue.add(adjNode);
                } else if (visited[adjNode] == visited[node]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int K = scanner.nextInt();

        for (int k = 0; k < K; k++) {
            int V = scanner.nextInt();
            int E = scanner.nextInt();

            ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
            for (int i = 0; i <= V; i++) {
                graph.add(new ArrayList<>());
            }

            int[] visited = new int[V + 1];
            for (int i = 0; i < E; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                graph.get(u).add(v);
                graph.get(v).add(u);
            }

            boolean isBipartite = true;
            for (int i = 1; i <= V; i++) {
                if (visited[i] == 0 && !bfs(graph, i, visited)) {
                    isBipartite = false;
                    break;
                }
            }
            System.out.println(isBipartite ? "YES" : "NO");
        }
        scanner.close();
    }
}