using System;
using System.Collections.Generic;

class Program
{
    const int MAX = 100001;

    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int N = int.Parse(inputs[0]);
        int K = int.Parse(inputs[1]);

        int[] visited = new int[MAX];
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(N);

        int cnt = 0;
        int result = 0;

        while (queue.Count > 0)
        {
            int curr = queue.Dequeue();

            if (curr == K)
            {
                if (result == 0) result = visited[curr];
                if (result == visited[curr]) cnt++;
                continue;
            }

            int[] nextNums = { curr - 1, curr + 1, curr * 2 };
            foreach (int nextNum in nextNums)
            {
                if (0 <= nextNum && nextNum < MAX && (visited[nextNum] == 0 || visited[nextNum] == visited[curr] + 1))
                {
                    visited[nextNum] = visited[curr] + 1;
                    queue.Enqueue(nextNum);
                }
            }
        }

        Console.WriteLine(result);
        Console.WriteLine(cnt);
    }
}
