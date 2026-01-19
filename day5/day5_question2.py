class Calculator:
    def __int__(self,value):
        self.value=value

    def add(self,other):
        print(self.value+other.value)

    def sub(self,other):
        print(self.value-other.value)

    def mul(self,other):
        print(self.value*other.value)

class AdvancedCalculator(Calculator):
    def __int__(self,value):
        self.value=value

    def add(self,other):
        print("This is advanced calculator")
        print(self.value+other.value)

    def __sub__(self, other):
        print(self.value-other.value)

v1=AdvancedCalculator(10)
v2=AdvancedCalculator(25)
v1.add(v2)
v1.sub(v2)
v1.mul(v2)
v1-v2