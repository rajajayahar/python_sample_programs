#unexpected events are called exception,that we can resolve od handle
#eg:forgot password etc....(exception handling=resolving problem)
#keywords:1.try-what are types of problem that gonna to form
#2.except-problem solver(try=except=problem resolve)
#3.#finaly-normaly used for the closing the concection with the db(data base)
#4.else.
"""
print("statement 1")
print("statement 2")
print("statement 3")
try:
    value1=10
    value2=0
    value3=value1/value2#zero division error
except ZeroDivisionError:
    print("denominator cant be zero")    

print("statement 4")
print("statement 5")
"""
"""
#try, excep, else
numerator=int(input("enter the numerator"))
denominator=int(input("enter the denomiator"))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("denominator cant be zero")#if 0 means "denominator cant be zero" is out put   
else:
    print(quotient) 
"""
"""
#type error-a string cant be added integer value
try:
    num1=15
    num2="25"
    add=num1+num2
    print(add)
except TypeError:
    print("string cant be added with integer value")     
"""
"""
#index error-index out of range
list1=[1,2,3,4,5]
try:
    print(list1[10])
except IndexError:
    print("index out of  range") 
"""
"""
#key error -dictionary 
book_details={
    "book_id":2,
    "book_name":"life"
} 
try:
    print(book_details["book author"])
except KeyError:
    print("key not found")  
"""
"""
#file not found error-searching for not having file
try:
    with open("text_file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found in directory")   
"""  
"""   
#import error-  
try:
    from math import sqruare
except ImportError as e:
    print(e)#showing what is the error formed on that class ,non custmly showing the error
"""
"""    
#attribute error-giving non functionality to any datastructure
try:
    user_value="welcome"    
    print(user_value.add())
except AttributeError as e:
    print(e)       
"""
"""
#value error-when give the np proper value
try:
    data=int("raja")
except ValueError as e:
    print(e)
"""  
""" 
#name error-when print an not having variable
try:
    
    print(student)
except NameError as f:
    print(f)
finally:
    print("executed normaly")  
"""
"""
#mulitple exception-more than one exception(handle one exception at a time)
try:
    data=int("raja")
    user_value="welcome"    
    print(user_value.add())
  
except ValueError as e:
    print(e)
except AttributeError as e:
    print(e)
"""       
    #resolve the frist problem in until exception as we can a sceen on the terminal box
#multiple exception using another method    

try:
    
    user_value="welcome"    
    print(user_value.add())
    data=int("raja")
except (ValueError,AttributeError) as e:
    print(e)#same output but different method

#custom  exception
 


