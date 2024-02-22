import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    static ArrayList<Integer> data = new ArrayList<>();

    public static void postOrder(int start, int end) {
        if (start > end) return;

        int div = end + 1;
        for (int i = start + 1; i <= end; i++) {
            if (data.get(start) < data.get(i)) {
                div = i;
                break;
            }
        }

        postOrder(start + 1, div - 1);
        postOrder(div, end);
        System.out.println(data.get(start));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            data.add(Integer.parseInt(line));
        }

        postOrder(0, data.size() - 1);
    }
}
