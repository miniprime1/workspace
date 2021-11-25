using System;
using static System.Console;

namespace Calculator
{
    class MainApp
    {
        static void Main(string[] args)
        {
            #region Declear
            double a;
            double b;
            double x;
            double temp1;
            double Result;
            string ConvertedResult;
            #endregion

            #region Logo
            WriteLine("Area Calculator v1.0\n");
            #endregion

            #region Options
            WriteLine("Options");
            WriteLine("1. Rectangle");
            WriteLine("2. Triangle");
            WriteLine("3. Trapezoid");
            WriteLine("4. Circle");
            WriteLine("5. Square");
            WriteLine("6. Sector");
            WriteLine("7. Parallelogram");
            WriteLine("8. Ellipse");
            WriteLine("9. Exit\n");
            Write("Your choice: ");
            string choose = ReadLine();
            #endregion

            #region Main
            switch (choose)
            {
                #region 1. Rectangle
                case "1":
                    {
                        WriteLine("\nRectangle (Weight * Height)\n");
                        Write("Enter Width: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Height: ");
                        b = double.Parse(ReadLine());
                        Result = a * b;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 2. Triangle
                case "2":
                    {
                        WriteLine("\nTriangle (Weight * Height * 0.5)\n");
                        Write("Enter Width: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Height: ");
                        b = double.Parse(ReadLine());
                        Result = a * b / 2;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{Result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 3. Trapezoid
                case "3":
                    {
                        WriteLine("\nTrapezoid ([Upper side + Lower side] * Height * 0.5)\n");
                        Write("Enter Upper side: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Lower side: ");
                        b = double.Parse(ReadLine());
                        Write("Enter Height: ");
                        x = double.Parse(ReadLine());
                        temp1 = a + b;
                        Result = temp1 * x * 0.5;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 4. Circle
                case "4":
                    {
                        WriteLine("\nCircle (Radius * Radius * 3.14)\n");
                        Write("Enter Radius: ");
                        a = double.Parse(ReadLine());
                        Result = a * 3.14;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 5. Square
                case "5":
                    {
                        WriteLine("\nSquare (Side ^ 2)\n");
                        Write("Enter length of Side: ");
                        a = double.Parse(ReadLine());
                        Result = Math.Pow(a, 2);
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 6. Sector
                case "6":
                    {
                        WriteLine("\nSector ([Radius ^ 2] * Angle * 0.5)\n");
                        Write("Enter Radius: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Angle: ");
                        b = double.Parse(ReadLine());
                        temp1 = Math.Pow(a, 2);
                        Result = temp1 * b * 0.5;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 7. Parallelogram
                case "7":
                    {
                        WriteLine("\nParallelogram (Base * Vertical Height)\n");
                        Write("Enter Base: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Height: ");
                        b = double.Parse(ReadLine());
                        Result = a * b;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 8. Eclipse
                case "8":
                    {
                        WriteLine("\nEclipse (Radius * Other Radius * 3.14)\n");
                        Write("Enter Radius: ");
                        a = double.Parse(ReadLine());
                        Write("Enter Other Radius: ");
                        b = double.Parse(ReadLine());
                        Result = a * b * 3.14;
                        ConvertedResult = Convert.ToString(Result);
                        WriteLine("\nResult");
                        WriteLine($"{ConvertedResult}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                #endregion

                #region 9. Exit
                case "9":
                    {
                        break;
                    }
                #endregion

                #region Invalid Choice
                default:
                    {
                        WriteLine("\nInvalid Choice\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                    #endregion
            }
            #endregion
        }
    }
}