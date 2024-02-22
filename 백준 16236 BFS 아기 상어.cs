using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program
{
    static int N;
    static int[,] board;
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static Shark shark = new Shark();

    class Position
    {
        public int X, Y, Dist;
        public Position(int x, int y, int dist)
        {
            X = x;
            Y = y;
            Dist = dist;
        }
    }

    class Shark
    {
        public int X, Y, Size = 2, Eaten = 0;
    }

    static void Main(string[] args)
    {
        N = int.Parse(Console.ReadLine());
        board = new int[N, N];

        for (int i = 0; i < N; i++)
        {
            var line = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            for (int j = 0; j < N; j++)
            {
                board[i, j] = line[j];
                if (board[i, j] == 9)
                {
                    shark.X = i;
                    shark.Y = j;
                    board[i, j] = 0;
                }
            }
        }

        int time = 0;
        while (true)
        {
            var fish = Bfs(shark);
            if (fish == null) break;

            board[fish.X, fish.Y] = 0;
            shark.X = fish.X;
            shark.Y = fish.Y;
            time += fish.Dist;
            shark.Eaten++;

            if (shark.Eaten == shark.Size)
            {
                shark.Size++;
                shark.Eaten = 0;
            }
        }

        Console.WriteLine(time);
    }

    static Position Bfs(Shark shark)
    {
        bool[,] visited = new bool[N, N];
        Queue<Position> queue = new Queue<Position>();
        List<Position> fishes = new List<Position>();

        queue.Enqueue(new Position(shark.X, shark.Y, 0));
        visited[shark.X, shark.Y] = true;

        while (queue.Count > 0)
        {
            var pos = queue.Dequeue();
            for (int i = 0; i < 4; i++)
            {
                int nx = pos.X + dx[i];
                int ny = pos.Y + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx, ny] && board[nx, ny] <= shark.Size)
                {
                    visited[nx, ny] = true;
                    queue.Enqueue(new Position(nx, ny, pos.Dist + 1));

                    if (board[nx, ny] > 0 && board[nx, ny] < shark.Size)
                    {
                        fishes.Add(new Position(nx, ny, pos.Dist + 1));
                    }
                }
            }
        }

        if (fishes.Count == 0) return null;

        fishes.Sort((a, b) => a.Dist != b.Dist ? a.Dist.CompareTo(b.Dist) : a.X != b.X ? a.X.CompareTo(b.X) : a.Y.CompareTo(b.Y));
        return fishes[0];
    }
}
