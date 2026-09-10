"""bus=(input("enter place from and to"))
seat=int(input("please enter seats"))
if seat>2<18:
    print("available")
else:
    print("not available") """ 

"""
delayed=(input(" cancel ticket"))    
if delayed in ("yes","no"):
    print("valid")
else:
    print("unvalid")  """ 

"""age=int(input("enter your age"))
if(age<5):
    print(10)
elif(age>=5 and age<=15):
    print(25)
elif(age>15 and age<30):
    print(50)
else:
    print(100)    """


"""age=int(input("enter your age"))
if age>=15:  
  if age<=30:
    print("junior and super senior")
  else:
    print("senior and junio") 
else:
    print("no result found")   """


"""total_seat=10
booked=0 
while booked < total_seat:
    seat=int(input("check seat avilable"))
    age=int(input("check discount enter age"))
    if seat<=total_seat - booked:
        booked = booked + seat
        if age<12:
           print("avilable and  child discount")
        elif age>60:
            print("avilable and senio citizen")   
        else: 
            print(" avilable")
        print("seat booked:" , booked)  
        print("seats available:" ,total_seat -booked) 
     
    else:
        print("not available")  """
"""

for seats in range(1,10,2):   
   print(seats)
           """


"""seats=10
iterations=int(input("enther the number of iterations: "))
while seats <=iterations:
    print(seats)
    seats+=2 
else:
    print("no seats")    """
"""
#functions 
def creating_account():
    print("1.creating account")
def deposit(balance,amount):
    """"""
    print(f"2.deposit :balance ={balance},total ={amount}")
print(deposit.__doc__)    
def withdraw(totaltaken,balance,gst):    
    print(f"you taken{totaltaken},having balance{balance},gst:{gst}")
def calculate_balance(transaction,balance):
    return transaction-balance  
def transaction_history(*arg):    
    return arg
def loan():    
    print("6.loan eligibility check") 
def exit():    
    print("7.exit from site")

print("1. Creating account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check balance")
print("5. Transaction history")
print("6. Loan eligibility")
print("7. Exit")

choice=int(input("enter the choice"))
if choice==1:
    creating_account()
elif choice==2:
    deposit(1000,500)
elif choice==3:
    withdraw(balance=5000,totaltaken=2000,gst=600)
elif choice==4:
    transaction=int(input("enter a:" ))
    balance=int(input("enter b:"))  
    print("balance:",calculate_balance(transaction,balance))
elif choice==5:
    print(transaction_history(300,500,400))  
elif choice==6:
    loan()  
elif choice==7:
    exit()
else:
    print("invalid option")        
 """


"""

def create_account(account_type="savings"):
    return f"my account type is {account_type}"
print(create_account("savings"))
print(create_account("current"))
print(create_account("permanent"))     

def transaction_history(*transaction):
    print(f"transactions:{transaction}")
transaction_history(2000,3000,4000,5000)    

def customer_details(**data):
    print(f"details of customer:{data}")
customer_details(name="raja",age=22,place="tamilnadu")


def display_message():
    print("hellow")

result = display_message()
print(result)
 
""" 
"""
customer_name={"raja": 500,"jayahar" :1000,"biju" :2000}
def name():
    print("total bill balance")
    def due():
        for customer,amount in customer_name.items():
            print("customer name:",customer,"amount:",amount)
       
    due()
  
name()  
"""
"""
gst=lambda a:a+50
print(gst(300))

interset=lambda a:a*0.5
print(interset(200))

numbers = (50,70,30,55,22,11)
result = filter(lambda a:a >= 50 ,numbers)
print(list(result))

name = ("raja","kholi","virat","jeva")
result = filter(lambda a:len(a)>= 5 ,name)
print(list(result))

principal=int(input("enter principal:"))
rate=int(input("enter rate:"))
years=int(input("enter a year:"))
def calculate_amount():
    amount = principal * (1+rate/100)**years
    return amount
print(calculate_amount())
"""
#data structures
bookname="python","java","c++"
authorname=["alex","revon","ceron"]
member_details=("raja","jayahar","biju")
print(bookname)
print(authorname)
print(member_details)
bookname[0]
bookname[-1]
bookname[0:5]
print(bookname)
print(authorname[0][0:2])
bookname="python"
print(bookname.upper())