using System;

namespace multiplication_table
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Multiplication Table (1-12)\n");
            for (int i = 1; i < 13; i++)
            {
                for (int j = 1; j < 13; j++)
                {
                    Console.WriteLine($"{i} * {j} = {i * j}");
                }
                Console.WriteLine("");
            }
        }
    }
}
