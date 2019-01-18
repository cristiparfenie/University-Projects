#pragma once
#include "Controller.h"

class UI
{
private:
	Controller ctrl;

public:
	UI(const Controller& c) : ctrl(c) {}
    void start();

private:
	static void printMenu();
	static void printRepositoryMenu();
	static void printAdoptionMenu();
	static void printFilterMenu();
	
	int addDogToRepo();
	int RemoveToRepo();
	int UpdateRepo();
	void displayAllDogsRepo();
	void displayAdoption();
	Repository displayFilter();
};