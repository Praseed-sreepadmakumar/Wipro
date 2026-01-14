def generator(n):
    count=0
    a=0
    while count < n:
        yield a
        count += 1
n=int(input("Enter the limit:"))
for num in generator(n):
    print(num)