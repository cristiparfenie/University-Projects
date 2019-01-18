from controller import *
from undo import *
class UI:
    def __init__(self,undoController,controller1,controller2,controller3):
        self.__studentController=controller1
        self.__disciplineController=controller2
        self.__gradeController=controller3
        self.__undoController=undoController
    def printMenu(self):
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add a student\n'
        string += '\t 2 - List the students\n'
        string += '\t 3 - Remove a student\n'
        string += '\t 4 - Update students\n'
        string += '\t 5 - Add a discipline\n'
        string += '\t 6 - List the disiciplines\n'
        string += '\t 7 - Remove a discipline\n'
        string += '\t 8 - Update disciplines\n'
        string += '\t 9 - Add a grade\n'
        string += '\t 10 - List grades\n'
        string += '\t 11 - Search students\n'
        string += '\t 12 - Search disiciplines\n'
        string += '\t 13 - sorted alphabetically\n'
        string += '\t 14 - sort descending by grade\n'
        string += '\t 15 - Show the failers\n'
        string += '\t 16 - Search disiciplines\n'
        string += '\t 19 - undo\n'
        string += '\t 20 - redo\n'
        string += '\t 0 - Exit\n'
        print(string)

    def mainMenu(self):
        self.printMenu()
        #self.__studentController.addstudents()
        while True:
          command=input("Enter command: ").strip()
          if command == '0':
                    print("exit")
                    break
          elif command=='1':
               ok=1
               try:
                    z=self.readStudent()
                    self.__undoController.newOperation()
                    self.__studentController.addStudent(z)
               except Exception as ve:
                   print(ve)
                   ok=0
               if ok==1:
                   print("added")

          elif command=='2':
             for student in self.__studentController.listStudent():
                   print(student)

          elif command=='3':
               ok = 1
               try:
                   z=self.readId()
                   self.__undoController.newOperation()
                   self.__studentController.delStudent(z)
               except Exception as ve:
                   print(ve)
                   ok = 0
               if ok == 1:
                   print("removed")

          elif command=='4':
               ok = 1
               try:
                   z=self.readStudent()
                   self.__undoController.newOperation()
                   self.__studentController.updateStudent(z)
               except Exception as ve:
                   print(ve)
                   ok=0
               if ok==1:
                   print("upgrated")
          elif command=='5':
               ok=1
               try:
                   z = self.readDiscipline()
                   self.__undoController.newOperation()
                   self.__disciplineController.addDiscipline(z)
               except Exception as ve:
                   print(ve)
                   ok=0
               if ok==1:
                   print("added")
          elif command=='6':
               for discipline in self.__disciplineController.GetAll():
                   print(str(discipline))
          elif command=='7':
               ok = 1
               try:
                z = self.readId()
                self.__undoController.newOperation()
                self.__disciplineController.delDiscipline(z)
                #self.__gradeController.delGrade2(z)
               except Exception as ve:
                   print(ve)
                   ok = 0
               if ok == 1:
                   print("removed")

          elif command=='8':
               ok = 1
               try:
                z = self.readDiscipline()
                self.__undoController.newOperation()
                self.__disciplineController.updateDiscipline(z)
               except Exception as ve:
                   print(ve)
                   ok=0
               if ok==1:
                   print("upgrated")
          elif command=='9':
               ok=1
               try:
                   z=self.readGrade()
                   self.__undoController.newOperation()
                   self.__gradeController.addGrade(z)
               except Exception as ve:
                   print(ve)
                   ok=0
               if ok==1:
                   print("added")

          elif command=='10':
               for grade in self.__gradeController.listGrade():
                   print(str(grade))

          elif command=='11':
               choose=input("choose the search:name/id ")
               if choose=='name':
                 t=input("give the search ")
                 slist=self.__studentController.searchName(t)
                 for i in slist:
                     print(str(i))
               elif choose=="id":
                   t=self.readId()
                   slist=self.__studentController.searchId(t)
                   print(str(slist))
               else:
                   print("invalid choose")

          elif command=='12':
               choose=input("choose the search:name/id ")
               if choose=='name':
                 t=input("give the search ")
                 slist = self.__disciplineController.searchDiscipline(t)
                 for i in slist:
                     print(str(i))
               elif choose=="id":
                   t=self.readId()
                   slist=self.__disciplineController.searchId(t)
                   print(str(slist))
               else:
                   print("invalid choose")

          elif command=='13':
            z=self.readId()
            slist1=self.__gradeController.statistic1(z)
            for i in slist1:
                print(str(i))

          elif command=='14':
               z=self.readId()
               sList2 = self.__gradeController.statistic2(z)
               for i in sList2:
                   print(str(i))

          elif command=='15':
             nr=int(input("how many diciplines do you want to check: "))
             j=0
             fList=[]
             while j<nr:
               z=self.readId()
               fList=self.__gradeController.faillers(z)
               j=j+1
               for i in fList:
                   print(str(i))

          elif command=='16':
               sList2 = self.__gradeController.aggAvg()
               for i in sList2:
                   print("the id: " + str(i[0])+"| the name: " + str(i[1]) + " | with the average: " + str(i[2]))

          elif command=='17':
                z=self.readId()
                t=self.readId()
                sList2 = self.__gradeController.average3(z,t)
                print(sList2)

          elif command=='18':
               sList2=self.__gradeController.aggAvgDis()
               for i in sList2:
                   print("the id: " + str(i[0]) + "| the name: " + str(i[1]) + " | with the average: " + str(i[2]))

          elif command=='19':
             self.__undoController.undo()
          elif command=='20':
             self.__undoController.redo()
          else:
              print("invalid input")

    def readStudent(self):
        id=self.readId()
        name=self.Name()
        return Student(id,name)

    def readRemove(self):
       id=int(input("give an id: "))
       return id

    def readId(self):
       ok=1
       while ok==1:
        try:
           id=int(input("give an id: "))
           return id
        except ValueError:
           print("id is not a number")

    def Name(self):
        ok=1
        while ok==1:
            try:
                name=input("give the name: ")
                if name=="":
                    print("invalid name")
                else:
                    return name
            except ValueError:
                print("invalid")

    def readDiscipline(self):
        id=self.readId()
        discipline=self.Name()
        return Discipline(id,discipline)

    def readGrade(self):
        idGrade=self.readId()
        sid=self.readId()
        did=self.readId()
        grade=self.Grade()
        return Grade(idGrade,sid,did,grade)

    def Grade(self):
        ok=1
        while ok==1:
            try:
                grade=int(input("give a grade: "))
                if grade < 1 or grade > 10:
                    print("invalid grade")
                else:
                    return grade
            except ValueError:
                print("grade is not a number")

