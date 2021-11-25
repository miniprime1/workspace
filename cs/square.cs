using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Media;
using System.IO;
using System.Collections;
using System.Windows;
using System.Threading.Tasks;
using static System.Console;

namespace playground
{
    class MainApp
    {
        public static double input1;
        public static double input2;
        public static double result;
        static void Main(string[] args)
        {
            //Main
            WriteLine("Square Engine v1.0\n");

            //Input
            Write("Enter X: ");
            input1 = double.Parse(ReadLine());
            Write("Enter Y: ");
            input2 = double.Parse(ReadLine());

            //Calculating
            result = Math.Pow(input1, input2);

            //Result
            WriteLine($"\nResult: {input1} ^ {input2} = {result}\n");

            //Continue
            WriteLine("Press any key to continue");
            ReadKey();
        }
    }
}