# Key & Value

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1990
}

print(user_dict['first_name']) # => John

print(user_dict['birth_year']) # => 1990

print(user_dict.get('last_name')) # => Doe

# Add

user_dict['major'] = 'Math'  # => Add key and value, {'first_name': 'John', 'last_name': 'Doe', 'birth_year': 1990, 'major': 'Math'}

print(user_dict)

# Length
print(len(user_dict)) # => 4

# Remove
user_dict.pop('last_name')  # => {'first_name': 'John', 'birth_year': 1990, 'major': 'Math'}
print(user_dict)

# Remove Last Item
user_dict.popitem()  # => Removes the last item {'first_name': 'John', 'birth_year': 1990}
print(user_dict)

# Delete

del user_dict['birth_year']  # => {'first_name': 'John'}
print(user_dict)

#del user_dict   # => delete the file - NameError: name 'user_dict' is not defined
print(user_dict)

# Clear
dict1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1990
}

print(dict1)  # => {'first_name': 'John', 'last_name': 'Doe', 'birth_year': 1990}
dict1.clear() # => Clear inside the dictionary {}
print(dict1)


vehicle = {
    'model':'XC40',
    'make': 'Volvo',
    'year': 2020,
    'mileage': 15.000
}

print(vehicle.get('year'))
print(vehicle['year'])

vehicle['year'] = 2018 # => change the value of dict {'model': 'XC40', 'year': 2018, 'mileage': 15.0}
print(vehicle['year'])  # => 2018

# Add key and value
vehicle['type'] = 'car'

vehicle.pop('make')
print(vehicle)

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1990
}

# Loops
for x in user_dict: # => first_name  last_name  birth_year
    print(x)

for x, y in user_dict.items(): # => first_name John  last_name Doe  birth_year 1990
    print(x,y)


if 'birth_year' in user_dict:  # => if 'birth_year' exists, it will print
    print('yes birth_year exists')

# Copy (if you make some changes in one copy, the other copy will be changed too)
dict2 = user_dict
dict2.popitem()  #=> birth_year will be deleted both from first and copy of the dictionary

print(f'user dict {user_dict}')
print(f'dict2 {dict2}')

#  Copy
dict2 = user_dict
dict2 = user_dict.copy()
dict2 = dict(user_dict)

# Nested Dicts

family = {
    'child1': {
        'first_name':'Joe',
        'last_name':'Doe',
        'birth_year':1990,
    },
'child2': {
        'first_name':'Mary',
        'last_name':'Doe',
        'birth_year':1993,
    },
'child3': {
        'first_name':'Peter',
        'last_name':'Doe',
        'birth_year':1995,
    },
}

print(family) # {'child1':{'first_name': 'Joe','last_name': 'Doe','birth_year': 1990}, 'child2': {...}, 'child3': {...}}


vehicle2 = {
    'model':'XC40',
    'make': 'Volvo',
    'year': 2020,
    'mileage': 15.000
}

for x,y in vehicle2.items():
    print(x,y)

vehicle3 = vehicle2

vehicle3['number of tires'] = 4

print(vehicle2)
print(vehicle3)

sentence = 'I am so happy to learn Python which makes my wife happy and interested in Python Python Python Python'

sentence_dict = {}
for each_word in sentence.split(' '):
    sentence_dict[each_word] = sentence_dict.get(each_word,0)+1