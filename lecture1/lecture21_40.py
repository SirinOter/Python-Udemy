my_list=[1,2,3,4,5,6,7,8,9,10]

print(my_list[1:8])  # => [2, 3, 4, 5, 6, 7, 8] 8th index is not included

print(my_list[1:8:2]) # => [2, 4, 6, 8] skip in every 2 item

new_list = my_list[1:5]  # => new_list = [2, 3, 4, 5]
print(new_list)

colour_list = ['red', 'blue', 'green', 'pink', 'purple']

print(colour_list[1:4])    # => ['blue', 'green', 'pink']

my_list.append(11)   # => added at the end of the list  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(my_list)

my_list.insert(3,12) # => added third index 12  [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 10, 11]

print(my_list)

my_list.remove(8)  # => delete the value not index  [1, 2, 3, 12, 4, 5, 6, 7, 9, 10, 11]

print(my_list)

my_list.pop(3) # => pop delete the element by index  [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]

print(my_list)

my_list.reverse() # => reverse the elements on the list  [11, 10, 9, 7, 6, 5, 4, 3, 2, 1]

print(my_list)

number_list=[10,6,98,52,4,21]

number_list.sort()   # => sort in ascending orders  [4, 6, 10, 21, 52, 98]
print(number_list)

colours = ['red', 'blue', 'green', 'pink', 'purple']


colours.pop(4)
colours.append('white')

print(colours)

nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(len(nested_list))   # => 3 elements
print(nested_list[1][2])   # => 6 elements

# Boolean
is_human = True
do_you_love_fashion = False
donut ='Donut'
fav_number = 7
print(type(donut)) # type shows that which type of data it is => str, int, boolean

# If Statements

number =101

if number ==100:      # => end of application
    print('number is equal to 100')
print('end of application')

x=100

if x!=100:
    print('x is equal to 100') # => it will not be executed until this condition is true

if x>10:
    print(f'x is equal to {x}') # => x is equal to 100

# Else Statements

number= 15  # =>   number is not equal to 15
if number ==100:
    print(f'number is  equal to {number}')
else:
    print (f'number is not equal to {number}')

hour =12
if hour <18:
    message ='Good Morning'
else:
    message = 'Good Afternoon'
print(message)

# Elif Statements

hour =21
if hour<15:
    print('Good morning!')   # => <15
elif hour<20:
    print('Good Afternoon!') # => 15<hour<20
else:
    print('Good Night!')  # => hour>20

grade =70

if grade>=90:
    print('A')
elif grade>=80 and grade<90:
    print('B')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 60 and grade < 70:
    print('D')
else:
    print('F')


# For Loop: Iteration

numbers_list = [1,2,3,4,5]

print(numbers_list[0])
print(numbers_list[1])
print(numbers_list[2])
print(numbers_list[3])
print(numbers_list[4])

for x in numbers_list: # =>  1,2,3,4,5
    print(x)

for x in range(3,6): # =>  value between 3 to 6(6 is excluded) 3,4,5
    print(x)

    sum_of_loop = 0
    for x in range(3, 6):
        sum_of_loop +=x
        print(sum_of_loop)  # =>  3,7,12 (3+4+5)

co_workers = ['Tom', 'Ben', 'Adil']

for x in co_workers:      # =>  Hello Tom! Hello Ben! Hello Adil!
    print(f'Hello {x}!')

for x in co_workers:
    if x=='Tom':
        print('Hello Tom!')       # =>  Hello Tom!
        break

# While Loops

x= 0
while x<10:
    x+=1
    if x==6:
        continue  # skip
    print (x)     # 1,2,3,4,5,7,8,9,10 (skipped 6)


y=0
while y<10:
    print (y)
    y+=1
else:
    print('y is now equal or larger to 10')      # 1,2,3,4,5,6,7,8,9,y is now equal or larger to 10

# Modula
i=10
while i<=10 and i>5:
    if i % 2==0:
        print(f'{i} is divisible by 2')
    else:
        print(f'{i} is not divisible by 2')
    i-=1

    '''
    10 is divisible by 2
    9 is not divisible by 2
    8 is divisible by 2
    7 is not divisible by 2
    6 is divisible by 2
    '''

list = [1,2,3,4,5,6,7,8]

for x in list:
    if x == 3 or x == 7:
        continue
    print(x)

z=5
while z>=1:
    print(z)
    z-=1
else:
    print('GO!')


for t in range(1,51):
    if t % 3 ==0:
        print('Fizz')

    elif t % 5 ==0:
        print('Buzz')

    elif t % 3 ==0 and t % 5 ==0:
        print ('FizzBuzz')

    else:
        print(t)



