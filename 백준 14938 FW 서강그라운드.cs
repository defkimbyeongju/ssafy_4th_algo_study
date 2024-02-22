using System;
using System.Linq;

class Program
{
    const int INF = int.MaxValue;
    const int MAX = 101;

    static void FloydWarshall(int n, int[,] dist)
    {
        for (int k = 1; k <= n; ++k)
        {
            for (int i = 1; i <= n; ++i)
            {
                for (int j = 1; j <= n; ++j)
                {
                    if (dist[i, k] != INF && dist[k, j] != INF && dist[i, k] + dist[k, j] < dist[i, j])
                    {
                        dist[i, j] = dist[i, k] + dist[k, j];
                    }
                }
            }
        }
    }

    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int n = input[0], m = input[1], r = input[2];

        var items = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int[,] dist = new int[MAX, MAX];

        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
                if (i == j) dist[i, j] = 0;
                else dist[i, j] = INF;
            }
        }

        for (int i = 0; i < r; ++i)
        {
            input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int a = input[0], b = input[1], l = input[2];
            dist[a, b] = l;
            dist[b, a] = l;
        }

        FloydWarshall(n, dist);

        int maxItems = 0;
        for (int i = 1; i <= n; ++i)
        {
            int total = 0;
            for (int j = 1; j <= n; ++j)
            {
                if (dist[i, j] <= m)
                {
                    total += items[j-1];
                }
            }
            maxItems = Math.Max(maxItems, total);
        }

        Console.WriteLine(maxItems);
    }
}
