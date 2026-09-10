#fuctions
# 1.user defind
"""
def function name(parameters):
    code to be executed
"""
# user defind without parameters 
"""
def wellcome():   
    print("wellcome raja")

wellcome()
wellcome()
"""
"""
# user defind with parameters
def greeting(username,userage):
    print(f"wellcome {username},you are {userage} years old")

greeting("raja",22)
"""
"""
def addition(num1,num2):
    return num1+num2
num1=int(input("frist number: "))
num2=int(input("second number: "))
print(addition(num1,num2))
"""
"""
#positional arguments .possition is matter
def book_ticket(moviename,customername,seats,ticketprice):
    totalprice=seats*ticketprice
    return f"{customername} booked {seats} tickets for {moviename}. total amount :{totalprice}"
print(book_ticket("jilla","raja",7,150))  
"""

#keyword arguments .position doest matter here
"""
def customer_details(customername,customerage,city):
    print(f"{customername}age is{customerage} from {city}")
customer_details(customerage=22,customername="raja",city="marthandam") 
"""
#default arguments 
"""
def booking_status(customername="raja",status="conform",screen="screen1"):
    print(f"{customername} status {status} screen alocated is{screen}")

booking_status("jayahar")   
booking_status("jerry","pending") 
booking_status("jack","pending") 
"""
"""
#multiple arguments
def calculate_bill(*ticketprice):
    print(f"ticketprice : {ticketprice}")
calculate_bill(120,300,400,500,420)    
"""
"""
#try out kwargs

#built in function

print(len("raja"))
print(sum([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sorted([4,5,6,7,8]))
print(sorted([5,2,4,9,10],reverse=True))
print(sorted(["r","a","j"],reverse=True))
"""
"""
def example(**kwargs):
    print(kwargs)

example(a=100, b=200, c=300)
    
def ticket_price(*ticket):
    print(ticket)

ticket_price(100, 200, 300)  
"""
"""
#legb rule
def student_details():
    name="raja"
    print("student_name:",name)
student_details()    
#print("student_name:",name)

#global variable

college_name="maria college"
def display():
    print("college name:",college_name)
display()    
print("college name:",college_name)
"""
"""
#enclosing variable

def department():
    department_name="cse"
    def student():
        print("department name:",department_name)
    student()
department()        
"""
"""
tax=50#global variable
def shopping():
    discount=100#enclosing
    def bill():
        amount=500#local
        total_amount=amount-discount+tax
        print("total amount:",total_amount)
    bill()
shopping() 
"""

#recursive function
#.base case
#.request case
"""
def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
num=int(input("enter a number:"))
print(factorial(num)) 
""" 

#working
#6*factorial(5)
#6*5factorial(4)
#6*5*4factorial(3)
#6*5*4*3factorial(2)
#6*5*4*3*2factorial(1)
      
#lamda function  or anonyms function
#lambda arguments:expression    syntax
"""
def add(num1,num2):
    return num1+num2
print (add(2,4))    

add=lambda a,b:a+b
print(add(4,5))

square=lambda a:a*a
print(square(3))

even=lambda a:a % 2 == 0 
num=int(input("enter a"))
print(even(num))
"""
multi=lambda a,b:a*b
print(multi(4,4))

smallest=lambda a,b:min(a,b)
print(smallest(3,4))

big=lambda a,b:max(a,b)
print(big(3,4))

calculate=lambda a:10% a
print(calculate(4))

celsius_to_fahrenheit=lambda c:(c*9/5)+32
print(celsius_to_fahrenheit(100)) 

age=lambda a:(a >= 18)
print(age(18))

numbers = (50,70,30,55,22,11)
result = filter(lambda a:a >= 50 ,numbers)
print(list(result))

name = ("raja","kholi","virat","jeva")
result = filter(lambda a:len(a)>= 5 ,name)
print(list(result))


result = filter(lambda a:(len(a)>= 5 ))
print(result(raja))