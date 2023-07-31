my_tuple = (1,2,3,4,5)
#You can not chage values of Tuples, ypu can not delete or add new values

print(my_tuple) # => (1, 2, 3, 4, 5)

print(my_tuple[-1]) # => 5 last element

print(my_tuple[1:4]) # => (2, 3, 4) 4 is not included

for x in my_tuple:  # => 1 2 3 4 5
    print(x)

print(len(my_tuple))  # => length = 5

brand = ('IBM', 'Apple', 'HP', 'Asus', 'Lenovo')

print(brand[2])

print(brand[0:3])

print(len(brand))

for x in brand:
    print(x)


# Sets = Used most often to remove duplicates and to check if item exists, unordered listing
# Lists are faster than sets when you want to iterate over the values

my_set = {'apples', 'bananas', 'oranges', 'melons', 'etc...'}

print(my_set) # {'melons', 'bananas', 'etc...', 'apples', 'oranges'}
              # each time we run it the order is changed inside of set

print('melons' in my_set) # True

print('grapes' in my_set) # False

for x in my_set:
    print(x)

# print(my_set[3]) =>Since it is unorderd you can not index through a set

#Remove
my_set.remove('oranges')
print(my_set)  # {'apples', 'bananas', 'melons', 'etc...'}

# my_set.remove('grapes') You will get an error if you want to remove  which is not exist in set

my_set.discard('grapes') # You won't get an error if you don't have this item in set

# Add

my_set.add('pears') # {'etc...', 'pears', 'apples', 'melons', 'bananas'}
print(my_set)

my_set.update(['mangoes', 'tangerines']) # Update= If you want to add more than one item
print(my_set)                            # {'pears', 'bananas', 'mangoes', 'tangerines', 'melons', 'etc...', 'apples'}

my_set.clear()
print(my_set) # set()

# Combine
set_one = {1,2,3,4,5}
set_two = {6,7,8,9,10}

set_three = set_one.union(set_two)
print(set_three)  #  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

colors = {'red', 'blue', 'green', 'pink', 'purple'}

print(len(colors)) # 5

colors.remove('green')
print(colors)

colors.update(['black', 'white'])
print(colors) # {'purple', 'red', 'black', 'white', 'pink', 'blue'}

numbers= {'one', 'two', 'three'}

combine = colors.union(numbers) # {'three', 'pink', 'red', 'black', 'white', 'two', 'purple', 'one', 'blue'}
print(combine)

