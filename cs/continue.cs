using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace playground
{
    class Program
    {
        static void Main(string[] args)
        {
            for (; ; )
            {
                Write("Continue? ([y]es, [n]o) : ");
                string answer = ReadLine();
                if (answer == "n")
                {
                    WriteLine("\nFailed");
                    ReadKey();
                    break;
                }
                else if (answer == "y")
                {
                    WriteLine("\nSucceed!");
                    ReadKey();
                    break;
                }
                else
                {
                    WriteLine("\nPlease answer only [y]es or [n]o\n");
                }
            }
        }
    }
}
