using System;
using System.Threading.Tasks;
using System.Linq;
using System.Collections.Generic;
using System.Timers;

namespace Maze
{
    class Program
    {
        static Timer timer;
        
        public static void Main(string[] args)
        {
            timer = new Timer();
            timer.Interval = 5;
            timer.Elapsed += new ElapsedEventHandler(timer_Elapsed);
            
            while (true)
            {
                timer.Start();
            }
        }

        private static void timer_Elapsed(Object sender, ElapsedEventArgs e)
        {
            Random rnd = new Random();
            
            int maze = rnd.Next(1, 3);
                
            if (maze == 1)
                Console.Write("⟋");
            if (maze == 2)
                Console.Write("⟍");
        }
    }
}