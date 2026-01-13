from functools import reduce
for i in range(1,21):
    print(i)

a=list(filter(lambda x : x%2==0,range(1,21)))
print(a)

a=list(map(lambda x : x*x ,filter(lambda x : x%2==0,range(1,21))))
print(a)


sum=reduce(lambda x,y : x+y ,map(lambda x : x*x ,filter(lambda x : x%2==0,range(1,21))))
print(sum)

for index , value in enumerate(a):
    print(index,value)