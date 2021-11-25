using System;
using System.Threading;

namespace PopCat
{
    class Program
    {
        static void Main(string[] args)
        {
            string popcat_openmouth_ascii = @"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,.@@@@@@@@@
@@//((///,,,@@@@@@@@@@@@@@@@@@@@@(**,,,,,,@@@@@@@@@
@@((((/(//(/,,@@@@@@@/,,,......,///*,,****@@@@@@@@@
@*(((((((//(((((((((/*,.         ..//(****,@@@@@@@@
@*/((((((((/((((((/,,/##*.   .,*////,....*,,@@@@@@@
@@***((((((((((((//(*.   .,*/(#%%%%%%#(*....,,@@@@@
@@@*,***/(((((((/,....,*(%&@@@@@@@@@@@@@&#(/***.@@2
@@@@,,*,*/((((%#/****/#@@@@@@@@@@@@@@@@@@@@%((/*@@@
@@@@@ *(#####%%(////(&@@@@@@@@@@@@@@@@@@@@@@%#(/*@@
@@@@@@@*#%&&&%((/((#&@@@@@@@@@@@@@@@@@@@@@@@%#(/*@@
@@@@@@@*/%&&&#((/((#@@@&&&&&@@@@@@@@@&&&&&&&%#(//@@
@@@@@@@@(*&&&%#(((((%&&&&&&&&&&&&&&&&&&&&&&%#((/(@@
@@@@@@@@@,*%&%((/(/(((#%%%&&&&&&&&&&&&&&%%##((/*@@@
@@@@@@@@@@*//((///////(((###%%%%%%%%%%%##((((/,@@@@
@@@@@@@@@.*//////////////(((((((#####(((((((*@@@@@@
@@@@@@@@@***///////////(/((((((((((((((((((*,@@@@@@
@@@@@@@@*****///////////((((((((((((((((((/*@@@@@@@
@@@@@@@,*****////////////////(((((((((((((/*(@@@@@@
@@@@@@,******///*///////////((((/(((((((////(@@@@@@
@@@@@@,**********////////////(((/(((((((////(@@@@@@
@@@@@.**************/////////////(((((((////@@@@@@@
@@@@@,***************////////////(((((((/(//@@@@@@@
@@@@@,**************//////////////((/(((////@@@@@@@
@@@@@,***////***//**/**/////////////(///(((/@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            ";

            string popcat_closemouth_ascii = @"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,@@@@@@@@
@@@@@*//((//*/@@@@@@@@@@@@@@@@@@@@@@**,,,,,%@@@@@@@
@@@@@*(((////(/*,@@@@@@@@@@@@@@@@@///*,,,**%@@@@@@@
@@@@@*((((((///((((///////**.     .*/******@@@@@@@@
@@@@@(/(((((((//(((((//*..          .,*//**@@@@@@@@
@@@@@@(**((((((///////*(####*       ,#%%#/*,@@@@@@@
@@@@@@@/****(((((((((/,,,((#/,        .....,//@@@@@
@@@@@@@@,,**/((((##%#(*,,,...  ..,////.....,*//*@@@
@@@@@@@@@,/#####%%%%#(///////((((/((((((((((((//(@@
@@@@@@@@@@,(%%%&&&%##///(((((((((((((((((((((((/,@@
@@@@@@@@@@@*#%&&&&###(///((((((((((((((((((((((*#@@
@@@@@@@@@@@@*#&&&&%%((////(((((((((((((((((((/*@@@@
@@@@@@@@@@@@@,(%%&#((////////(((((((((((((((/,@@@@@
@@@@@@@@@@@@@,////////////////(((((((((((((/*,@@@@@
@@@@@@@@@@@@***//////////////((((((((((((((/*,@@@@@
@@@@@@@@@@@***//////////////////(((((((((((/**@@@@@
@@@@@@@@@@(****///////////////////((((((((///*@@@@@
@@@@@@@@@@******////////////////////(((((((//**@@@@
@@@@@@@@@,******////////////////////((((((////(@@@@
@@@@@@@@@********////////////////////(((((////*@@@@
@@@@@@@@.************/////////////////(((((///*@@@@
@@@@@@@@,************////////////////((((/////*@@@@
@@@@@@@@,************////////////////((((/////,@@@@
@@@@@@@@***/*******///////////////////////////,%@@@
@@@@@@@@************//////////////////////////,,@@@
            ";

            for (; ; )
            {
                Console.Clear();
                Console.WriteLine(popcat_closemouth_ascii);
                Thread.Sleep(250);
                Console.Clear();
                Console.WriteLine(popcat_openmouth_ascii);
                Thread.Sleep(250);
            }
        }
    }
}