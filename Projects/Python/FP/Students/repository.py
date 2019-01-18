from domain import *
import unittest
class Repository:
    def __init__(self):
        self._data=[]

    def add(self,obj):
        if self.find(obj.getId())!=None:
            raise RepositoryException("Element having id=" + str(obj.getId()) + " already stored!")
        self._data.append(obj)
    '''
    def add(self,id,name):
        if self.find(id)!=None:
            raise RepositoryException("Element having id=" + str(id)+ " already stored!")
        object=[id,name]
        self.__data.append(object)
    '''
    def find(self,objectId):
        for e in self._data:
            if objectId==e.getId():
                return e
        return None
    '''
    def remove(self,Id):
        for i in range(0,len(self.__data)-1):
            if self.__data[i].getId()==Id:
                  self.__data.remove(self.__data[i])


    def r(self,obj):
        #if self.find(obj.getId())==None:
            #raise RepositoryException("Element having id=" + str(obj.getId()) + " already stored!")
        j=self.find(obj)
        if j==None:
            raise RepositoryException("doesn't exist")
        i=0
        n=len(self.__data)
        while(i<n):
           if self.__data[i].getId()==obj:
                  self.__data.remove(self.__data[i])
                  n=n-1
                  i=i-1
           i=i+1
    '''
    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        objectId - The objectId that will be removed
        Returns the object that was removed
        Raises RepositoryException if object with given objectId is not contained in the repository
        """
        object = self.find(objectId)
        if object == None:
            raise RepositoryException("Element not in repository!")
        self._data.remove(object)
        return object

    def getIndex(self,index):
        return  self._data[index]

    '''
    def remove2(self,Id):
        i=0
        n=len(self.__data)
        while(i<n):
           if self.__data[i].getDisciplineId()==Id:
                  self.__data.remove(self.__data[i])
                  n=n-1
                  i=i-1
           i=i+1
    '''
    def update(self, object):
        """
        Update the instance given as parameter. The provided instance replaces the one having the same ID
        object - The object that will be updated
        Raises RepositoryException in case the object is not contained within the repository
        """
        el = self.find(object.getId())
        if el == None:
            raise RepositoryException("Element not found!")
        idx = self._data.index(el)
        self._data.remove(el)
        self._data.insert(idx,object)


    '''
    def update(self,p):
        j=self.find(p)
        if j==None:
            print("salut")
        else:
           self.__data[j].setName(p.getName())
    '''
    def getAll(self):
        return self._data


    def __len__(self):
            return len(self._data)
    '''
    def __str__(self):
        r = ""
        for e in self._data:
            r += str(e)
            r += "\n"
        return r
    '''
class RepositoryException(Exception):
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



