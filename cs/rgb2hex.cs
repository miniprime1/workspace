using System;
using System.Collections.Generic;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace playground
{
    class Program
    {
        static void Main(string[] args)
        {
            //Memory
            byte r;
            byte g;
            byte b;
            string hexr;
            string hexg;
            string hexb;
            string upr;
            string upg;
            string upb;
            string result;
            
            //Main
            WriteLine("RGB2HEX v1.0\n");
            
            //Input
            WriteLine("RGB");
            A:
            try
            {
                Write("R: ");
                r = byte.Parse(ReadLine());
                Write("G: ");
                g = byte.Parse(ReadLine());
                Write("B: ");
                b = byte.Parse(ReadLine());
                
            }
            catch (System.Exception)
            {
                WriteLine("\nError: Please enter valid input: Values for R, G and B should be from 0 to 255 only\n");
                goto A;
            }

            //Convert RGB to HEX
            hexr = Convert.ToString(r, 16);
            hexg = Convert.ToString(g, 16);
            hexb = Convert.ToString(b, 16);
            
            //Convert lower-case to upper-case
            upr = hexr.ToUpper();
            upg = hexg.ToUpper();
            upb = hexb.ToUpper();

            //Result
            result = '#' + upr + upg + upb;

            //Print Result
            WriteLine("\nHEX");
            WriteLine(result);

            //Exit
            WriteLine("\nPress any key to continue");
            ReadKey();
            Write("\b");
        }
    }
}
