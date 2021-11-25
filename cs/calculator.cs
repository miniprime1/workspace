using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using static System.Console;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Declear
            double a;
            double b;
            double y;
            double x;
            double big;
            double small;
            double nmg;
            double angle;
            double GCD;
            double LCM;
            double temp1;
            double Result;
            string ConvertedResult;
            string choice;
            double result;
            bool resultboolean;
            int yint;
            #endregion

            #region Window
            SetWindowSize(120, 40);
            Title = "Calculator";
            #endregion

            #region Logo
            WriteLine("CLI Calculator, version 14.0");
            WriteLine("Copyright (C) 2020 miniprime1. All rights reserved.");
            WriteLine("Configured for .NET Framework 4.8\n");
            #endregion

            #region Options
            WriteLine("Options");
            WriteLine("1. Addition");
            WriteLine("2. Subtraction");
            WriteLine("3. Multiplication");
            WriteLine("4. Division");
            WriteLine("5. Remainder");
            WriteLine("6. Exponentiation");
            WriteLine("7. Square root");
            WriteLine("8. Cube root");
            WriteLine("9. Trigonometric Functions");
            WriteLine("10. Inverse Trigonometric Functions");
            WriteLine("11. Hyperbolic Functions");
            WriteLine("12. Constant");
            WriteLine("13. Absolute Value");
            WriteLine("14. Area Calculator");
            WriteLine("15. LCM/GCD");
            WriteLine("16. Logarithm");
            WriteLine("17. Equals");
            WriteLine("18. Round/RoundUp/RoundDown");
            WriteLine("19. Truncate");
            WriteLine("20. Radian/Degree");
            WriteLine("21. Min/Max");
            WriteLine("22. Celsius/Fahrenheit");
            WriteLine("23. Average");
            WriteLine("24. Exit\n");
            Write("Your choice: ");
            choice = ReadLine();
            #endregion

            #region Main
            switch (choice)
            {
                case "1":
                    {
                        WriteLine("\nAddition\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input: ");
                        b = double.Parse(ReadLine());
                        result = a + b;
                        WriteLine("\nResult");
                        WriteLine($"{a} + {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "2":
                    {
                        WriteLine("\nSubtraction\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input: ");
                        b = double.Parse(ReadLine());
                        result = a - b;
                        WriteLine("\nResult");
                        WriteLine($"{a} - {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "3":
                    {
                        WriteLine("\nMultiplication\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input: ");
                        b = double.Parse(ReadLine());
                        result = a * b;
                        WriteLine("\nResult");
                        WriteLine($"{a} * {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "4":
                    {
                        WriteLine("\nDivision\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input ");
                        b = double.Parse(ReadLine());
                        result = a / b;
                        WriteLine("\nResult");
                        WriteLine($"{a} / {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "5":
                    {
                        WriteLine("\nRemainder\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input ");
                        b = double.Parse(ReadLine());
                        result = a % b;
                        WriteLine("\nResult");
                        WriteLine($"{a} % {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        break;
                    }

                case "6":
                    {
                        WriteLine("\nExponentiation\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input: ");
                        b = double.Parse(ReadLine());
                        result = Math.Pow(a, b);
                        WriteLine("\nResult");
                        WriteLine($"{a} ^ {b} = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "7":
                    {
                        WriteLine("Square root");
                        Write("Enter input: ");
                        a = double.Parse(ReadLine());
                        result = Math.Sqrt(a);
                        WriteLine("\nResult");
                        WriteLine($"{a} ^ 0.5 = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "8":
                    {
                        WriteLine("Cube root (Beta)");
                        Write("Enter input: ");
                        a = double.Parse(ReadLine());
                        result = Math.Ceiling(Math.Pow(a, (double) 1 / 3));
                        WriteLine("\nResult");
                        WriteLine($"{a} ^ 1/3 = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "9":
                    {
                        WriteLine("\nTrigonometric Functions (Radian)\n");
                        WriteLine("Options");
                        WriteLine("1. Sine");
                        WriteLine("2. Cosine)");
                        WriteLine("3. Tangent");
                        Write("Your choice: ");
                        string choosefunc = ReadLine();

                        switch (choosefunc)
                        {
                            case "1":
                                {
                                    WriteLine("\nSine - Returns the sin value of an angle x radians.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Sin(x);
                                    WriteLine("\nResult");
                                    WriteLine($"sin({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nCosine - Returns the cos of an angle x radians.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Cos(x);
                                    WriteLine("\nResult");
                                    WriteLine($"cos({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "3":
                                {
                                    WriteLine("\nTangent - Returns the tan value of an angle x radians.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Tan(x);
                                    WriteLine("\nResult");
                                    WriteLine($"tan({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "10":
                    {
                        WriteLine("\nInverse Trigonometric Functions (Radian)\n");
                        WriteLine("Options");
                        WriteLine("1. arcsine");
                        WriteLine("2. arccosine");
                        WriteLine("3. arctangent");
                        WriteLine("4. arctangent2");
                        Write("Your choice: ");
                        string choosefunc = ReadLine();

                        switch (choosefunc)
                        {
                            case "1":
                                {
                                    WriteLine("\narcsine - Returns the angle in radians at which x appears when sin is applied.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Asin(x);
                                    WriteLine("\nResult");
                                    WriteLine($"srcsin({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\narccosine - Returns the angle in radians at which x occurs when cos is applied.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Acos(x);
                                    WriteLine("\nResult");
                                    WriteLine($"arccos({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "3":
                                {
                                    WriteLine("\narctangent - Returns the angle in radians at which x occurs when tan is applied.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Atan(x);
                                    WriteLine("\nResult");
                                    WriteLine($"tan({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "4":
                                {
                                    WriteLine("\narctangent2 - Returns the angle in radians from (x, y) when tan is applied.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Write("Enter Y: ");
                                    y = double.Parse(ReadLine());
                                    result = Math.Atan2(x, y);
                                    WriteLine("\nResult");
                                    WriteLine($"arctan2({x}, {y}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "11":
                    {
                        WriteLine("\nHyperbolic Functions (Radian)\n");
                        WriteLine("Options");
                        WriteLine("1. Hyperbolic Sine");
                        WriteLine("2. Hyperbolic Cosine");
                        WriteLine("3. Hyperbolic Tangent");
                        Write("Your choice: ");
                        string choosefunc = ReadLine();

                        switch (choosefunc)
                        {
                            case "1":
                                {
                                    WriteLine("\nSine (Radian)\n");
                                    Write("Enter input: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Sinh(x);
                                    WriteLine("\nResult");
                                    WriteLine($"sinh({x}){result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nCosine (Radian)\n");
                                    Write("Enter input: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Cosh(x);
                                    WriteLine("\nResult");
                                    WriteLine($"cosh({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "3":
                                {
                                    WriteLine("\nTangent (Radian)\n");
                                    Write("Enter input: ");
                                    x = double.Parse(ReadLine());
                                    result = Math.Tanh(x);
                                    WriteLine("\nResult");
                                    WriteLine($"tanh({x}) = {result}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "12":
                    {
                        WriteLine("\nConstant\n");
                        WriteLine("Options");
                        WriteLine("1. e (2.718281)");
                        WriteLine("2. pi (3.141592)");
                        Write("Your choice: ");
                        string choosecons = ReadLine();

                        switch (choosecons)
                        {
                            case "1":
                                {
                                    WriteLine("");
                                    WriteLine("Result");
                                    WriteLine("2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("");
                                    WriteLine("Result");
                                    WriteLine("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "13":
                    {
                        WriteLine("\nAbsolute Value\n");
                        Write("Enter input: ");
                        x = double.Parse(ReadLine());
                        result = Math.Abs(x);
                        WriteLine("\nResult");
                        WriteLine($"|{x}| = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "14":
                    {
                        WriteLine("\nArea Calculator\n");

                        WriteLine("Options");
                        WriteLine("1. Rectangle");
                        WriteLine("2. Triangle");
                        WriteLine("3. Trapezoid");
                        WriteLine("4. Circle");
                        WriteLine("5. Square");
                        WriteLine("6. Sector");
                        WriteLine("7. Parallelogram");
                        WriteLine("8. Ellipse");
                        Write("Your choice: ");
                        string choicearea = ReadLine();

                        switch (choicearea)
                        {
                            case "1":
                                {
                                    WriteLine("\nRectangle [Width * Height]\n");
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

                            case "2":
                                {
                                    WriteLine("\nTriangle [Width * Height * 0.5]\n");
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

                            case "3":
                                {
                                    WriteLine("\nTrapezoid [(Upper side + Lower side) * Height * 0.5]\n");
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

                            case "4":
                                {
                                    WriteLine("\nCircle [Radius * Radius * Pi]\n");
                                    Write("Enter Radius: ");
                                    a = double.Parse(ReadLine());
                                    Result = a * a * Math.PI;
                                    ConvertedResult = Convert.ToString(Result);
                                    WriteLine("\nResult");
                                    WriteLine($"{ConvertedResult}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "5":
                                {
                                    WriteLine("\nSquare [Side ^ 2]\n");
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

                            case "6":
                                {
                                    WriteLine("\nSector [(Radius ^ 2) * Angle * 0.5]\n");
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

                            case "7":
                                {
                                    WriteLine("\nParallelogram [Base * Vertical Height]\n");
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

                            case "8":
                                {
                                    WriteLine("\nEclipse [Radius * Other Radius * Pi]\n");
                                    Write("Enter Radius: ");
                                    a = double.Parse(ReadLine());
                                    Write("Enter Other Radius: ");
                                    b = double.Parse(ReadLine());
                                    Result = a * b * Math.PI;
                                    ConvertedResult = Convert.ToString(Result);
                                    WriteLine("\nResult");
                                    WriteLine($"{ConvertedResult}\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "15":
                    {
                        WriteLine("\nLCM/GCD");
                        WriteLine("Options");
                        WriteLine("1. Least Common Multiple");
                        WriteLine("2. Greatest Common Divisor\n");
                        Write("Your choice: ");
                        string choicelcmgdc = Convert.ToString(ReadLine());
                        switch (choicelcmgdc)
                        {
                            case "1":
                                WriteLine("\nLeast Common Multiple [lcm(a, b)]\n");
                                Write("Enter A: ");
                                a = double.Parse(ReadLine());
                                Write("Enter B: ");
                                b = double.Parse(ReadLine());
                                if (a >= b)
                                {
                                    big = a;
                                    small = b;
                                }
                                else
                                {
                                    big = b;
                                    small = a;
                                }

                                nmg = big % small;

                                while (nmg != 0)
                                {
                                    big = small;
                                    small = nmg;

                                    nmg = big % small;
                                }
                                GCD = small;
                                LCM = a * b / GCD;
                                WriteLine("\nResult");
                                WriteLine($"lcm({a}, {b}) = {LCM}\n");
                                WriteLine("Press any key to continue");
                                ReadKey();
                                Write("\b");
                                break;

                            case "2":
                                WriteLine("\nGreatest Common Divisor [gcd(a, b)]\n");
                                Write("Enter A: ");
                                a = double.Parse(ReadLine());
                                Write("Enter B: ");
                                b = double.Parse(ReadLine());
                                if (a >= b)
                                {
                                    big = a;
                                    small = b;
                                }
                                else
                                {
                                    big = b;
                                    small = a;
                                }

                                nmg = big % small;

                                while (nmg != 0)
                                {
                                    big = small;
                                    small = nmg;

                                    nmg = big % small;
                                }
                                GCD = small;
                                LCM = a * b / GCD;
                                WriteLine("\nResult");
                                WriteLine($"gcd({a}, {b}) = {GCD}\n");
                                WriteLine("Press any key to continue");
                                ReadKey();
                                Write("\b");
                                break;

                            default:
                                WriteLine("\nInvalid Choice\n");
                                WriteLine("Press any key to continue");
                                ReadKey();
                                Write("\b");
                                break;

                        }
                        break;
                    }

                case "16":
                    {
                        WriteLine("\nLogarithm\n");
                        WriteLine("Options");
                        WriteLine("1. LogE(X) - Logarithm of x to the base e");
                        WriteLine("2. Log10(X) - Logarithm of x to the base 10");
                        WriteLine("3. LogY(X) - Logarithm of x to the base y");
                        Write("Your choice: ");
                        string chooselog = Convert.ToString(ReadLine());

                        switch (chooselog)
                        {
                            case "1":
                                {
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Result = Math.Log(x);
                                    WriteLine("\nResult");
                                    WriteLine($"LogE({x}) = {Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                            case "2":
                                {
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Result = Math.Log10(x);
                                    WriteLine("\nResult");
                                    WriteLine($"Log10({x}) = {Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                            case "3":
                                {
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Write("Enter Y: ");
                                    y = double.Parse(ReadLine());
                                    Result = Math.Log(x, y);
                                    WriteLine("\nResult");
                                    WriteLine($"Log{y}({x}) = {Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "17":
                    {
                        WriteLine("\nEquals - Determine if x and y are equal\n");
                        Write("Enter X: ");
                        x = double.Parse(ReadLine());
                        Write("Enter Y: ");
                        y = double.Parse(ReadLine());
                        resultboolean = Math.Equals(x, y);
                        WriteLine("\nResult");
                        WriteLine($"Equals = {resultboolean}");
                        WriteLine("\nPress any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "18":
                    {
                        WriteLine("\nRound / Round Up / Round Down\n");
                        WriteLine("Options");
                        WriteLine("1. Rounds");
                        WriteLine("2. Round Up");
                        WriteLine("3. Round Down\n");
                        Write("Your choice: ");
                        string choosercf = ReadLine();

                        switch (choosercf)
                        {
                            case "1":
                                {
                                    WriteLine("\nRound - Rounds to y digits for x\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Write("Enter Y: ");
                                    yint = int.Parse(ReadLine());
                                    Result = Math.Round(x, yint);
                                    WriteLine("Result");
                                    WriteLine($"{Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nRounds up for x\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Result = Math.Ceiling(x);
                                    WriteLine("Result");
                                    WriteLine($"{Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "3":
                                {
                                    WriteLine("\nRounds down for x.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Result = Math.Floor(x);
                                    WriteLine("Result");
                                    WriteLine($"{Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "19":
                    {
                        WriteLine("\nTruncate - Remove the decimal point for x\n");
                        Write("Enter X: ");
                        x = double.Parse(ReadLine());
                        Result = Math.Truncate(x);
                        WriteLine("\nResult");
                        WriteLine($"trunc({x}) = {Result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }

                case "20":
                    {
                        WriteLine("\nRadian/Degree\n");
                        WriteLine("Options");
                        WriteLine("1. Radian to Degree");
                        WriteLine("2. Degree to Radian");
                        Write("Your choice: ");
                        string choosecons = ReadLine();

                        switch (choosecons)
                        {
                            case "1":
                                {
                                    WriteLine("\nRadian to Degree [angle * (Pi / 180)]\n");
                                    Write("Enter angle: ");
                                    angle = double.Parse(ReadLine());
                                    Result = angle * (Math.PI / 180);
                                    WriteLine("\nResult");
                                    WriteLine($"{angle} * ({Math.PI} / 180) = {Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nDegree to Radian [Pi * angle / 180]\n");
                                    Write("Enter angle: ");
                                    angle = double.Parse(ReadLine());
                                    Result = Math.PI * angle / 180;
                                    WriteLine("\nResult");
                                    WriteLine($"{Math.PI} * {angle} / 180 = {Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "21":
                    {
                        WriteLine("\nMin/Max\n");
                        WriteLine("Options");
                        WriteLine("1. Min");
                        WriteLine("2. Max");
                        Write("Your choice: ");
                        string choosecons = ReadLine();

                        switch (choosecons)
                        {
                            case "1":
                                {
                                    WriteLine("\nMin - Returns the smaller of x and y.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Write("Enter Y: ");
                                    y = double.Parse(ReadLine());
                                    Result = Math.Min(x, y);
                                    WriteLine("\nResult");
                                    WriteLine($"{Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nMax - Returns the greater of x and y.\n");
                                    Write("Enter X: ");
                                    x = double.Parse(ReadLine());
                                    Write("Enter Y: ");
                                    y = double.Parse(ReadLine());
                                    Result = Math.Max(x, y);
                                    WriteLine("\nResult");
                                    WriteLine($"{Result}");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "22":
                    {
                        WriteLine("\nCelsius/Fahrenheit\n");
                        WriteLine("Options");
                        WriteLine("1. Celsius to Fahrenheit");
                        WriteLine("2. Fahrenheit to Celsius");
                        Write("Your choice: ");
                        string choosecons = ReadLine();

                        switch (choosecons)
                        {
                            case "1":
                                {
                                    WriteLine("\nCelsius to Fahrenheit [Celsius * 9/5 + 32]\n");
                                    Write("Enter input: ");
                                    x = double.Parse(ReadLine());
                                    Result = x * (5 / 9) + 32;
                                    WriteLine("\nResult");
                                    WriteLine($"{x}C = {Result}F");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            case "2":
                                {
                                    WriteLine("\nFahrenheit to Celsius [(Fahrenheit - 32) / 9/5]\n");
                                    Write("Enter input: ");
                                    x = double.Parse(ReadLine());
                                    Result = x * (5 / 9) + 32;
                                    WriteLine("\nResult");
                                    WriteLine($"{x}F = {Result}C");
                                    WriteLine("\nPress any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }

                            default:
                                {
                                    WriteLine("\nInvalid Choice\n");
                                    WriteLine("Press any key to continue");
                                    ReadKey();
                                    Write("\b");
                                    break;
                                }
                        }
                        break;
                    }

                case "23":
                    {
                        WriteLine("\nAverage [(x + y) / 2]\n");
                        Write("Enter 1st input: ");
                        a = double.Parse(ReadLine());
                        Write("Enter 2nd input: ");
                        b = double.Parse(ReadLine());
                        result = (a + b) / 2;
                        WriteLine("\nResult");
                        WriteLine($"({a} + {b}) / 2 = {result}\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
                case "24":
                    {
                        break;
                    }

                default:
                    {
                        WriteLine("\nInvalid Choice\n");
                        WriteLine("Press any key to continue");
                        ReadKey();
                        Write("\b");
                        break;
                    }
            }
            #endregion
        }
    }
}
