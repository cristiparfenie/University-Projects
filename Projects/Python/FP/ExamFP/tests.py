import unittest
from repository import *
from controller import *
class TestRepo(unittest.TestCase):
    def testAdd(self):
        a=Repository()
        a.add('maria are mere')
        a.add('maria are pere')
        a.add('maria are prune')
        self.assertEqual(a.get(0),'maria are mere')
        self.assertEqual(a.get(1), 'maria are pere')
        self.assertEqual(a.get(2), 'maria are prune')

    def testGet(self):
        b = Repository()
        b.add('maria are mere')
        b.add('maria are pere')
        b.add('maria are prune')
        self.assertEqual(b.get(0), 'maria are mere')
        self.assertEqual(b.get(1), 'maria are pere')
        self.assertEqual(b.get(2), 'maria are prune')
    def testGetAll(self):
        c = Repository()
        c.add('maria are mere')
        c.add('maria are pere')
        c.add('maria are prune')
        self.assertEqual(c.getAll(), ['maria are mere','maria are pere','maria are prune'])
class TestController(unittest.TestCase):
    def testAdd(self):
        d = Controller()
        d.add('maria are mere')
        d.add('maria are pere')
        d.add('maria are prune')
        self.assertEqual(d.get(0), 'maria are mere')
        self.assertEqual(d.get(1), 'maria are pere')
        self.assertEqual(d.get(2), 'maria are prune')
    def testPickRandomWord(self):
        e = Controller()
        e.add('maria are mere')
        b=e.pickRandomWord()
        self.assertEqual(b,['maria', 'are', 'mere'])
    #def testScramble(self):

    def testGameOver(self):
        f = Controller()
        f.add('l')
        c = f.pickRandomWord()
        b=f.GameOver()
        self.assertEqual(b,1)
    def testSwitchPairs(self):
        g = Controller()
        g.add('maria are mere')
        c = g.pickRandomWord()
        b=g.switchPairs(1,2,0,1)
        self.assertEqual(b, 'meria ara mere')
    def testCheckSame(self):
        h = Controller()
        h.add('maria are mere')
        c = h.pickRandomWord()
        b=h.checkSame()
        self.assertEqual(b, 12)
    def testUndo(self):
        i = Controller()
        i.add('maria are mere')
        c = i.pickRandomWord()
        b = i.switchPairs(1, 2, 0, 1)
        c=i.undo()
        self.assertEqual(i.getMine(),'maria are mere')
#unittest.main()