from repository import *
from UI import *
from domain import *
from controller import *
from undo import *
from PickleRepository import *
from CSV_Student import *
from CSV_Discipline import *
from CSV_Grades import *
cmd=int(input("give a command: "))
try:
    if cmd==1:
        repo1=PickleRepository("student.txt")
        repo2=PickleRepository("discipline.txt")
        repo3=PickleRepository("grade.txt")
    if cmd==2:
        repo1=StudentCSVFileRepository("studentCSV.txt")
        repo2=DisciplineCSVFileRepository("disciplineCSV.txt")
        repo3=GradeCSVFileRepository("gradeCSV.txt")
    if cmd==3:
        repo1=Repository()
        repo2=Repository()
        repo3=Repository()

        repo1.add(Student(6, "alin"))
        repo1.add(Student(7, "marius"))
        repo1.add(Student(8, "razvan"))
        repo1.add(Student(9, "garl"))
        repo1.add(Student(5, "malina"))
        repo1.add(Student(4, "darius"))
        repo1.add(Student(10, "raul"))
        repo1.add(Student(11, "tudor"))
        repo1.add(Student(13, "george"))
        repo1.add(Student(14, "mihai"))

        repo2.add(Discipline(1, "fizica"))
        repo2.add(Discipline(2, "mate"))
        repo2.add(Discipline(3, "info"))
        repo2.add(Discipline(4, "chimie"))
        repo2.add(Discipline(5, "romana"))
        repo2.add(Discipline(6, "desen"))

        repo3.add(Grade(1, 6, 3, 6))
        repo3.add(Grade(2, 6, 2, 6))
        repo3.add(Grade(3, 6, 3, 2))
        repo3.add(Grade(4, 8, 1, 10))
        repo3.add(Grade(5, 7, 5, 3))
        repo3.add(Grade(6, 7, 3, 4))
        repo3.add(Grade(7, 9, 4, 7))
        repo3.add(Grade(8, 8, 3, 6))
        repo3.add(Grade(9, 11, 5, 7))
        repo3.add(Grade(10, 10, 4, 5))
        repo3.add(Grade(11, 4, 4, 4))
        repo3.add(Grade(12, 5, 6, 1))
    undoController=UndoController()
    #controller1=ControllerStudent(repo1,undoController)
    controller3=ControllerGrade(repo3,repo1,repo2,undoController)
    controller2=ControllerDiscipline(repo2,undoController,controller3)
    controller1=ControllerStudent(repo1,undoController,controller3)

    '''
    repo1.add(Student(6,"alin"))
    repo1.add(Student(7,"marius"))
    repo1.add(Student(8,"razvan"))
    repo1.add(Student(9,"garl"))
    repo1.add(Student(5,"malina"))
    repo1.add(Student(4,"darius"))
    repo1.add(Student(10,"raul"))
    repo1.add(Student(11,"tudor"))
    repo1.add(Student(13,"george"))
    repo1.add(Student(14,"mihai"))



    repo2.add(Discipline(1,"fizica"))
    repo2.add(Discipline(2,"mate"))
    repo2.add(Discipline(3,"info"))
    repo2.add(Discipline(4,"chimie"))
    repo2.add(Discipline(5,"romana"))
    repo2.add(Discipline(6,"desen"))
    
    repo3.add(Grade(1, 6, 3, 6))
    repo3.add(Grade(2, 6, 2, 6))
    repo3.add(Grade(3, 6, 3, 2))
    repo3.add(Grade(4,8,1,10))
    repo3.add(Grade(5, 7, 5, 3))
    repo3.add(Grade(6, 7, 3, 4))
    repo3.add(Grade(7, 9, 4, 7))
    repo3.add(Grade(8, 8, 3, 6))
    repo3.add(Grade(9, 11, 5, 7))
    repo3.add(Grade(10, 10, 4, 5))
    repo3.add(Grade(11, 4, 4, 4))
    repo3.add(Grade(12, 5, 6, 1))
    '''

    u=UI(undoController, controller1, controller2, controller3)
    u.mainMenu()
except ValueError:
    print("something is wrong")