from controller import *
class UI:
    def __init__(self,controller=Controller()):
        self.__c=controller
        self.__w1=None
        self.__w2=None
        self.__p1=None
        self.__p2=None
        self.__count=0
    def showMenu(self):
        s=''
        s+='swap <word1> <letter1> - <word2> <letter2>'
        print(s)
    def start(self):
        again=True
        while again==True:
            again=False
            try:
                a = self.__c.pickRandomWord()

                self.__c.scramble()
            except:
                again=True
        while True:
            try:
                self.showMenu()
                print(self.__c)
                repeat=True
                x=None
                while repeat==True:
                    repeat=False
                    x=input('Enter the command:')
                    if x=='undo':
                        if self.__count!=0:
                            self.__c.undo()
                        else:
                            print("Can't undo this!")
                            repeat=True
                    else:
                        x = x.strip()
                        x = x.split()
                        if str(int(x[1])) != str(x[1]) and str(int(x[2])) != str(x[2]) and str(int(x[4])) != str(
                                x[4]) and str(
                                int(x[5])) != str(x[5]):
                            print('Invalid input!')
                            repeat = True
                        if x[0] != 'swap':
                            print('Invalid command!')
                            repeat = True
                        if len(x) != 6:
                            print('Invalid input!')
                            repeat = True
                self.__w1=int(x[1])
                self.__p1=int(x[2])
                self.__w2=int(x[4])
                self.__p2=int(x[5])
                r=self.__c.switchPairs(self.__p1,self.__p2,self.__w1,self.__w2)
                self.__count+=1
                if r==False:
                    print('Invalid data!')
                else:
                    print('Pairs have been switched!')
                z=self.__c.checkSame()
                if z!=0:
                    print('YOU WON!')
                    break
                y=self.__c.GameOver()
                if y==0:
                    print('You can do better next time!')
                    break
            except:
                repeat=True