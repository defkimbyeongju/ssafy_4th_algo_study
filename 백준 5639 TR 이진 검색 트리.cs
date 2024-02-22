using System;
using System.Collections.Generic;

class Program {
    static List<int> data = new List<int>();

    static void PostOrder(int start, int end) {
        if (start > end) return;

        int div = end + 1;
        for (int i = start + 1; i <= end; i++) {
            if (data[start] < data[i]) {
                div = i;
                break;
            }
        }

        PostOrder(start + 1, div - 1);
        PostOrder(div, end);
        Console.WriteLine(data[start]);
    }

    static void Main() {
        string line;
        while ((line = Console.ReadLine()) != null && line != "") {
            data.Add(int.Parse(line));
        }

        PostOrder(0, data.Count - 1);
    }
}
