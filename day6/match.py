import re
text="Python is pretty good"
result=re.match("Python",text)
if result:
    print("Match found")
else:
    print("Not found")
print(result.group())

email="asdasdad@gmail.com"
if re.match(r"[a-zA-Z]+@gmail.com",email):
    print("Valid Start")

result2 = re.fullmatch(r"\d{10}", "1234567898")
print(result2)

print(re.findall(r"\d+", "price 50 and 100 and 200"))

for n in re.finditer(r"\d+", "A1, B33, C444"):
    print(n.group(), n.start(), n.end())


print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abnkkkkkknnc"))

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

print(re.search("python","Python",re.I))

text4="one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))