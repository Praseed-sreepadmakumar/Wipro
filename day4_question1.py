class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_details(self):
        print("Name:",self.name)
        print("RollNo:", self.rollno)


s1=student("Praseed",20)
s2=student("Mark",10)
s1.display_details()
s2.display_details()