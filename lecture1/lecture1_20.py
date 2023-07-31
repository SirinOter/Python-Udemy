print(2+2)
bank_amount = 100
item_one = 25
item_two = 30
item_three = 15

'''
 we subtract the amount
'''

bank_amount-= item_one # bank_amount = bank_amount - item_one
bank_amount-=item_two
bank_amount-=item_three

print(bank_amount)

print('You\'re Welcome')
print('next\n line' )

statement = '''
Attention
Everyone
This 
Is 
Very 
Important
'''

print(statement)

my_name = 'Shirin'
print(my_name+' '+'Oter')

last_name = 'Oter'

print(my_name+' '+last_name)

hello_text = 'Hello, {my} {last}'\
    .format(my=my_name, last=last_name)

print(hello_text)

number_of_shoes = 8

hello_statement = \
f'{my_name} has {number_of_shoes} pairs of shoes'

print(hello_statement)

message = 'Welcome to Python!'

print(message.upper()) # upper() lower() capitalize()=>first letter big

print (message.lower())

print (message.capitalize())

print(message.count('o'))

print(message.endswith('!'))

print(message.isdigit())

gift1 = 'job'
gift2 = 'health'

birthday_gifts_phrase = f'This birthday I want {gift1} and {gift2}'

print(birthday_gifts_phrase)

birthday_gifts_phrase = 'This birthday I want {}'\
                        ' and {}'.format(gift1, gift2)

print(birthday_gifts_phrase)

birthday_gifts_phrase = 'This birthday I want {first}'\
                        ' and {second}'.format(first = gift1, second = gift2)

print(birthday_gifts_phrase.upper())

name = input('Enter your name: ')
age = input('Enter the year you were born: ')

print(f'{name} was born in {age}')

item_one = input('What is the first gift you would like?')
item_two = input('What is the second gift you would like')

birthday_gifts = f'For my birthday I want {item_one}'\
    f'and {item_two}'

print(birthday_gifts.upper())

my_list = [6,7,8,9,10]

print(my_list)
print(my_list[4])

print(my_list[-1]) # -1 always return the last element of the arrow

my_list[1]=100 #we can change the content of arrow
print(my_list)

print(len(my_list)) #len=length of arrow

animal_list=['Tiger', 'Lion', 'Bear']
print(animal_list)
print(len(animal_list))


colour_list = ['red', 'blue', 'green', 'pink', 'purple']

print(len(colour_list))
print(colour_list[2])










