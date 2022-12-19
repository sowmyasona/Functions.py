def s(a,b):
    c=a+b
    d=a+b
    print('sum is',c)
    print('sum is',d)

s(10,50)
s(2.9,8.7)

def sum(a,b):
    c=a+b
    return c

x=sum(30,20)
print('sum is',x)
y=sum(1.5,4.3)
print("sum is:",y)

def eo(num):
    if num%2==0:
        print(num, "is even")
    else:
        print(num,"is odd")
n=int(input())
eo(n)
eo(22)
eo(97)

def eo(num):
    if num%2==0:
        print(num, "is even")
    else:
        print(num,"is odd")
n=int(input())
eo(n)

def even(x):
    if x%2==0:
        return True
    else:
        return False
# print(even(76))
# let us take a list of numbers
# list1 = [10, 23, 45, 46, 70, 99]
z=[int(x) for x in input().split()]

#call filter() with is_even and lst
# r = list(filter(even, list1))
q = list(filter(even, z))
# print("From the list1 the even values are:",r)
print("From the z the even values are:",q)

p = lambda x,y,z: x+y+z #write lambda function
q = lambda x,y,z: x/y/z #write lambda function
r = p(3,80,5) #call lambda function
z= q(9,3,3)
print('Sum =',r)# display r
print('Divide =',z)# display z