#pragma once
#include "Dog.h"
#include "DynamicArray.h"

class Repository
{
private:
	DynamicVector<Dog> dogs;
	int current ;
public:
	/*
	Default constructu=or.
	Initializes an object of type repository.
	*/
	Repository();

	/*
	Adds a dog to the repository.
	Input: d - Dog.
	Output: 1 if the dog was added 0 otherwise
	*/
	int addDog(const Dog& d);

	//find the position of a dog
	int findPos(const std::string& name);

	//remove a dog from repository
	//in:the name
	//out:1 if the dog was removed,0 otherwise
	int del(const std::string& name);

	/*
	Finds a dog, by name.
	Input: name- string
	Output: the dog that was found, or an "empty" dog if nothing was found.
	*/
	/*Dog findByName(const std::string& name);*/

	//update a dog from repository
	//in:the name and the new age
	//out:1 if the dog was updated, 0 otherwise
	int update(const std::string& name, int age);

	int len();


	Dog getCurrentDog();

	//show a picture with the current dog
	//void showDog();

	//show the next dog 
	void next();

	DynamicVector<Dog> getDogs() const { return dogs; };

};
