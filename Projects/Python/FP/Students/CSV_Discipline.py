from repository import *
from domain import *
class DisciplineCSVFileRepository(Repository):
    def __init__(self, fileName="disciplineCSV.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def store(self,student):
        Repository.add(self,student)
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
                discipline=Discipline(int(attrs[0]),attrs[1])
                Repository.add(self,discipline)
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
