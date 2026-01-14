class Counter:
    def __init__(self,limit):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val=self.current
            self.current +=1
            return val
        else:
            raise StopIteration

n=int(input("Enter the limit:"))
obj1=Counter(n)
for i in obj1:
    print(i)

################################################################
def fib_generator(n):
    a, b= 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a+b
        count += 1
n=int(input("Enter the N:"))
for i in fib_generator(n):
    print(i,end = " ")
print()

#########################################################################

#For iterator
n=int(input("Enter the limit:"))
obj1=Counter(n)
print("--- Iterator Output ---")
for i in obj1:
    print(i)
#For Generator
def simple_generator(n):
    current=1
    while current <= n:
        yield current
        current +=1

print("\n--- Generator Output ---")
a= simple_generator(5)
for i in a:
    print(i)