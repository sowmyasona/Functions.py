def greet():
    print('Hello')
    greet()
greet()

def greet(n):
    print('sowmya '+str(n))
greet(9)
greet('SONA')

def greet(*names):
    print('Lucky',names[-3])
greet('MY','Name ','is','Singh')

def details(n,a):
    print('Hey '+n + '! Your Age is '+str(a))
details('SOWMYA',25)
details(n='SONA',a=26)
details(a=24,n='SONA')

def details(n,a):
    print('Hey '+n + '! Your Favourate colour is '+str(a))
n=input('Enter your Name: ')
a=input('Enter your colour: ')
details(n,a)

def r(x,y):
    return x/y
print(r(36,6))

def r(x,y):
    return x+y
print(r(366,44))
print(r(36,44))
print(r(6,44))
print(r(0,44))

def z(p,q):
    return p*q,p+q; 
p,q=[int(x) for x in input().split()]
print(z(p,q))