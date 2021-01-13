x = input('Enter number 1: ')
y = input('Enter number 2: ')

# Solution 1
#-----------------------
# try:
#     z = int(x)/int(y)
# except Exception as e:
#     print(e)
#     z = None


# Solution 2 for a more specific errors
#-----------------------

try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('You cannot divide by zero')
    z = None
except TypeError as e:
    print('Type error exception')
    z = None
except Exception as e:
    #finds out the specific exception.... now we know it's a ValueError. So replace 'Exception' with Value Error
    print('exception type -----> ', type(e).__name__)
    z = None

print('Division answer: ', z)