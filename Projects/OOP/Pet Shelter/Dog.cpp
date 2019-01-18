#include "Dog.h"
#include <Windows.h>
#include <shellapi.h>

Dog::Dog() : breed(""), name(""), age(), source("") {}

Dog::Dog(const std::string& breed, const std::string& name, int age, const std::string& source)
{
	this->breed = breed;
	this->name = name;
	this->age = age;

	this->source = source;
}
void Dog::setAge(int varsta)
{
	this->age = varsta;
}
void Dog::show()
{
	ShellExecuteA(NULL, NULL, "firefox.exe", this->getSource().c_str(), NULL, SW_SHOWMAXIMIZED);
}