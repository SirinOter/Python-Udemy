
try:
    x=10*(1/0)  # ZeroDivisionError
    print(x)
except ZeroDivisionError as e:
    print(f'[{e} : cannot divide by 0!') # division by zero


    try:
        x='2'+2
        print(x)
    except Exception as e:              # Exception is parent of exceptions
        print(f'Error was thrown :{e}') # Error was thrown :can only concatenate str (not "int") to str
    finally:
        print('show FINALLY no matter what')


'''
     try:
         x=None
         if x is None:
             raise Exception

     except ZeroDivisionError as e:
         print(e)
     except Exception as e:
         print(f'x is None, could not find the answer')

'''

try:
    gateway ='Gateway : Opened'
    print(gateway)
    x= '2'+2

except Exception as e:
    print(f'Error: Must convert string to int')
finally:
    gateway = 'Gateway : Closed'
    print(gateway)