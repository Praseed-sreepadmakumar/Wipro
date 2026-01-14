def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

add(10,20)
sub(20,10)

def hello(greeting='Hello',name='Wprld'):
    print('%s,%s'%(greeting,name))
hello()

def print_param(*params):
    print(params)
print_param('Testing')
print_param(1,2,3,4)
def print_param1(**params):
    print(params)
print_param1(x=1,y=2,z=3)