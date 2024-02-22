import java.util.*;

public class Main {
    static final int MAX_N = 20;
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static int[][] board = new int[MAX_N][MAX_N];
    static boolean[][] visited = new boolean[MAX_N][MAX_N];
    static int N;

    static class Position implements Comparable<Position> {
        int x, y, dist;

        Position(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public int compareTo(Position o) {
            if (this.dist != o.dist) return this.dist - o.dist;
            if (this.x != o.x) return this.x - o.x;
            return this.y - o.y;
        }
    }

    static class Shark {
        int x, y, size, eaten;

        Shark(int x, int y, int size, int eaten) {
            this.x = x;
            this.y = y;
            this.size = size;
            this.eaten = eaten;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        Shark shark = new Shark(0, 0, 2, 0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] = sc.nextInt();
                if (board[i][j] == 9) {
                    shark.x = i;
                    shark.y = j;
                    board[i][j] = 0;
                }
            }
        }

        int time = 0;
        while (true) {
            Position fish = findFish(shark);
            if (fish == null) break;

            board[fish.x][fish.y] = 0;
            shark.x = fish.x;
            shark.y = fish.y;
            time += fish.dist;
            shark.eaten++;

            if (shark.eaten == shark.size) {
                shark.size++;
                shark.eaten = 0;
            }
        }

        System.out.println(time);
        sc.close();
    }

    static Position findFish(Shark shark) {
        Queue<Position> q = new LinkedList<>();
        List<Position> fishes = new ArrayList<>();
        for (boolean[] row : visited) Arrays.fill(row, false);

        q.add(new Position(shark.x, shark.y, 0));
        visited[shark.x][shark.y] = true;

        while (!q.isEmpty()) {
            Position pos = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = pos.x + dx[i], ny = pos.y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && board[nx][ny] <= shark.size) {
                    visited[nx][ny] = true;
                    q.add(new Position(nx, ny, pos.dist + 1));

                    if (board[nx][ny] > 0 && board[nx][ny] < shark.size) {
                        fishes.add(new Position(nx, ny, pos.dist + 1));
                    }
                }
            }
        }

        if (fishes.isEmpty()) return null;
        Collections.sort(fishes);
        return fishes.get(0);
    }
}
