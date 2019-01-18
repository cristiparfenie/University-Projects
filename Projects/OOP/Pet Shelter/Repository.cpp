#include "Repository.h"
#include <string>

using namespace std;

Repository::Repository()
{
	this->current = 0;

}


int Repository::addDog(const Dog& d)
{
	int i = findPos(d.getName());
	if (i == -1)
		this->dogs.add(d);
		//this->dogs=this->dogs+d;
	else
		return 0;
	return 1;


}
//Dog Repository::findByName(const std::string& name)
//{
//	if (findPos(name) != -1)
//	{
//		Dog dog = this->dogs.getElem(findPos(name));
//	}
//	else
//
//		return Dog{};
//}

int Repository::findPos(const std::string& name)
{

	Dog* dogsInDynamicVector = this->dogs.getAllElems();
	for (int i = 0; i < this->dogs.getSize(); i++)
	{
		Dog d = dogsInDynamicVector[i];
		if (d.getName() == name)
	       return i;
	}
	return -1;


}
int Repository::del(const std::string& name)
{
	int i = findPos(name);
	if (i == -1)
		return 0;
	this->dogs.remove(i);
	return 1;
}
int Repository::update(const std::string& name, int age)
{
	int i = findPos(name);
	if (i == -1)
		return 0;
	Dog* dogsInDynamicVector = this->dogs.getAllElems();
    dogsInDynamicVector[i].setAge(age);
	return 1;
}
int Repository::len()
{
	return this->dogs.getSize();

}

Dog Repository::getCurrentDog()
{
	if (this->current == this->dogs.getSize())
		this->current = 0;
	Dog* dogsInDynamicVector = this->dogs.getAllElems();
	return dogsInDynamicVector[this->current];
	/*Dog d = dogsInDynamicVector[this->current];
	return d;*/
}


//void Repository::showDog()
//{
//	if (this->dogs.getSize() == 0)
//		return;
//	this->current = 0;
//	Dog currentDog = this->getCurrentDog();
//	currentDog.show();
//}

void Repository::next()
{
	if (this->dogs.getSize() == 0)
		return;
	this->current++;
	Dog currentDog = this->getCurrentDog();
	//currentDog.show();
}