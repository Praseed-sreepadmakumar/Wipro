import re

emp_id=input("Enter the employee id:")
if re.match(r"EMP+\d{3}",emp_id):
    print("Valid employee id")
else:
    print("Invalid employee id")

text="12372437hello@gmail.com1231290"

result=re.search(r"^[\w\.-]+@[\w\.-]+.com",text)
print(result.group(),result.start(),result.end())


text4 = "one\ntwo\nthree"
print(re.findall(r"^t\w+", text4, re.M))
