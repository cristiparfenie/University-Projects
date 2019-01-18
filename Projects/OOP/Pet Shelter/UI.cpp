#include "UI.h"
#include <string>
using namespace std;


void UI::printMenu()
{
	cout << "Choose the mode: " << endl;
	cout << "\t 1 - Administrator mode " << endl;
	cout << "\t 2 - User mode " << endl;
}


void UI::printRepositoryMenu()
{
	cout << "Possible commands: " << endl;
	cout << "\t 1 - Add a dog." << endl;
	cout << "\t 2 - Remove a dog." << endl;
	cout << "\t 3 - Update a dog." << endl;
	cout << "\t 4 - Display all." << endl;
	cout << "\t 0 - Back." << endl;
}

void UI::printAdoptionMenu()
{
	cout << "Possible commands: " << endl;
	cout << "\t 1 - See  the dogs in  the  database, one  by  one" << endl;
	cout << "\t 2 - Adopt the dog" << endl;
	cout << "\t 3 - See the next dog" << endl;
	cout << "\t 4 - See the adoption list." << endl;
	cout << "\t 5 - See all the dogs of a given breed, having an age less than a given number" << endl;
	cout << "\t 0 - Back." << endl;
}
void UI::printFilterMenu()
{
	cout << "Possible commands: " << endl;
	cout << "\t 1 - See  the dogs in  the  database, one  by  one" << endl;
	cout << "\t 2 - Adopt the dog" << endl;
	cout << "\t 3 - See the next dog" << endl;
}

int UI::addDogToRepo()
{

	cout << "Enter the breed: ";
	std::string breed;
	cin >> breed;
	cout << "Enter the name: ";
	std::string name;
	cin >> name;
	cout << "Enter the age: ";
	int age;
	cin >> age;
	cout << "Youtube link: ";
	std::string link;
	cin >> link;
	return this->ctrl.addDogToRepo(breed, name, age, link);
}

int UI::RemoveToRepo()
{
	cout << "Enter the name: ";
	std::string name;
	cin >> name;
	return this->ctrl.deleteController(name);

}
int UI::UpdateRepo()
{
	cout << "Enter the name: ";
	std::string name;
	cin >> name;
	cout << "Enter the new age: ";
	int age;
	cin >> age;
	return this->ctrl.updateController(name, age);
}
void UI::displayAllDogsRepo()
{
	DynamicVector<Dog> v = this->ctrl.getRepo().getDogs();
	Dog* dogs = v.getAllElems();
	if (dogs == NULL)
		return;
	if (v.getSize() == 0)
	{
		cout << "There are no dogs in the repository." << endl;
		return;
	}

	for (int i = 0; i < v.getSize(); i++)
	{
		Dog d = dogs[i];
		cout << d.getBreed() << " - " << d.getName() << "- " << d.getAge() << " years " << endl;
	}
}
void UI::displayAdoption()
{
	DynamicVector<Dog> v = this->ctrl.getAdoptionList().getDogs();
	Dog* dogs = v.getAllElems();
	if (dogs == NULL)
		return;
	if (v.getSize() == 0)
	{
		cout << "There are no dogs in the adoption list" << endl;
		return;
	}

	for (int i = 0; i < v.getSize(); i++)
	{
		Dog d = dogs[i];
		cout << d.getBreed() << " - " << d.getName() << "- " << d.getAge() << " years " << endl;
	}

}
Repository UI::displayFilter()
{
	cout << "Enter the breed: ";
	std::string breed;
	cin >> breed;
	cout << "Enter the age: ";
	int age;
	cin >> age;

	Repository re;
	re = this->ctrl.filtrare(breed, age);
	return re;
	/*DynamicVector<Dog> v = re.getDogs();
	Dog* dogs = v.getAllElems();
	
	for(int i=0;i<v.getSize();i++)
	{
		Dog d = dogs[i];
		cout << d.getBreed() << " - " << d.getName() << "- " << d.getAge() << " years " << endl;
	}*/
}


void UI::start()
{

	while (true)
	{
		printMenu();
		int command;
		cout << "please give the comand: ";
		cin >> command;
		if (command == 0)
			break;
		if (command == 1)
		{
			printRepositoryMenu();
			while (true)
			{
			
				int commandR;
				cout << "please give the comand: ";
				cin >> commandR;
				if (commandR == 0)
					break;
				switch (commandR)
				{
				case 1:
				{
					if (this->addDogToRepo() == 1)
						cout << "the dog was added\n";

					else
						cout << "the dog can not be added because there exists another dog with this name\n";
					break;
				}
				case 2:
				{
					if (this->RemoveToRepo() == 1)
						cout << "the dog was removed\n";
					else
						cout << "the dog can not be removed because it doesn't exist in the shelter\n";
					break;
				}
				case 3:
				{
					if (this->UpdateRepo() == 1)
						cout << "the dog was updated\n";
					else
						cout << "the dog can not be updated because it doesn't exist in the shelter\n";
					break;
				}
				case 4:
				{
					this->displayAllDogsRepo();
					break;
				}
				}
			}
		}

		if (command == 2)
		{
			printAdoptionMenu();
			while (true)
			{
				
				int commandA;
				cout << "please give the comand: ";
				cin >> commandA;
				if (commandA == 0)
					break;
				else if (commandA == 1)
				{

					Dog d = this->ctrl.getRepo().getCurrentDog();
					cout << "The breed: " << d.getBreed() << " - His name is: " << d.getName() << "- and has " << d.getAge() << " years" << endl;
					d.show();
					//this->ctrl.getRepo().showDog();

				}
				else if (commandA == 2)
				{
					Dog d = this->ctrl.getRepo().getCurrentDog();
					if (this->ctrl.adopt(d) == 1)
						cout << "the dog was added" << endl;
					else
						cout << "the dog is already adopted" << endl;
				}
				else if (commandA == 3)
				{
					this->ctrl.nextDog();
					Dog d = this->ctrl.getRepo().getCurrentDog();
					cout << "The breed: " << d.getBreed() << " - His name is: " << d.getName() << "- and has " << d.getAge() << " years" << endl;
					d.show();
				}
				else if (commandA == 4)
				{

					this->displayAdoption();

				}
				else if (commandA == 5)
				{
					//Repository re;
					this->displayFilter();
					printFilterMenu();
					while (true)
					{
						int commandF;
						cout << "please give the comand: ";
						cin >> commandF;
						if (commandF == 0)
							break;
						else if (commandF == 1)
						{
							if (this->ctrl.checkEmpty())
							{
								cout << "there are no such dogs" << endl;
								break;
							}
							else
							{
								Dog d = this->ctrl.getReps().getCurrentDog();
								cout << "The breed: " << d.getBreed() << " - His name is: " << d.getName() << "- and has " << d.getAge() << " years" << endl;
								//this->ctrl.getReps().showDog();
								d.show();
							}
						}
						else if (commandF == 2)
						{
							Dog d = this->ctrl.getReps().getCurrentDog();
							if (this->ctrl.adopt(d) == 1)
								cout << "the dog was added" << endl;
							else
								cout << "the dog is already adopted" << endl;
							
						}
						else if (commandF == 3)
						{
							if (this->ctrl.checkEmpty())
							{
								cout << "there are no such dogs" << endl;

							}
							this->ctrl.nextD();
							Dog d = this->ctrl.getReps().getCurrentDog();
							cout << "The breed: " << d.getBreed() << " - His name is: " << d.getName() << "- and has " << d.getAge() << " years" << endl;
							d.show();
						}

					}

				}


			}

		}
	}

}