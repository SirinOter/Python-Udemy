
greetings = 'Welcome to the Python World'

print(greetings[0]) # => W

#Slicing
print(greetings[0:7]) # => Welcome - 7 is not included

print(greetings[0:10:2]) # => Wloet - 10 is not included every other

#Length
print(len(greetings))  # => legth of greeting is 27

# Returning a list seperated by spaces
print(greetings.split())   # =>   ['Welcome', 'to', 'the', 'Python', 'World']

# Finds and returns index
print(greetings.find('Python'))  # =>   15  Python starts at 15th index

# Joins
print(greetings,','.join('abcdefg'))  # => Welcome to the Python World a,b,c,d,e,f,g

print(greetings, ':'.join(('10', '23', '44', '50')))  # => Welcome to the Python World 10:23:44:50

password = '      abc123!        '

if password.strip()=='abc123!':      #=> strip clear all the empty spaces around the string
    print('Password is successful') #=> Password is successful
else:
    print('Password is incorrect')

# Replace Functionality
say_hi = 'Welcome to the Python World!'

new_say_hi = say_hi.replace('Welcome to', 'Hello there and welcome to') #=>  Hello there and welcome to the Python World!

print(new_say_hi)

success_quote = 'you win some and you lose some'

new_success_quote = success_quote.replace('lose', 'learn')

print(new_success_quote)  #=> you win some and you learn some

string_list = 'lets make this a list'

make_list = string_list.split()

print(make_list)   #=>  ['lets', 'make', 'this', 'a', 'list']

print(string_list[1])







