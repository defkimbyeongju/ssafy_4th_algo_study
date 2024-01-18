import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static int binarySearch(List<Integer> sub, int val) {
        int left = 0, right = sub.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (sub.get(mid) < val) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    public static int minCut(int[] connections) {
        List<Integer> sub = new ArrayList<>();
        for (int val : connections) {
            int pos = binarySearch(sub, val);
            if (pos == sub.size()) {
                sub.add(val);
            } else {
                sub.set(pos, val);
            }
        }
        return connections.length - sub.size();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] connections = new int[N];
        for (int i = 0; i < N; i++) {
            connections[i] = scanner.nextInt();
        }
        System.out.println(minCut(connections));
    }
}