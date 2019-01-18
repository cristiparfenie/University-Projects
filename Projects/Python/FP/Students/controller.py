from repository import *
from domain import *
from undo import *
class ControllerStudent:
    def __init__(self,repo1,undoController,controller3):
        self.__repository=repo1
        self.__undoController=undoController
        self.__g=controller3

    def addStudent(self,Student):
        self.__repository.add(Student)
        redo=FunctionCall(self.addStudent,Student)
        undo=FunctionCall(self.delStudent,Student.getId())
        operation=Operation(redo,undo)
        self.__undoController.recordOperation(operation)



    def updateStudent(self,Student):
        l=Student.getId()
        S = self.__repository.find(l)
        self.__repository.update(Student)
        redo = FunctionCall(self.updateStudent,Student)
        undo=FunctionCall(self.updateStudent,S)
        operation=Operation(redo,undo)
        self.__undoController.recordOperation(operation)

    def delStudent(self,StudentId):
        S=self.__repository.find(StudentId)
        grades=[]
        gr=self.__g.listGrade()
        for g in gr:
            if g.getStudentId()==StudentId:
                grades.append(g)
        self.__repository.delete(StudentId)
        self.__g.delGrade1(StudentId)
        redo=FunctionCall(self.delStudent,StudentId)
        undo=FunctionCall(self.addStudent,S)
        operation=Operation(redo,undo)
        self.__undoController.recordOperation(operation)
        redo=FunctionCall(self.__g.delGrade1,StudentId)
        undo=FunctionCall(self.__g.forUndo,grades)
        operation = Operation(redo,undo)
        self.__undoController.recordOperation(operation)

    '''
    def forUndo2(self,StudentId):
        n=self.__g.forUndo(StudentId)
        d=self.__g.delGrade1(StudentId)
        for x in n:
            d.append(x)
    '''

    def listStudent(self):
         return self.__repository.getAll()

    def searchName(self,name):
        mylist=[]
        mylist=self.listStudent()
        return list(filter(lambda student:name.strip().lower() in student.getName().lower(),mylist))

    def searchId(self,id):
        S=self.__repository.find(id)
        return S

class ControllerDiscipline:
    def __init__(self,repo2,undoController,controller3):
        self.__repository=repo2
        self.__undoController=undoController
        self.__g=controller3

    def addDiscipline(self,Discipline):
        self.__repository.add(Discipline)
        redo = FunctionCall(self.addDiscipline,Discipline)
        undo = FunctionCall(self.delDiscipline,Discipline.getId())
        operation=Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def updateDiscipline(self,Discipline):
        S = self.__repository.find(Discipline.getId())
        self.__repository.update(Discipline)
        self.__repository.update(Discipline)
        redo = FunctionCall(self.updateDiscipline,Discipline)
        undo = FunctionCall(self.updateDiscipline,S)
        operation = Operation(redo,undo)
        self.__undoController.recordOperation(operation)

    def delDiscipline(self,DisciplineId):
        D=self.__repository.find(DisciplineId)
        grades=[]
        gr=self.__g.listGrade()
        for g in gr:
            if g.getDisciplineId()==DisciplineId:
                grades.append(g)
        self.__repository.delete(DisciplineId)
        self.__g.delGrade2(DisciplineId)
        redo=FunctionCall(self.delDiscipline,DisciplineId)
        undo=FunctionCall(self.addDiscipline,D)
        operation=Operation(redo,undo)
        self.__undoController.recordOperation(operation)
        redo = FunctionCall(self.__g.delGrade2,DisciplineId)
        undo = FunctionCall(self.__g.forUndo,grades)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def GetAll(self):
        return  self.__repository.getAll()

    def searchDiscipline(self,dis):
        mylist=[]
        mylist = self.GetAll()
        return list(filter(lambda discipline : dis.strip().lower() in discipline.getName().lower(), mylist))

    def searchId(self,id):
        S=self.__repository.find(id)

class ControllerGrade(ControllerStudent,ControllerDiscipline):
    def __init__(self,repo3,repo1,repo2,undoController):
        self.__repository=repo3
        ControllerStudent.__init__(self,repo1,undoController,repo3)
        ControllerDiscipline.__init__(self,repo2,undoController,repo3)
        #self.__s = controller1
        #self.__d = controller2

        self.__undoController=undoController

    def addGrade(self,grade):
        #sid=self.__repository.find(sid)
        #did=self.__repository.find(did)
        #grade=Grade(id,sid,did,grade)
        self.__repository.add(grade)
        redo=FunctionCall(self.addGrade,grade)
        undo=FunctionCall(self.removeG,grade.getId())
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def listGrade(self):
        return self.__repository.getAll()

    def search(self):
          return self.__repository.getAll()

    def removeG(self,grade):
        self.__repository.delete(grade)

    def delGrade1(self,Student):
        Id=Student
        mylist=[]
        mylist2=[]
        mylist=self.listGrade()
        i=0
        n=len(mylist)
        while i<n:
            if mylist[i].getStudentId()==Id:
              mylist.remove(mylist[i])
              n=n-1
              i=i-1
            i=i+1
        return mylist

    def forUndo(self,grades):
        #k=0
        for i in grades:
            self.__repository.add(i)

    def delGrade2(self,Id):
        mylist=[]
        mylist=self.listGrade()
        i = 0
        n = len(mylist)
        while i<n:
            if mylist[i].getDisciplineId()==Id:
                mylist.remove(mylist[i])
                n=n-1
                i=i-1
            i=i+1
        return mylist

    def statistic1(self,discip):
        new=[]
        stat1=[]
        liststudents=[]
        listg=self.listGrade()
        for i in range(len(listg)):
            if listg[i].getDisciplineId()==discip:
                new.append(listg[i].getStudentId())
        #liststudents=self.__s.listStudent()
        liststudents = ControllerStudent.listStudent(self)
        n=len(new)
        l=len(liststudents)
        for i in range(0,n):
            for j in range(0,l):
                if new[i]==liststudents[j].getId():
                        stat1.append((liststudents[j]))
        stat1.sort(key=lambda x:x.getName())
        stat1=self.verify(stat1)
        return stat1

    def verify(self,mylist):
        i=0
        n=len(mylist)
        while i<n-1:
            j=i+1
            while j<n:
                if mylist[i] == mylist[j]:
                    mylist.pop(j)
                    n=n-1
                    j=j-1

                j=j+ 1
            i=i+1
        return mylist

    def average(self,discip):
        s=0
        k=0
        av=[]
        stud=self.statistic1(discip)
        #return stud
        listg=self.listGrade()
        for i in stud:
            s=0
            k=0
            for l in listg:
                if i.getId()==l.getStudentId() and l.getDisciplineId()==discip:
                     s=s+l.getGrade()
                     k=k+1
            if k==0:
                k=1
            average=float(s/k)
            av.append(average)
        return av

    def average1(self,discip):
        av=[]
        #stud=self.__s.listStudent()
        stud = ControllerStudent.listStudent(self)
        #return stud
        listg=self.listGrade()
        for i in stud:
            s=0
            k=0
            for l in listg:
                if i.getId()==l.getStudentId() and l.getDisciplineId()==discip:
                     s=s+l.getGrade()
                     k=k+1
            if k == 0:
                k = 1
            average=float(s/k)
            av.append(average)
        return av

    def statistic2(self,discip):
        stud=self.statistic1(discip)
        av=self.average(discip)
        for i in range(0,len(av)):
            for j in range(i+1,len(av)):
                if av[i]<av[j]:
                    av[i],av[j]=av[j],av[i]
                    stud[i],stud[j]=stud[j],stud[i]
        return stud

    def faillers(self,discip):
         fail=[]
         #stud=self.__s.listStudent()
         #for disciplines in discip:
         stud=ControllerStudent.listStudent(self)
         av=self.average1(discip)
         for i in range (0,len(av)-1):
            if av[i]>0 and av[i]<5:
                  fail.append(stud[i])
         fail=self.verify(fail)
         return fail

    def average3(self,sid,did):
        s=0
        k=0
        grade=self.listGrade()
        for grades in grade:
            if grades.getDisciplineId()==did and grades.getStudentId()==sid:
                s=s+grades.getGrade()
                k=k+1
        if s==0:
            k=1
        return float(s/k)

    def aggAvg(self):
        agglist=[]
        #stud=self.__s.listStudent()
        stud=ControllerStudent.listStudent(self)
        #discipline=self.__d.GetAll()
        discipline=ControllerDiscipline.GetAll(self)
        for students in stud:
            s=0
            k=1
            for disciplines in discipline:
                a=self.average3(students.getId(),disciplines.getId())
                if a!=0:
                  s=s+a
                  k=k+1
            k=k-1
            if k==0:
                k=1
            t=[students.getId(),students.getName(),float(s/k)]
            agglist.append(t)
            agglist.sort(key=lambda x:x[2],reverse=True)
        return agglist

    def aggAvgDis(self):
        agglist=[]
        #stud=self.__s.listStudent()
        stud=ControllerStudent.listStudent(self)
        discipline=ControllerDiscipline.GetAll(self)
        for disciplines in discipline:
            s=0
            k=1
            for students in stud:
                a=self.average3(students.getId(),disciplines.getId())
                if a!=0:
                  s=s+a
                  k=k+1
            k=k-1
            if k == 0:
                k = 1
            t=[disciplines.getId(),disciplines.getName(),float(s/k)]
            agglist.append(t)
            agglist.sort(key=lambda x:x[2],reverse=True)
        return agglist





class ControllerException(Exception):
        """
        Exception class for repository errors
        """

        def __init__(self, message):
            """
            Constructor for repository exception class
            message - A string representing the exception message
            """
            self.__message = message

        def __str__(self):
            return self.__message
