#pragma once
#include "Repository.h"
#include "AdoptionList.h"

class Controller
{
private:
	Repository repo;
	AdoptionList AL;
	Repository reps;

public:
	Controller(const Repository& r) : repo{ r } {}

	Repository getRepo() const { return repo; }
	AdoptionList getAdoptionList() const { return AL; }
	Repository getReps() const { return reps; }
	// Adds a dog with the given data to the repository.
	int addDogToRepo(const std::string& breed, const std::string& name, int age, const std::string& source);

	int deleteController(const std::string& name);

	int updateController(const std::string& name, int age);

	int adopt(const Dog& d);


	void showPic();
	void nextDog();

	void nextD();
	Repository filtrare(const std::string& breed, int age);
	
	bool checkEmpty();
};
