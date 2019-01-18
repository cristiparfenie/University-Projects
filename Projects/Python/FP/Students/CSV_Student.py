from repository import *
from domain import *
class StudentCSVFileRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def store(self, client):
        Repository.add(self, client)
        self.__storeToFile()

    def delete(self,studentId):
        Repository.delete(self,studentId)
        self.__storeToFile()

    def update(self,newStudent):
        Repository.update(self,newStudent)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs=line.split(",")
                student=Student(int(attrs[0]),attrs[1])
                Repository.add(self,student)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        students= Repository.getAll(self)
        for student in students:
            strf = str(student.getId()) + "," + student.getName()+"\n"
            f.write(strf)
        f.close()
