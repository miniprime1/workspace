using System;

namespace InputOutput
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This program will echo back the text you typed\n");

            while (true)
            {
                Console.Write("Input: ");
                var input = Console.ReadLine();
                Console.WriteLine($"Text typed: {input}\n");
            }
        }
    }
}