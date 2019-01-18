#include "Tests.h"
#include <assert.h>
#include "DynamicArray.h"
#include "Repository.h"
#include "Controller.h"
#include "AdoptionList.h"
void Test::TestDog()
{
	Dog d{ "Bulldog","alvin",5,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw" };
	assert(d.getBreed() == "Bulldog");
	assert(d.getName() == "alvin");
	assert(d.getAge() == 5);
	assert(d.getSource() == "https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw");
}

void Test::testDynamicVector()
{
	DynamicVector<Dog> dy{ 2 };
	DynamicVector<Dog> dyn{ 2 };
	Dog d{ "Bulldog","alvin",5,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw" };
	Dog d1{ "Huskey","maxi",5,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjrs6awz4XaAhUNaFAKHV0lCvUQ_AUICigB&biw=1366&bih=693#imgrc=HXopYIUkNOGE3M:" };
	dy.add(d);
	dy.add(d1);
	assert(dy.getElem(1).getName() == d1.getName());
	dy.remove(0);
	assert(dy.getSize() == 1);
	

}

void Test::testAdoption()
{
	AdoptionList al = {};
	Dog d{ "Bulldog","alvin",5,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw" };
	assert(al.findPos(d.getName()) == -1);
	assert(al.Add(d) == 1);
	assert(al.Add(d) == 0);
	assert(al.findPos(d.getName()) == 0);
	assert(al.getDogs().getSize() == 1);
}

void Test::testRepo()
{
	Repository repo = {};
	Dog d{ "Bulldog","alvin",5,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw" };
	Dog d2{ "Huskey","Cody",1,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=4vzyIiqDaKZT-M:" };
    Dog* dogsInDynamicVector = repo.getDogs().getAllElems();
    assert(repo.del(d.getName()) == 0);
	assert(repo.update(d.getName(), 4) == 0);
	assert(repo.len() == 0);
	assert(repo.addDog(d) == 1);
	assert(repo.getDogs().getSize() == 1);
	assert(repo.getCurrentDog().getName()==d.getName());
	assert(repo.addDog(d) == 0);
	assert(repo.findPos(d.getName()) == 0);
	assert(repo.del(d.getName()) == 1);
	assert(repo.addDog(d) == 1);
	assert(repo.addDog(d2) == 1);
	repo.next();
	assert(repo.getCurrentDog().getName() == d2.getName());
	assert(repo.update(d.getName(), 4) == 1);
}
void Test::testCtrl()
{
	Repository repo = {};
	Repository reps = {};
	Controller ctrl{ repo };
	Dog d{ "Bulldog","alvin",5,"https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw" };
	Dog d2{ "Huskey","Cody",1,"https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=4vzyIiqDaKZT-M:" };
	assert(ctrl.checkEmpty() == 1);
	assert(ctrl.adopt(d) == 1);
	assert(ctrl.adopt(d) == 0);
	assert(ctrl.getReps().addDog(d) == 1);
	assert(ctrl.getReps().addDog(d2) == 1);
	
	ctrl.nextD();
	assert(ctrl.getReps().getCurrentDog().getName() != d2.getName());
	assert(ctrl.addDogToRepo("Bulldog", "alvin", 5, "https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw") == 1);
	assert(ctrl.addDogToRepo("Huskey", "Cody", 1, "https://www.google.ro/search?q=husky&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLs5fNtJnaAhUxsaQKHfIaCowQ_AUICigB&biw=1366&bih=693#imgrc=4vzyIiqDaKZT-M:") == 1);
	ctrl.nextDog();
	assert(ctrl.getRepo().getCurrentDog().getName() == d2.getName());
	assert(ctrl.filtrare("Huskey", 5).len() == 1);
	
	assert(ctrl.getRepo().getDogs().getSize()== 2);
	assert(ctrl.getAdoptionList().getDogs().getSize() == 1);
	assert(ctrl.getReps().getDogs().getSize() == 1);
	assert(ctrl.addDogToRepo("Bulldog", "alvin", 5, "https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw") == 0);
	assert(ctrl.deleteController(d.getName()) == 1);
	assert(ctrl.addDogToRepo("Bulldog", "alvin", 5, "https://www.google.ro/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/e/e9/CH_Buck_and_Sons_Evita_Peron.jpg&imgrefurl=https://en.wikipedia.org/wiki/Bulldog&h=1142&w=956&tbnid=6saCMCQ78sa_CM:&tbnh=186&tbnw=155&usg=__iV_2MAmEaPqyaHOTJHH8RKRQ0bM%3D&vet=10ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw..i&docid=35PzRdNy1f4rWM&itg=1&sa=X&ved=0ahUKEwjIzqeNjY3aAhWOK1AKHdjyBeUQ_B0IxQEwEw") == 1);
	assert(ctrl.updateController(d.getName(), 6) == 1);
}

void Test::All()
{
	TestDog();
	testDynamicVector();
	testRepo();
	testCtrl();
	testAdoption();
}
