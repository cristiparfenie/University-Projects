#include "Controller.h"
int Controller::addDogToRepo(const std::string& breed, const std::string& name, int age, const std::string& source)
{
	Dog d{ breed,name,age,source };
	int res = this->repo.addDog(d);
	return res;
}
int Controller::deleteController(const std::string& name)
{
	int res = this->repo.del(name);
	return res;
}

int Controller::updateController(const std::string& name, int age)
{
	int res = this->repo.update(name, age);
	return res;
}

int Controller::adopt(const Dog& d)
{
	int res = this->AL.Add(d);
	return res;
}


//void Controller::showPic()
//{
//	this->repo.showDog();
//}

void Controller::nextDog()
{
	this->repo.next();
}
void Controller::nextD()
{
	this->reps.next();
}
Repository Controller::filtrare(const std::string& breed, int age)
{
	
	for (int i = 0; i < this->repo.getDogs().getSize(); i++)
	{
		Dog d = this->repo.getDogs().getElem(i);
		const std::string& br = d.getBreed();
	    if (br==breed && d.getAge()<age)
		   this->reps.addDog(d);

	}
	return this->reps;

}
bool Controller::checkEmpty()
{
	return this->reps.getDogs().getSize() == 0;
}