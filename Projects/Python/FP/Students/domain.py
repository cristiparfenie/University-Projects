
class IDObject():
    """
    Base class for all objects having unique id within the application
    """

    def __init__(self, objectId):
        """
        Constructor method for building IDObject
        objectId - the unique objectId of the object in the application
        """
        self._objectId = objectId

    def getId(self):
        """
        Return the object's unique id
        """
        return self._objectId

class Student(IDObject):
    def __init__(self,studentId,name):
       IDObject.__init__(self,studentId)
       self.__name=name
    def getName(self):
        return self.__name
    def setName(self,name):
         self.__name=name
    def __eq__(self, z):
        if isinstance(z,Student) == False:
            return False
        return self.getId() == z.getId()
    def __str__(self):
        return "studentId: " + str(self.getId()) + ", student name: " +  str(self.__name)

class Discipline(IDObject):
    def __init__(self,disciplineId,Discipline):
        IDObject.__init__(self,disciplineId)
        self.__Discipline=Discipline
    def getName(self):
        return self.__Discipline
    def setName(self,Discipline):
        self.__Discipline=Discipline
    def __eq__(self, z):
        if isinstance(z,Discipline) == False:
            return False
        return self.getId() == z.getId()
    def __str__(self):
        return "diciplineId: " + str(self.getId()) + ", Discipline: " + str(self.getName())

class Grade(IDObject):
    def __init__(self,gradeId,studentId,disciplineId,grade):
        IDObject.__init__(self,gradeId)
        self.__disciplineId = disciplineId
        self.__studentId = studentId
        self.__grade=grade

    def getDisciplineId(self):
        return self.__disciplineId

    def getStudentId(self):
        return self.__studentId
    def getGrade(self):
        return self.__grade
    def setDisciplineId(self,disciplineId):
        self.__disciplineId=disciplineId
    def setStudentId(self,studentId):
        self.__studentId=studentId
    def setGrade(self,grade):
        self.__grade=grade

    def __str__(self):
        return "grade Id: " + str(self.getId()) + ", studentId: " + str(self.getStudentId()) + ", disciplineId: " + str(self.getDisciplineId()) + ", grade: " + str(self.getGrade())