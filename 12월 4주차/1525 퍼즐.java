import java.util.*;

public class Main {
    static int bfs(String start) {
        String target = "123456789";
        Queue<Pair> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new Pair(start, 0));
        visited.add(start);

        while (!queue.isEmpty()) {
            Pair currentPair = queue.poll();
            String current = currentPair.state;
            int count = currentPair.count;

            if (current.equals(target)) {
                return count;
            }

            int zeroPos = current.indexOf('9');
            int x = zeroPos / 3, y = zeroPos % 3;

            int[] dx = {1, -1, 0, 0};
            int[] dy = {0, 0, 1, -1};

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                    char[] swapped = current.toCharArray();
                    char temp = swapped[zeroPos];
                    swapped[zeroPos] = swapped[nx * 3 + ny];
                    swapped[nx * 3 + ny] = temp;

                    String swappedStr = new String(swapped);
                    if (!visited.contains(swappedStr)) {
                        visited.add(swappedStr);
                        queue.add(new Pair(swappedStr, count + 1));
                    }
                }
            }
        }
        return -1;
    }

    static class Pair {
        String state;
        int count;

        Pair(String s, int c) {
            state = s;
            count = c;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder board = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            char num = sc.next().charAt(0);
            board.append((num == '0') ? '9' : num);
        }

        int result = bfs(board.toString());
        System.out.println(result);
    }
}
