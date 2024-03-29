#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32

#include <Windows.h>
#define ClearConsole() system("cls");
#define TimeSleep() Sleep(250);

#else

#include <unistd.h>
#define ClearConsole() system("clear");
#define TimeSleep() usleep(500000);

#endif

const char* popcat_openmouth_ascii =
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
	"@@@,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,.@@@@@@@@\n"
	"@@//((///,,,@@@@@@@@@@@@@@@@@@@@@(**,,,,,,@@@@@@@@\n"
	"@@((((/(//(/,,@@@@@@@/,,,......,///*,,****@@@@@@@@\n"
	"@*(((((((//(((((((((/*,.         ..//(****,@@@@@@@\n"
	"@*/((((((((/((((((/,,/##*.   .,*////,....*,,@@@@@@\n"
	"@@***((((((((((((//(*.   .,*/(#%%%%%%#(*....,,@@@@\n"
	"@@@*,***/(((((((/,....,*(%&@@@@@@@@@@@@@&#(/***.@@\n"
	"@@@@,,*,*/((((%#/****/#@@@@@@@@@@@@@@@@@@@@%((/*@@\n"
	"@@@@@ *(#####%%(////(&@@@@@@@@@@@@@@@@@@@@@@%#(/*@\n"
	"@@@@@@@*#%&&&%((/((#&@@@@@@@@@@@@@@@@@@@@@@@%#(/*@\n"
	"@@@@@@@*/%&&&#((/((#@@@&&&&&@@@@@@@@@&&&&&&&%#(//@\n"
	"@@@@@@@@(*&&&%#(((((%&&&&&&&&&&&&&&&&&&&&&&%#((/(@\n"
	"@@@@@@@@@,*%&%((/(/(((#%%%&&&&&&&&&&&&&&%%##((/*@@\n"
	"@@@@@@@@@@*//((///////(((###%%%%%%%%%%%##((((/,@@@\n"
	"@@@@@@@@@.*//////////////(((((((#####(((((((*@@@@@\n"
	"@@@@@@@@@***///////////(/((((((((((((((((((*,@@@@@\n"
	"@@@@@@@@*****///////////((((((((((((((((((/*@@@@@@\n"
	"@@@@@@@,*****////////////////(((((((((((((/*(@@@@@\n"
	"@@@@@@,******///*///////////((((/(((((((////(@@@@@\n"
	"@@@@@@,**********////////////(((/(((((((////(@@@@@\n"
	"@@@@@.**************/////////////(((((((////@@@@@@\n"
	"@@@@@,***************////////////(((((((/(//@@@@@@\n"
	"@@@@@,**************//////////////((/(((////@@@@@@\n"
	"@@@@@,***////***//**/**/////////////(///(((/@@@@@@\n"
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n";

const char* popcat_closemouth_ascii =
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
	"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,@@@@@@@\n"
	"@@@@@*//((//*/@@@@@@@@@@@@@@@@@@@@@@**,,,,,%@@@@@@\n"
	"@@@@@*(((////(/*,@@@@@@@@@@@@@@@@@///*,,,**%@@@@@@\n"
	"@@@@@*((((((///((((///////**.     .*/******@@@@@@@\n"
	"@@@@@(/(((((((//(((((//*..          .,*//**@@@@@@@\n"
	"@@@@@@(**((((((///////*(####*       ,#%%#/*,@@@@@@\n"
	"@@@@@@@/****(((((((((/,,,((#/,        .....,//@@@@\n"
	"@@@@@@@@,,**/((((##%#(*,,,...  ..,////.....,*//*@@\n"
	"@@@@@@@@@,/#####%%%%#(///////((((/((((((((((((//(@\n"
	"@@@@@@@@@@,(%%%&&&%##///(((((((((((((((((((((((/,@\n"
	"@@@@@@@@@@@*#%&&&&###(///((((((((((((((((((((((*#@\n"
	"@@@@@@@@@@@@*#&&&&%%((////(((((((((((((((((((/*@@@\n"
	"@@@@@@@@@@@@@,(%%&#((////////(((((((((((((((/,@@@@\n"
	"@@@@@@@@@@@@@,////////////////(((((((((((((/*,@@@@\n"
	"@@@@@@@@@@@@***//////////////((((((((((((((/*,@@@@\n"
	"@@@@@@@@@@@***//////////////////(((((((((((/**@@@@\n"
	"@@@@@@@@@@(****///////////////////((((((((///*@@@@\n"
	"@@@@@@@@@@******////////////////////(((((((//**@@@\n"
	"@@@@@@@@@,******////////////////////((((((////(@@@\n"
	"@@@@@@@@@********////////////////////(((((////*@@@\n"
	"@@@@@@@@.************/////////////////(((((///*@@@\n"
	"@@@@@@@@,************////////////////((((/////*@@@\n"
	"@@@@@@@@,************////////////////((((/////,@@@\n"
	"@@@@@@@@***/*******///////////////////////////,%@@\n"
	"@@@@@@@@************//////////////////////////,,@@\n";

int main() {
	for (;;) {
		ClearConsole();
		printf("%s", popcat_closemouth_ascii);
		TimeSleep();
		ClearConsole();
		printf("%s", popcat_openmouth_ascii);
		TimeSleep();
	}

	return 0;
}
