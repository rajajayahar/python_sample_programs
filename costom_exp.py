"""
class CustomException(Exception):
    pass
def check_number(num):
    if num<0:
        raise CustomException("not allow negative number")
    return num
try:
    result=check_number(7)
except CustomException as e:
    print(e)
else:
    print(result)      
"""                  
"""
class Name_To_Short_Error(Exception):
    pass
name=input("enter the user name:") 
try:
    if len(name)<8:
        raise Name_To_Short_Error("name must be greater than eight leeters")
except Name_To_Short_Error as e:
    print(e)      
else:
    print(name)    
"""
"""
class  InsufficientBalanceError(Exception):
    pass
number=int(input("enter the number:"))
balance=5000
try:
    if number>balance:
        raise InsufficientBalanceError("infusient balance")
     
except InsufficientBalanceError as e:
    print(e)
else:
    print(balance-number)    
"""            

            
     