#include "AdoptionList.h"

int AdoptionList::Add(const Dog& d)
{
	int i = findPos(d.getName());
	if (i == -1)
		this->dogs.add(d);
	else
		return 0;
	return 1;
}

int AdoptionList::findPos(const std::string& name)
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


