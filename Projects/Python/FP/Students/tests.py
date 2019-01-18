import unittest
from domain import *
from repository import *
class Test(unittest.TestCase):
   def testGetStudentId(self):
       s1=Student(1,"edward")
       self.assertEqual(s1.getId(),1)
   def testGetName(self):
       s1=Discipline(2,"info")
       self.assertEqual(s1.getName(),"info")
   def testGetDisciplineId(self):
       d1=Discipline(1,"electrica")
       self.assertEqual(d1.getId(),1)

   def testNameDiscipline(self):
       d1 = Discipline(1,"electrica")
       self.assertEqual(d1.getName(),"electrica")

   def testGetGradeId(self):
       g1=Grade(2,3,4,6)
       self.assertEqual(g1.getId(),2)

class RepoTest(unittest.TestCase):
    def testAddStudent(self):
        r=Repository()
        z=Student(1,"Marian")
        r.add(z)
        self.assertEqual(r.getIndex(0),z)
    def testAddDiscipline(self):
        r=Repository()
        z=Discipline(1,"info")
        r.add(z)
        self.assertEqual(r.getIndex(0), z)
    def testAddGrade(self):
        r=Repository()
        z=Grade(1,2,3,8)
        r.add(z)
        self.assertEqual(r.getIndex(0),z)
    def testFind(self):
        r = Repository()
        z=Student(1,"Marian")
        z1=Student(2,"poli")
        r.add(z)
        r.add(z1)
        self.assertEqual(r.find(2),z1)
