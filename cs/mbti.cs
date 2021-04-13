using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace MBTI
{
    class mbti
    {
        public static void Print(string result)
        {
            /*            
            else if (result == "")
            {
                WriteLine("<>");
                WriteLine("");
            }
            */

            if (result == "ISTJ")
            {
                WriteLine("\n<ISTJ>");
                WriteLine("Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized - their work, their home, their life. Value traditions and loyalty.");
            }
            else if (result == "ISFJ")
            {
                WriteLine("<ISFJ>");
                WriteLine("Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home.");
            }
            else if (result == "INFJ")
            {
                WriteLine("<INFJ>");
                WriteLine("Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision.");
            }
            else if (result == "INTJ")
            {
                WriteLine("<INTJ>");
                WriteLine("Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance - for themselves and others.");
            }
            else if (result == "ISTP")
            {
                WriteLine("<ISTP>");
                WriteLine("Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency.");
            }
            else if (result == "ISFP")
            {
                WriteLine("<ISFP>");
                WriteLine("Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others.");
            }
            else if (result == "INFP")
            {
                WriteLine("<INFP>");
                WriteLine("Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened.");
            }
            else if (result == "INTP")
            {
                WriteLine("<INTP>");
                WriteLine("Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical.");
            }
            else if (result == "ESTP")
            {
                WriteLine("<ESTP>");
                WriteLine("Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them - they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing.");
            }
            else if (result == "ESFP")
            {
                WriteLine("<ESFP>");
                WriteLine("Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people.");
            }
            else if (result == "ENFP")
            {
                WriteLine("<ENFP>");
                WriteLine("Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency.");
            }
            else if (result == "ENTP")
            {
                WriteLine("<ENTP>");
                WriteLine("Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another.");
            }
            else if (result == "ESTJ")
            {
                WriteLine("<ESTJ>");
                WriteLine("Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans.");
            }
            else if (result == "ESFJ")
            {
                WriteLine("<ESFJ>");
                WriteLine("Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute.");
            }
            else if (result == "ENFJ")
            {
                WriteLine("<ENFJ>");
                WriteLine("Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership.");
            }
            else if (result == "ENTJ")
            {
                WriteLine("<ENTJ>");
                WriteLine("Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas.");
            }
            else
            {
                WriteLine("Error!");
            }
        }
    }

    class cli
    {
        public static void Pause()
        {
            WriteLine("\nPress any key to continue");
            ReadKey();
            Write("\b");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string q1;
            string q2;
            string q3;
            string q4;
            string result;

            WriteLine("MBTI Test, version 1.0");
            WriteLine("Simple MBTI test in only 4 questions");
            WriteLine("Copyright (c) 2020 miniprime1\n");

            q1:
            WriteLine("<Category I: Favorite World>");
            WriteLine("(E) Extraversion: You focus on the outer world. \nYou enjoy socializing and are comfortable in large groups.");
            WriteLine("(I) Introversion: You focus on your inner wold. \nYou are comfortable when you are alone and prefer to socialize with others one-on-one");
            Write("What about you?: ");
            q1 = Convert.ToString(ReadLine());

            if ((q1 == "E") || (q1 == "I"))
            {
                q2:
                WriteLine("\n<Category II: Information>");
                WriteLine("(S) Sensing: You take in information using your five senses. \nYou focus on the present, and you have to see things to believe them.");
                WriteLine("(N) Intuition: You analyze and interpret information. \nYou like to consider new possibilities, so you spend more time thinking about the future.");
                Write("What about you?: ");
                q2 = Convert.ToString(ReadLine());

                if ((q2 == "S") || (q2 == "N"))
                {
                    q3:
                    WriteLine("\n<Category III: Decisions>");
                    WriteLine("(T) Thinking: You identify facts and use them to make decisions. \nYou do not avoid arguments, and you consider them natural and necessary.");
                    WriteLine("(F) Feeling: You make decisions based on feelings and emotions. \nArguments make you feel upset, and you avoid them.");
                    Write("What about you?: ");
                    q3 = Convert.ToString(ReadLine());

                    if ((q3 == "T") || (q3 == "F"))
                    {
                        q4:
                        WriteLine("\n<Category IV: Structure>");
                        WriteLine("(J) Judging: You plan and organize everything meticulously. \nYou are punctual, and you are good at getting things done on time.");
                        WriteLine("(P) Perceiving: You prefer to plan things as you go, \nand you are willing to change plans according to how you feel. \nIt is sometimes difficult for you to meet deadlines.");
                        Write("What about you?: ");
                        q4 = Convert.ToString(ReadLine());

                        if ((q4 == "J") || (q4 == "P"))
                        {
                            result = q1 + q2 + q3 + q4;
                            WriteLine("\nResult\n");
                            mbti.Print(result);
                            cli.Pause();
                        }
                        else
                        {
                            WriteLine("\nError: invalid choice\n");
                            goto q4;
                        }
                    }
                    else
                    {
                        WriteLine("\nError: invalid choice\n");
                        goto q3;
                    }
                }
                else
                {
                    WriteLine("\nError: invalid choice\n");
                    goto q2;
                }
            }
            else
            {
                WriteLine("\nError: invalid choice\n");
                goto q1;
            }
        }
    }
}
