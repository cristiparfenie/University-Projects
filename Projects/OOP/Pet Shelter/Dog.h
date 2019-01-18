#pragma once
#include <iostream>

class Dog
{
private:
	std::string breed;
	std::string name;
	int age;
	std::string source;
public:
	Dog();

	// constructor with parameters
	Dog(const std::string& breed, const std::string& name, int age, const std::string& source);

	std::string getBreed() const { return breed; }
	std::string getName() const { return name; }
	int getAge() const { return age; }
	void setAge(int varsta);
	std::string getSource() const { return source; }
	

	void show();

};