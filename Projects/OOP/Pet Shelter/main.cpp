#include "Dog.h"
#include "UI.h"
#include <Windows.h>
#include "Tests.h"
using namespace std;

int main()
{
	system("color f9");
	Test::All();
	Repository repo{};
	Dog d1{ "Huskey","Oscar",5,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjrs6awz4XaAhUNaFAKHV0lCvUQ_AUICigB&biw=1366&bih=693#imgrc=HXopYIUkNOGE3M:" };
	Dog d2{ "Akita","Coco",2,"https://www.google.ro/search?q=akita&client=firefox-b-ab&dcr=0&tbm=isch&source=iu&ictx=1&fir=Vhnjrc62vpjEmM%253A%252CwRSql48lAZzkOM%252C_&usg=__ByGWZ51KS4TFhseHa9L_hu3WfPk%3D&sa=X&ved=0ahUKEwja6qPL0YXaAhUEPFAKHfrkAvUQ_h0IiwIwFg#imgrc=0EKiz-F7WH3KiM:" };
	Dog d3{ "Beagle","Toby",10,"https://www.google.ro/search?q=beagle&client=firefox-b-ab&dcr=0&tbm=isch&source=iu&ictx=1&fir=hPlgeHW2mBsILM%253A%252CLWcY9XL5rvXonM%252C_&usg=__QC6OnYL_DBYUOAZpJglJWWSjm_M%3D&sa=X&ved=0ahUKEwiJpf_80YXaAhWRYVAKHfHGC_wQ_h0I6wEwFQ#imgrc=hPlgeHW2mBsILM:" };
	Dog d4{ "Boxer","Ollie",6,"https://www.google.ro/search?q=boxer&client=firefox-b-ab&dcr=0&tbm=isch&source=iu&ictx=1&fir=v6bJ3bjVb4WgKM%253A%252C_252TasA827QTM%252C_&usg=__g9_JQ9DcfZd-Cc3XFv2Jr8xodf8%3D&sa=X&ved=0ahUKEwiu6uaw0oXaAhVDPVAKHTo_BfUQ_h0I7gEwFw#imgrc=v6bJ3bjVb4WgKM:" };
	Dog d5{ "Bulldog","Maxi",4,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjrybPq0oXaAhVRIlAKHWIwA_QQ_B0I0QEwEw..i&docid=35PzRdNy1f4rWM&itg=1&client=firefox-b-ab&sa=X&ved=0ahUKEwjrybPq0oXaAhVRIlAKHWIwA_QQ_B0I0QEwEw" };
	Dog d6{ "Dalmatian","Jack",1,"https://www.google.ro/search?q=dalmatian&client=firefox-b-ab&dcr=0&tbm=isch&source=iu&ictx=1&fir=ge8ZGSH1LiyWLM%253A%252CUgTKz7EjJBEM-M%252C_&usg=__htcIanMl50h9wN0P0LLJ5_iVerY%3D&sa=X&ved=0ahUKEwjtoK2k04XaAhWGJVAKHdalBvUQ_h0IrAEwFg#imgrc=ge8ZGSH1LiyWLM:" };
	Dog d7{ "German Shepherd","Leo",7,"https://www.google.ro/search?q=german+shepherd&client=firefox-b-ab&dcr=0&tbm=isch&source=iu&ictx=1&fir=-gPaUIDGWP75aM%253A%252CX7mTrLR6PqtHxM%252C_&usg=__-ds_qH7Hi0JwpEmf7XX4N9XDbmo%3D&sa=X&ved=0ahUKEwie3YzX04XaAhWPPFAKHTx4CfEQ_h0I7wEwFw#imgrc=-gPaUIDGWP75aM:" };
	Dog d8{ "Caucazian Shephard","Max",8,"https://www.google.com/imgres?imgurl=https://www.dogbreedinfo.com/images18/CentralAsianOvtcharkaTurkmenAlabaiMale187.JPG&imgrefurl=https://www.dogbreedinfo.com/caucasianowtcharka.htm&h=342&w=375&tbnid=F1-rVoGCZjRavM:&tbnh=183&tbnw=200&usg=__Nl3bWWqtqE_k36SXq1vGANNWwqY%3D&vet=10ahUKEwiY2bTrqI7aAhVSkRQKHYahDzMQ_B0IwwEwEw..i&docid=T0hWKTx6CnYubM&itg=1&client=firefox-b-ab&sa=X&ved=0ahUKEwiY2bTrqI7aAhVSkRQKHYahDzMQ_B0IwwEwEw#h=342&imgdii=RHFD_mcsfVgc-M:&tbnh=183&tbnw=200&vet=10ahUKEwiY2bTrqI7aAhVSkRQKHYahDzMQ_B0IwwEwEw..i&w=375" };
	Dog d9{ "Pitbull","John",1,"https://www.google.com/search?q=pitbull+puppy&client=firefox-b-ab&tbm=isch&source=iu&ictx=1&fir=sv5Jm_4dFncSDM%253A%252CQ289gIrDYs2X4M%252C_&usg=__P70esHE7DzR9wWb2vIyTSTsTIcQ%3D&sa=X&ved=0ahUKEwjkgI2yqY7aAhVMOhQKHcMbBb8Q_h0I7QEwGA#imgrc=sv5Jm_4dFncSDM:" };
	Dog d10{ "Poodle","Mark",4,"https://www.google.com/imgres?imgurl=http://cdn1-www.dogtime.com/assets/uploads/gallery/poodle-dog-breed-pictures/thumbs/thumbs_greaycoat-5.jpg&imgrefurl=http://dogtime.com/dog-breeds/poodle&h=295&w=190&tbnid=eJXlW6Gx40_eMM:&tbnh=186&tbnw=119&usg=__5zjKLxC2DYWoFHqDN6t0MKY_FIU%3D&vet=10ahUKEwjr5-zwqY7aAhUMNxQKHUZzB-IQ_B0IzwEwCw..i&docid=k5CQ5E-T8Qm87M&itg=1&client=firefox-b-ab&sa=X&ved=0ahUKEwjr5-zwqY7aAhUMNxQKHUZzB-IQ_B0IzwEwCw" };
	Dog d11{ "Huskey","Charilie",5,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=40gAUHUaF6-ArM:" };
	Dog d12{ "Huskey","Jake",10,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=FPj-Ghn5maJruM: " };
	Dog d13{ "Huskey","Cody",1,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=4vzyIiqDaKZT-M:" };
	repo.addDog(d1);
	repo.addDog(d2);
	repo.addDog(d3);
	repo.addDog(d4);
	repo.addDog(d5);
	repo.addDog(d6);
	repo.addDog(d7);
	repo.addDog(d8);
	repo.addDog(d9);
	repo.addDog(d10);
	repo.addDog(d11);
	repo.addDog(d12);
	repo.addDog(d13);
	Controller ctrl{ repo };
	UI ui{ ctrl };
	ui.start();
	return 0;
}