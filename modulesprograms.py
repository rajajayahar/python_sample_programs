"""import math

print(math.pi)
print(math.sqrt(49))

print(math.pow(2,8))

from math import sqrt
print(sqrt(2))
"""
"""
import random
import string
print(random.randint(2,20))
random_letter=random.choice(string.ascii_letters)
print(random_letter)
small_letter=random.choice(string.ascii_lowercase)
print(small_letter)
capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

numbers=[1,2,3,4,5,6]
print(random.choice(numbers))
print(random.sample(numbers,k=3))

#try out secret module

"""
"""
import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))

from datetime import datetime
now=datetime.now()
currenttime=now.time()
print(currenttime)

#try out between random days

import sys

print(sys.platform)
print(sys.version)

import os
print(os.getcwd())
print(os.listdir())
"""
"""
import datetime as dt #alias
print(dt.datetime.now())

import requests 

"""

import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())

#os module
import os

print(os.getcwd())#shows the current working directory eg total programs done in python programs so out put is python programs

import os

print(os.listdir())#shows the files and folders

import sys

print(sys.version)#shows the which version is your python
