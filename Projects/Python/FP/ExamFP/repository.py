import pickle
class Repository:
    def __init__(self):
        self._data=[]

    def add(self,el):
        '''
        adds an element 'el' to the repository
        in:param el:
        '''
        self._data.append(el)
    def get(self,index):
        '''
        Returns the element of the repository on the index position, -1 if the index is not in the radius of the repository
        in:param index:
        :return: element
        '''
        if index>=len(self._data):
            return -1
        return self._data[index]
    def getAll(self):
        '''
        Returns the repository
        :return:
        '''
        return self._data


class PickleRepository(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self.__fileName=fileName
        self.__load()
    def add(self,el):
        Repository.add(self,el)
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
