#tuple
details = ('Farman', 'Haider', 'Jarin', 'Tasnim', 'Mim')
#print(type(details))
print('Access item:', details[0])
print('Access Item:', details[-1])
print('Range:', details[:3])
print('Range:', details[2:])
print('Range:', details[1:3])


#update
up = list(details)
up[4] = 'LinYi'
details = tuple(up)
print('Updated Item:', details)

#Add Item
up = list(details)
up.append('Mim')
details = tuple(up)
print('Add Item:', details)

#Remove Item
up = list(details)
up.remove('LinYi')
details = tuple(up)
print('Remove Item:', details)


##Set
a = {2, 3, 11, 45, 11, 66, 100, 3}
print(type(a))
print('Not allow duplicate value:', a)

#Access item
for s in a:
    print('Access item:', s)

print(5 in a)
print(11 in a)

#Add item
a.add(10)
print('Add item:', a)

#discard item
a.discard(100)
print('Discard item:', a)

#del keyword
# del a
# print('Delete set', a)

#set union
b = {1, 2, 3, 4, 5}
c = {4, 5, 6, 7, 8}
print('Union Set:', b|c)

#set intersection
print('Intersection:', b&c)

#Dictionary
Dict = {'Python': 14, 'DS': 10, 'ML': 20, 'Django': 25}
print(type(Dict))
print(Dict)

#get method
x = Dict.get('DS')
print(x)

#keys method
x = Dict.keys()
print(x)

#Values method
x = Dict.values()
print(x)

#add item
Dict['DSA']=15
print('Add item:', Dict)

#update item
Dict.update({'Python': 24, 'DS': 20})
print('Updated:', Dict)

#pop method
Dict.pop('ML')
print('Pop:', Dict)

#Function
def first_name():
    print('Welcome to Function')
first_name()


#Parameter
def addition(x,y):
    w = x+y
    print(w)
addition(5,2)
addition(4,2)
addition(7,2)
addition(2,2)
addition(3,2)

def subtraction(x,y):
    w = x-y
    print(w)
subtraction(4, 2)

def calculator(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a, b, c, d
sum, sub, mul, div = calculator(10,2)
print('Sum:',sum, 'Sub:', sub, 'Multiple:', mul, 'Division:', div)