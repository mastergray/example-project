# An example of OOP in Python
class ClassA:

    # A class attribute. It is shared by all instances of this class
    instanceCount = 0

    # CONSTRCTOR :: STRING -> classA
    def __init__(self, name):
        self.name = name 
        ClassA.instanceCount +=1 

    # Instance method :: VOID -> VOID
    def sayHello(self):
        print(f"Hi! My Name Is {self.name}")

    # Class Method :: VOID -> VOID
    # NOTE: A class method can access a shared value between instances - it is called from an instance
    def getCount(cls):
        return cls.instanceCount

    # Static Method :: STRING -> classA
    # NOTE:A static method can be called from the class directly
    def init(name):
        return ClassA(name)
    



