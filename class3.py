#int

a = 55
d = -2334466777
f = 12345678909875441
print(type(a))
print(type(d))
print(type(f))

#float

b = 21.34
print(type(b))

#complex

c = 6+3j
print(type(c))

#data conversion

x = 23
y = -34.5
z = 4+5j
# w = float(x)
# print(w)
# print(type(w))
e = complex(x)
print(e)
print(type(e))

f = complex(y)
print(f)
print(type(f))

#complex to int or complex to float both aren't possible

#Boolean
print(type(True))
print(type(False))

x = 10>5
print(x)
print(type(x))

y = 10<5
print(y)
print(type(y))

z = 5<10
print(z)
print(type(z))

#Dictionary

firstdict = {
    'name': 'Jarin Tasnim Mim',
    'id': '111',
    'year': '2025',
    'course': 'Backend API Development'
}
print(firstdict)
print(type(firstdict))

#set
firstset = {'Farman',213,'Tasnim',23.44}
print(firstset)
print(type(firstset))

#List
firstList = [2,1,3,0,0,2,1,1,1,'Jarin']
print(firstList)
print(type(firstList))

#tuple
firstTuple = (2,1,3,0,0,2,1,1,1,'Farman Haider')
print(firstTuple)
print(type(firstTuple))

#Arithmetic operation
x = 10
y = 15
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

#Assignment operation
x = 10
y = 5
y=x
print(y)        #y=10

x+=y
print(x)       #add assign x = x+y #x=20

x -=y
print(x)     #sub assign

x *=y
print(x)       #mul assign

x /=y
print(x)       #div assign

x %=y
print(x)      #mod assign

#comparison operator
x = 10
y = 10
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

#Logical operators
x = 5
y = 7
print(x<y and x>y)
print(x<y or x>y)
print(not (x>y or x==y))

#membership operators
x = ['Farman','Haider']
print('Farman' in x)
print('Haider' not in x)

#Identity operators
x = 11
y = 11
print(x is y)
print(type(x is y))
print(x == y)
print(type(x == y))

#Bitwise operators

x = 12
y = 13
print(~y)
print(x&y)
print(x|y)
print(x<<y)
print(x>>y)
print(x^y)