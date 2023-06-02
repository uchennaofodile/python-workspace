#must import module

import os

print(os.name) #nt windows

from os import name #import specific functions

print(name)

#import a module instead of trying to do everything from scratch
#reusable code - less likely to get bugs, easier for other people to understand

#JSON module - transforms data
#dump/dumps turns data into string - can be written to a file
#load/loads turns string back into structured data 
#dumps/loads work with string objects
#load/dump work with file objects

import json

result1 =json.dumps(5)
print(result1)

result2 = json.dumps([1, "string", 3])
print(result2)

result3 = json.loads('[1,"string",3]')
print(result3)