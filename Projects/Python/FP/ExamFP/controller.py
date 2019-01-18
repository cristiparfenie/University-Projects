from repository import *
import random
class Controller:
    def __init__(self,data=Repository()):
        self.__repo=data
        self.__need=None
        self.__all=None
        self.__score=0
        self.__words=None
        self.__undo=None
    def get(self,index):
        '''
        Returns the element on the given index, -1 if it is not possible
        in:param index:
        :return:
        '''
        if index>=len(self.__repo.getAll()):
            return -1
        return self.__repo.get(index)
    def getMine(self):
        '''
        Returns self.__all
        :return:
        '''
        return self.__all
    def add(self,el):
        '''
        Adds an element to the controller list
        in:param el:
        :return:
        '''
        self.__repo.add(el)
    def pickRandomWord(self):
        '''
        Picks a random word or sentence from the controller list and creates the score of the word
        :return:
        '''
        c=0
        n=len(self.__repo.getAll())-1
        x=random.randint(0,n)
        a=self.__repo.get(x)
        for i in range(len(a)):
            if a[i]!=' ':
                c+=1
        self.__undo =a
        self.__all=a
        self.__need=a
        a=a.strip()
        a=a.split()
        self.__words=len(a)
        self.__score=c
        return a
    def scramble(self):
        '''
        Shuffles the letters of each word of the sentence except the first and last letter of each word
        :return:
        '''
        p1=''
        s=self.__all
        s=s.strip()
        s=s.split()
        for i in range(len(s)):
            x=s[i]
            n=len(x)-2
            for b in range(n+1):
                l=''
                k=random.randint(1,n)
                t1=x[k]
                m = random.randint(1, n)
                while m!=k and len(x)>3:
                    m = random.randint(1, n)
                t2=x[m]
                for q in range(n+2):
                    if q==k:
                        l+=str(t2)
                    elif q==m:
                        l+=str(t1)
                    else:
                        l+=str(x[q])
                x=l
            p1+=str(x)+' '
        self.__all=p1

    def GameOver(self):
        '''
        Returns 1 if the game did not end or 0 if it did end
        :return:
        '''
        if self.__score==0:
            return 0
        return 1
    def undo(self):
        '''
        Undoes the last operation
        :return:
        '''
        self.__all=self.__undo
        self.__score+=1
    def switchPairs(self,a,b,word1,word2):
        '''
        Makes a switch between a and b from a given word and decrements the score by 1
        in:param a:
        in:param b:
        '''
        if word1 >=self.__words or word2>=self.__words:
            return False
        s=self.__all
        s=s.strip()
        s=s.split()
        x=s[word1]
        y=s[word2]
        t1=''
        t2=''
        for i in range(len(x)):
            if i==a:
                m=None
                for j in range(len(y)):
                    if j==b:
                        n=x[i]
                        m=y[j]
                        t2+=str(n)
                    else:
                        t2+=str(m)
                t1+=str(m)
            else:
                t1+=str(x[i])
        h=''
        for i in range(len(s)):
            if i==word1:
                h+=str(t1)+' '
            elif i==word2:
                h+=str(t2)+' '
            else:
                h+=str(s[i])+' '
        self.__undo=self.__all
        self.__all=h
        self.__score-=1
        return self.__all
    def __str__(self):
        '''
        Overwrites the str function for this class
        :return:
        '''
        s=''
        s+=str(self.__all)+'   [score is: '+str(self.__score)+']'
        return s
    def checkSame(self):
        '''
        Checks if self.__need and self.__all are the same meaning that the user has found the solution
        :return: self.__score if thy are the same, 0 if not
        '''
        if self.__all==self.__need:
            return self.__score
        return 0