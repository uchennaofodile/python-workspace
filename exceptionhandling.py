try:
    value = 5/0
except ZeroDivisionError: #set the exception that will be caught and clean up
    value = 1
    print(value)