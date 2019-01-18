from repository import *
from domain import *
class GradeCSVFileRepository(Repository):
    def __init__(self, fileName="clients.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def store(self,grade):
        Repository.add(self,grade)
        self.__storeToFile()
    ''' 
    def delete(self, clId):
        Repository.delete(self, clientId)
        self.__storeToFile()

    def update(self, newClient):
        Repository.update(self, newClient)
        self.__storeToFile()
    '''
    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                grade=Grade(int(attrs[0]),int(attrs[1]),int(attrs[2]),int(attrs[3]))
                Repository.add(self,grade)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        grades= Repository.getAll(self)
        for grade in grades:
            strf = str(grade.getId()) + "," + str(grade.getStudentId()) + "," + str(grade.getDisciplineId()) + str(grade.getGrade()) + "\n"
            f.write(strf)
        f.close()