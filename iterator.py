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