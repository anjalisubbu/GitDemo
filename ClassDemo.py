class calculator :

    num = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addint(self):

        return self.a + self.b + calculator.num

    def multiplication(self):

        return self.a * self.b

    def getData(self):

        print("Calculator is working fine")


obj = calculator(10, 5)
obj1 = calculator(2, 5)
print(obj.addint())
print(obj1.multiplication())
obj.getData()

