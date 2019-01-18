#pragma once
#include "DynamicArray.h"
#include "Dog.h"

class AdoptionList
{
private:
	DynamicVector<Dog> dogs;
	
public:
	//add a dog to the adoption list
	int Add(const Dog& d);
	
	//find the position of a dog
	int findPos(const std::string& name);
	DynamicVector<Dog> getDogs() const { return dogs; };

};