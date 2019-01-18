class Operation:
    def __init__(self,functionDo,functionUndo):
        self.__functionDo=functionDo
        self.__functionUndo=functionUndo
    def undo(self):
        self.__functionUndo.call()
    def redo(self):
        self.__functionDo.call()

class FunctionCall():
    def __init__(self,functionRef,*parameters):
        self.__functionRef=functionRef
        self.__parameters=parameters
    def call(self):
        self.__functionRef(*self.__parameters)

class UndoController:
    def __init__(self):
        self.__operation=[]
        self.__index=-1
        self.__recorded=True

    def newOperation(self):
        if self.isRecorded()==False:
            return
        self.__operation=self.__operation[0:self.__index+1]
        self.__operation.append([])
        self.__index+=1

    def recordOperation(self,operation):
        if self.isRecorded()==True:
            self.__operation[-1].append(operation)

    def isRecorded(self):
        return self.__recorded

    def undo(self):
        if self.__index<0:
            return False
        self.__recorded=False
        for oper in self.__operation[self.__index]:
            oper.undo()
        self.__recorded=True
        self.__index-=1
        return True

    def redo(self):
        self.__index +=1
        if self.__index>=len(self.__operation):
            return False
        self.__recorded=False
        for oper in self.__operation[self.__index]:
            oper.redo()
        self.__recorded=True
        return True