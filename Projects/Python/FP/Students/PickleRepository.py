from repository import *
import pickle
class PickleRepository(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self.__fileName=fileName
        self.__load()
    def add(self,obj):
        Repository.add(self,obj)
        self.__store()
    def remove(self,id):
        Repository.delete(self,id)
        self.__store()
    def update(self,object):
        Repository.update(self,object)
        self.__store()
    def __load(self):
        file=open(self.__fileName,"rb")
        try:
            self._data=pickle.load(file)
        except EOFError:
            self._data=[]
        except Exception as exc:
            raise exc
        finally:
            file.close()
    def __store(self):
        file=open(self.__fileName,"wb")
        pickle.dump(self._data,file)
        file.close()