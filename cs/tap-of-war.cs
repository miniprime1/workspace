using System;
using static System.Console;

namespace Tap_Of_War
{
    class Program
    {
        static void update(int o, int x)
        {
            Clear();
            Write("[ ");
            for (int i = 0; i < o; i++)
            {
                Write("O ");
            }
            for (int j = 0; j < x; j++)
            {
                Write("X ");
            }
            Write("]");
        }

        static char check(int o, int x)
        {
            if (o == 0)
            {
                return 'x';
            }
            else if (x == 0)
            {
                return 'o';
            }
            else
            {
                return 'n';
            }
        }

        static void Main(string[] args)
        {
            int difficult = 30;
            int index_o = difficult / 2;
            int index_x = difficult / 2;
            char tmp;

            WriteLine("Tap of War v1.0");
            WriteLine("Copyright (c) 2020 miniprime1\n");
            // WriteLine("[Recommended OS: Windows]");

            WriteLine("Game Rule");
            WriteLine("1. Choose a team with your friend (X or O)");
            WriteLine("2. Press enter key to start the game (enter)");
            WriteLine("2. Type your team's markers as fast as you can ('o' or 'x')");
            WriteLine("3. If all the spaces are your team's markers, you win\n");

            WriteLine("Press enter key to start"); ReadLine();
            update(index_o, index_x);

            while (true)
            {
                tmp = ReadKey().KeyChar;

                if (tmp == 'o')
                {
                    index_o++; index_x--;
                }
                else if (tmp == 'x')
                {
                    index_o--; index_x++;
                }
                else
                {
                    // pass
                }

                update(index_o, index_x);

                if (check(index_o, index_x) == 'o')
                {
                    WriteLine("\n\nO is winner!");
                    break;
                }
                else if (check(index_o, index_x) == 'x')
                {
                    WriteLine("\n\nX is winner!");
                    break;
                }
                else
                {
                    // pass
                }
            }
        }
    }
}
