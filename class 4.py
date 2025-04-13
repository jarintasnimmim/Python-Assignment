#if-else statement

# Jarin = 1000
# Mahin = 850
# Aman = 1200
#
# if(Mahin > Jarin and Mahin > Aman):
#     print('Mahin have more tk')
# elif(Aman < Jarin and Aman > Mahin):
#     print('Aman have more tk')
# else:
#     print('Jarin have more tk')

#For loop

# fruits = ['Apple', 'Mango', 'Watermelon', 'Blueberry', 'Cherry']
# for fruit in fruits:
#     if fruit == 'Cherry':
#         break               #To break an item,the break statement must be used
#     print('Fruits name:', fruit)
#
# DryFruits = ['Cashews', 'Walnuts', 'Raisins', 'Dates', 'Pistachios']
# for dry in DryFruits:
#     if dry == 'Raisins':
#         continue             #To remove a specific item, the continue statement must be used
#     print('DryFruits name:', dry)


#range
# for a in  range(10):
#     print('Flower:', a)              #Start=0, Step=1,  Stop range
#
# for i in range(40,60):
#     print('40-60 range:', i)         #n-1  start=40  end=59
#
# for i in range(60,70,3):
#     print('Odd number:', i)


#While loop
# i = 11
# while i<20:
#     print(i)
#     i+=5

#List
course = ['Python', 15, 'ML', 'AI', 'NLP', 30]
print(len(course))
print('Item access:', course[3])
print('Item access neg:', course[-2])

#start end range
print('Range:', course[1:4])

#end range
print('Range:', course[:4])

#start range
print('Range:', course[2:])
print('Range:', course[-6:])

#change ite value
course [2] = 20
print('New list:', course)

#insert
course.insert(0, 'API')
print('Inserted list', course)

#append
course.append('Data Science')
print('Appened list:', course)

#remove
course.remove(30)
print('Remove', course)

#pop method
course.pop(2)
print('Pop:', course)  #this method removes an element based on a  specific index

#pop
course.pop()
print('POP:', course)   #if no index number is mentioned, it will remove the last item from the list

#sort
alphabetic = ['Tasnim', 'Haider', 'Jarin', 'Farman']
alphabetic.sort()
print('Alphabetic', alphabetic)

#numeric
numeric = [1, 10, 5, 7, 2, 100, 80]
numeric.sort()
print('Numeric:', numeric)