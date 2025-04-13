# Q-01: Swap two numbers using arithmetic operations.

p, q = 4, 3
p = p + q
q = p - q
p = p - q
print('p=', p)
print('q=', q)

# Q-02: Get the intersection of two lists.
x = {2, 4, 6, 8, 10}
y = {6, 8, 10, 12, 14}
print('Intersection:', x & y)

# Q-03: Write a for loop that prints numbers from 1 to 10 but skips 3.
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# Q-04: Assign values to three variables in one line and print them.
a, b, c = 10, 12, 15
print('Three variables:', a, b, c)

# Q-05: Write a program using a while loop to print numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

#Q-06: Write a Python program that takes a users age as input and prints a message.
users_age = int(input('Enter your age:'))
if users_age < 18:
    print('You are not adult')
elif users_age > 18:
    print('You are adult')
else:
    print('You are child')

#Q-07: Create a calculator using function.
def calculator(a , b):
    p = a + b
    q = a - b
    r = a * b
    s = a / b
    return p, q, r, s
sum, sub, mul, div = calculator(10, 2)
print('Sum:', sum, 'Sub:', sub, 'Multiple:', mul, 'Division:', div)

#Q-08: Create a tuple with three fruits and print the second fruit.
fruits = ('Apple', 'Strawberry', 'Blueberry')
print('Second Fruit:', fruits[1])

#Q-09: Create a list of five numbers. Append a new number and print the updated list.
numbers =[5, 10, 15, 20, 25]
print(type(numbers))
numbers.append(30)
print('updated list:', numbers)

#Q-10: Write a Python program that checks if a number is positive, negative, or zero.
num = int(input('Enter number:'))
if num > 0:
    print('Positive number')
elif num < 0:
    print('Negative number')
else:
    print('Zero')

