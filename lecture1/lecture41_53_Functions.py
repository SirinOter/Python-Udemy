
print('Hello from outside the function')

def my_function():   # def = definition
    print('Hello from within the function')

my_function()

def print_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}')

print_name('Bill', 'Gates')


def birthday_gift(item_one, item_two, item_three):
    print(f'For my birthday I hope I get {item_one}, {item_two}, and {item_three}!')

birthday_gift('cat', 'socks', 'dress')

#Scope

def my_function():
    year = 1998
    print(year)   # The year is only defined within the function's scope

year = 2000
print(year) #=> 2000

my_function() #=> 1998

def x_function(*bunch_of_data):
    print(bunch_of_data[-1]) #=> shows the last value of list which is 5

x_function(1,2,3,4,5)

def y_function(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

y_function(lowest_number=8, highest_number=10)

def z_function(country = 'Somewhere in the world...'):
    print(country)

z_function('Sweden')
z_function('India')
z_function()  # Takes the default value as => Somewhere in the world...
z_function('United Kingdom')


def t_function(number_one, number_two):
    return number_one*number_two

mult_num = t_function(10,5)
print(mult_num)  # 50

def f_function(list_of_fruit):
    for fruit in list_of_fruit:
        print(fruit)

fruit = ['Banana', 'Apple', 'Orange']

f_function(fruit)

def remove_elements(numbers_list_arg):
    numbers_list_arg.pop(0)
    numbers_list_arg.pop(-1)
    return numbers_list_arg


numbers_list = [1,2,3,4,5,6,7,8]
updated_list = remove_elements(numbers_list)
print(updated_list)


def fahrenheit_to_celcius_coverter(f_degree):
    c_degree = (f_degree-32) * 5.0 / 9.0
    return c_degree

def celcius_to_fahrenheit_coverter(c_degree):
    f_degree = 9.0 / 5.0 * c_degree +32
    return f_degree

print(fahrenheit_to_celcius_coverter(81))

print(celcius_to_fahrenheit_coverter(10))


def fib_seq(amount):
    n1 = 0
    n2 = 1

    if amount <=0 :
        print('Please change to a positive int')
    elif amount == 1:
        print ('Fib Seq: ')
        print(n1)
    else:
        print('Fib Seq: ')
        count = 0
        while count< amount:
            print(n1)
            fib_sum = n1+n2
            n1=n2
            n2 = fib_sum
            count+=1


def factorial(x):
    y=1
    while x>0:
        y*=x
        x-=1
        return y

factorial_number = factorial(5)

print(factorial_number)



def factorial_y(y):
    if y==1:
        return 1
    else:
        return y* factorial_y(y-1)
factorial_number_y = factorial_y(4)

print(factorial_number_y)



def fib_seq(amount):
    if amount ==0:
        return 0
    elif amount == 1:
        return 1
    else:
        return fib_seq(amount-2)+fib_seq(amount-1)

print(fib_seq(13))

for t in range (13):
    print(fib_seq(t))