using System;
using System.Timers;

namespace CLI_Clock
{
    class Program
    {
        static Timer timer;

        static void Main(string[] args)
        {   
            Console.Write(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

            timer = new Timer();
            timer.Interval = 1000;
            timer.Elapsed += new ElapsedEventHandler(timer_Elapsed);

            while (true)
            {
                timer.Start();
            }
        }

        private static void timer_Elapsed(Object sender, ElapsedEventArgs e)
        {
            Console.Write("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
            Console.Write(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
        }
    }
}
