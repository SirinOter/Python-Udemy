f= open('text.txt', 'r')
print(f.read())
#Must close, can lead to memory leak
f.close()

# Context Manager will open and close automatically
with open('text.txt', 'r') as f:
    print(f.read)
with open('text.txt', 'r') as f:
    print(f.read(15)) # reads the first 15 characters of the file

with open('text.txt', 'r') as f:
    print(f.read(10)) # reads the first 10 characters of the file
    print(f.read(10)) # reads the next 10 characters of the file
    print(f.read(10)) # reads the next 10 characters of the file => in total 30 characters can be seen
    print(f.tell()) # tell me which character are you now

with open('text.txt', 'r') as f:
    print(f.readline)  # Prints the first line of the text file

with open('text.txt', 'r') as f:
    print(f.readlines)  # Prints the all lines of the text file in a list format

# Creating a File

with open('text2.txt', 'w') as x:
    x.write('This is a new file and some text!') # We create and write a file
 # If the file already exists it will overwrite the file
 # if the file does not exist, it will create a new file



#Reading a photo
with open('logocircledarkblue.png','rb') as t: # rb = read binary
    print(t.read())








