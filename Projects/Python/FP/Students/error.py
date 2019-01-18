class MyError(Exception):#this class was created for errors.With this class the program didn't stop when the user enter an invalid input
    def __init__(self,msg):
        self.msg=msg
