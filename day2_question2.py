class PositiveNumber:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        setattr(instance, self.private_name, value)


class Employee:
    salary= PositiveNumber()
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


e1= Employee('praseed',50000)
print(e1.name)
print(e1.salary)

e2= Employee('ravi',60000)
print(e2.name)
print(e2.salary)

e3= Employee('mark',-10000)
print(e3.name)
print(e3.salary)